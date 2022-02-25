import os
from typing import Dict, Optional
import graphviz

from src.l_systems.LSystem import LSystem, Node

RENDER_PATH = os.path.join('renderings')


def get_graphviz_style(node: Node):
    style = node.style
    n_attrs = {}
    e_attrs = {}
    if not style.visible:
        e_attrs['style'] = 'invis'
        n_attrs['style'] = 'invis'
    if style.solid:
        n_attrs['style'] = 'filled'
        n_attrs['fillcolor'] = 'black'
    return n_attrs, e_attrs


def __dfs(graph: Dict[Node, Dict], parent: Optional[Node], dot: graphviz.Digraph):
    for node in graph:
        nid = str(node.id)
        n_attrs, e_attrs = get_graphviz_style(node)
        dot.node(nid, label=node.label, **n_attrs)
        if parent:
            pid = str(parent.id)
            dot.edge(pid, nid, **e_attrs)
        __dfs(graph[node], node, dot)


def system_to_graphviz(system: LSystem, iterations: int, name: str) -> graphviz.Digraph:
    graph = system.get_graph(iterations)
    dot = graphviz.Digraph(comment=name)
    __dfs(graph, None, dot)
    return dot


def local_render(dot: graphviz.Digraph):
    if not os.path.isdir(RENDER_PATH):
        os.makedirs(RENDER_PATH)
    dot.render(directory=RENDER_PATH, filename=dot.comment)
