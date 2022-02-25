
import sys
from src.models.algae import algae
from src.models.fractal_tree import fractal_tree
from src.models.cantor_set import cantor_set
from src.l_systems.renderer import local_render, system_to_graphviz

KEYWORD_MAP = {
    'algae': algae,
    'fractal-tree': fractal_tree,
    'cantor-set': cantor_set
}


def main():
    system_in, iterations = sys.argv[1:]
    system = KEYWORD_MAP[system_in]()
    graph = system_to_graphviz(system, int(iterations), f'{system_in}_{iterations}')
    local_render(graph)


if __name__ == '__main__':
    main()
