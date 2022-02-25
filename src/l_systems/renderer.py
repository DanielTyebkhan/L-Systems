import os
from typing import Dict
import graphviz

from src.l_systems.LSystem import LSystem, Node

RENDER_PATH = os.path.join('renderings')


def __dfs(graph: Dict[Node, Dict], parent: Node, dot: graphviz.Digraph):
    for node in graph:
        nid = str(node.id)
        dot.node(nid, label=node.label)
        if parent:
            pid = str(parent.id)
            dot.edge(pid, nid)
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
