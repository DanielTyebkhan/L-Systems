from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, Dict, List, Optional
import uuid

from src.l_systems import util


class Leafable(ABC):
    @abstractmethod
    def is_leaf(self) -> bool:
        ...


SymbolLike = str


@dataclass
class NodeStyle:
    solid: bool = False
    visible: bool = True


class Node(Leafable):
    """
    Node class for L system graph.
    """
    def __init__(self, label: SymbolLike, is_leaf: bool = False, style: NodeStyle = None):
        self.label = label
        self.__is_leaf = is_leaf  # production rules are not applied to leaves
        self.id = uuid.uuid4()
        self.style = style or NodeStyle()

    def is_leaf(self):
        return self.__is_leaf

    def __hash__(self):
        return self.id.int

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.id == other.id
        return super().__eq__(other)


NodeFactory = Callable[[], List[Node]]


class Axiom(Leafable):
    def __init__(
            self, symbol: SymbolLike, is_leaf: bool = False,
            node: Optional[Node] = None
    ):
        self.symbol = symbol
        self.__is_leaf = is_leaf
        self.node = node or Node(symbol, is_leaf=is_leaf)

    def is_leaf(self) -> bool:
        return self.__is_leaf


@dataclass(frozen=True)
class Production:
    predecessor: SymbolLike
    successor_generator: Callable[[], List[Node]]

    def apply(self, node: Node) -> List[Node]:
        if not node.is_leaf() and self.predecessor == node.label:
            return self.successor_generator()
        return []


LSysGraph = Dict[Node, "LSysGraph"]


@dataclass
class LSystem:
    """
    Implementation of a deterministic L-system G = (V,w,P)
    TODO: constructor to validate productions against axioms 
          to enforce determinism and valid entries
    """
    axiom: List[Axiom]
    productions: List[Production]

    def get_graph(self, iterations: int) -> LSysGraph:
        graph = {}
        generation = []
        for a in self.axiom:
            node = a.node
            graph[node] = {}
            generation.append((node, graph[node]))
        if iterations > 0:
            for i in range(iterations):
                next_gen = []
                for node, entry in generation:
                    new_nodes = util.flat_map(lambda p: p.apply(node), self.productions)
                    for new_node in new_nodes:
                        entry[new_node] = {}
                        next_gen.append((new_node, entry[new_node]))
                generation = next_gen
        return graph
