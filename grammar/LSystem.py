from dataclasses import dataclass
from typing import Dict, List, Set


@dataclass(frozen=True)
class Node:
    label: str
    id: int


@dataclass(frozen=True)
class Production:
    predecessor: str
    successors: List[str]

        
@dataclass(frozen=True)
class LSystem:
    """
    Implementation of a deterministic L-system G = (V,w,P)
    TODO: constructor to validate productions and axiom against alphabet 
          to enforce determinism and valid entries
    """
    alphabet: Set[str]
    axiom: Set[str]
    productions: Set[Production]

    def get_graph(self, iterations: int) -> Dict:
        __id = -1
        def make_node(label: str) -> Node:
            nonlocal __id
            __id += 1
            return Node(label, __id)

        def apply_production(production: Production, node: Node) -> List[Node]:
            if node.label == production.predecessor:
                return [make_node(s) for s in production.successors]
            return []

        graph = {}
        generation = []
        for var in self.axiom:
            node = make_node(var)
            graph[node] = {}
            generation.append((node, graph[node]))
        if iterations > 0:
            for i in range(iterations):
                next_gen = []
                for node, entry in generation:
                    for production in self.productions:
                        new_nodes = apply_production(production, node)
                        for new_node in new_nodes:
                            entry[new_node] = {}
                            next_gen.append((new_node, entry[new_node]))
                        if len(new_nodes) > 0:
                            break
                generation = next_gen
        return graph


