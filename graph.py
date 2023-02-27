import networkx as nx
import matplotlib.pyplot as plt

g=nx.Graph()

g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)

g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,3)
g.add_edge(3,4)


nx.draw(g, with_labels=True)
plt.show()