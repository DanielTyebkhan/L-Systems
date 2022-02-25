from pprint import pprint

from src.l_systems.LSystem import LSystem, Node, Production, Axiom, NodeStyle

A = 'A'
B = 'B'


def cantor_set() -> LSystem:
    """
    Lindenmayer's L-system for modeling fractal/binary trees
    """
    def b_node(): return Node(B, style=NodeStyle(visible=False))
    def a_node(): return Node(A, style=NodeStyle(solid=True))
    return LSystem(
        [Axiom(A, node=a_node())],
        [
            Production(A, lambda: [a_node(), b_node(), a_node()]),
            Production(B, lambda: [b_node(), b_node(), b_node()])
        ]
    )


if __name__ == '__main__':
    pprint(cantor_set().get_graph(4))
