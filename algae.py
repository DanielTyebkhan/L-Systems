import graphviz

from renderer import local_render


"""
Lindemayer's L-system for modeling the biological growth of algae
"""
dot = graphviz.Digraph(comment="Algae L-System")

dot.node('A')
dot.node('B')
dot.edge('B', 'A')
local_render(dot)