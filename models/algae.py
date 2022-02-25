from pprint import pprint
from grammar.LSystem import LSystem, Production

from render.renderer import local_render

A = 'A'
B = 'B'

def algae() -> LSystem:
    """
    Creates Lindenmayer's L-system for modeling the biological growth of algae
    """
    return LSystem(
        {'A', 'B'}, {'A'}, 
        [Production('A', ['A', 'B']), Production('B', ['A'])]
    )
    
if __name__ == '__main__':
    pprint(algae().get_graph(4))