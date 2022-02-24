import os
import graphviz
RENDER_PATH = os.path.join('renderings')

def local_render(dot: graphviz.dot.Dot):
    if not os.path.isdir(RENDER_PATH):
        os.makedirs(RENDER_PATH)
    dot.render(directory=RENDER_PATH, filename=dot.comment)
