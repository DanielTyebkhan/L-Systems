import os
from typing import Dict
import graphviz

from LSystem import Node, LSystem
RENDER_PATH = os.path.join('renderings')

def __dfs(graph: Dict[Node, Dict], parent: Node, dot: graphviz.Digraph):
    for node in graph:
        id = str(node.id)
        pid = str(parent.id)
        dot.node(id, label=node.label)
        if parent:
            dot.edge(pid, id)
        __dfs(graph[node], node, dot)


def system_to_graphviz(system: LSystem, iterations: int, name: str) -> graphviz.Digraph:
    graph = system.get_graph(iterations)
    dot = graphviz.Digraph(comment=name)
    __dfs(graph, None, dot)
    return dot


def local_render(dot: graphviz.dot.Dot):
    if not os.path.isdir(RENDER_PATH):
        os.makedirs(RENDER_PATH)
    dot.render(directory=RENDER_PATH, filename=dot.comment)
