from abc import ABC, abstractmethod
from dataclasses import dataclass
from lib2to3.pytree import Leaf
from symtable import Symbol
from typing import Callable, Dict, List, Set, Union
import uuid

from numpy import isin

from util import flat_map, flatten


class Leafable(ABC):
    @abstractmethod
    def is_leaf(self) -> bool:
        ...


Symbollike = str


@dataclass(unsafe_hash=True)
class Node(Leafable):
    label: Symbollike
    id: uuid.UUID
    __is_leaf: bool = False # production rules are not applied to leaves

    def __init__(self, label: str, is_leaf: bool):
        self.label = label
        self.__is_leaf = is_leaf
        self.id = uuid.uuid4()

    def is_leaf(self):
        return self.__is_leaf


NodeFactory = Callable[[], List[Node]]

    
@dataclass(frozen=True)
class Axiom(Leafable):
    symbol: Symbollike
    __is_leaf: bool = False

    def is_leaf(self) -> bool:
        return self.__is_leaf


@dataclass(frozen=True)
class Production:
    predecessor: Symbollike
    successor_generator: Callable[[], List[Node]]
    
    def apply(self, node: Node) -> List[Node]:
        if not node.is_leaf() and self.predecessor == node.id:
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
            node = Node(a.symbol, a.is_leaf())
            graph[node] = {}
            generation.append((node, graph[node]))
        if iterations > 0:
            for i in range(iterations):
                next_gen = []
                for node, entry in generation:
                    new_nodes = flat_map(lambda p: p.apply(node), self.productions)
                    for new_node in new_nodes:
                        entry[new_node] = {}
                        next_gen.append((new_node, entry[new_node]))
                generation = next_gen
        return graph


