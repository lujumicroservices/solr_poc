import networkx as nx
import matplotlib.pyplot as plt

# Create an undirected graph
G = nx.Graph()

# Add nodes
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])

# Add edges
G.add_edges_from([ ('B', 'C'), ('C', 'D'), ('D', 'E')])

# Draw the graph
pos = nx.spring_layout(G)  # Spring layout
nx.draw(G, pos, with_labels=True, node_size=1000, font_size=10, font_color='black')
plt.show()
print("test")