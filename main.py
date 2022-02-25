
import sys
from src.models.algae import algae
from src.l_systems.renderer import local_render, system_to_graphviz

KEYWORD_MAP = {
    'algae': algae

}


def main():
    system_in, iterations = sys.argv[1:]
    system = KEYWORD_MAP[system_in]()
    graph = system_to_graphviz(system, int(iterations), 'Algae')
    local_render(graph)


if __name__ == '__main__':
    main()
