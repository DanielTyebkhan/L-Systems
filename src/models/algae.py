from pprint import pprint

from src.l_systems.LSystem import LSystem, Node, Production, Axiom


A = 'A'
B = 'B'


def algae() -> LSystem:
    """
    Lindenmayer's L-system for modeling the biological growth of algae
    """
    return LSystem(
        [Axiom(A)], 
        [
            Production(A, lambda: [Node(A), Node(B)]),
            Production(B, lambda: [Node(A)])
        ]
    )
        
    
if __name__ == '__main__':
    pprint(algae().get_graph(4))