from pprint import pprint
from grammar.LSystem import Axiom, LSystem, Node, Production

from render.renderer import local_render

A = 'A'
B = 'B'

def algae() -> LSystem:
    """
    Creates Lindenmayer's L-system for modeling the biological growth of algae
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