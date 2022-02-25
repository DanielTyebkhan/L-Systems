from pprint import pprint

from src.l_systems.LSystem import LSystem, Node, Production, Axiom

ZERO = '0'
ONE = '1'


def fractal_tree() -> LSystem:
    """
    Lindenmayer's L-system for modeling fractal/binary trees
    """
    return LSystem(
        [Axiom(ZERO)],
        [
            Production(ZERO, lambda: [Node(ONE), Node(ZERO, True), Node(ZERO)]),
            Production(ONE, lambda: [Node(ONE), Node(ONE)])
        ]
    )


if __name__ == '__main__':
    pprint(fractal_tree().get_graph(4))
