
from algae import algae
from render.renderer import local_render, system_to_graphviz


def main():
    system = algae()
    graph = system_to_graphviz(system, 7, 'Algae')
    local_render(graph)

if __name__ == '__main__':
    main()