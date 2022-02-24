import os
import graphviz

from grammar.LSystem import LSystem
RENDER_PATH = os.path.join('renderings')

def system_to_graphviz(system: LSystem, iterations: int, name: str) -> graphviz.Digraph:
    dot = graphviz.Digraph(comment=name)
    __curr_id = -1
    def add_node(label) -> int:
        nonlocal __curr_id
        __curr_id += 1
        dot.node(__curr_id, label=label)
        return __curr_id
    generation = []
    for var in system.axiom:
        generation.append(add_node(var))

def local_render(dot: graphviz.dot.Dot):
    if not os.path.isdir(RENDER_PATH):
        os.makedirs(RENDER_PATH)
    dot.render(directory=RENDER_PATH, filename=dot.comment)
