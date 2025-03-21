import networkx as nx
import matplotlib.pyplot as plt

# Create directed weighted graph
G = nx.DiGraph()
G.add_weighted_edges_from([
    ("A", "B", 5), 
    ("A", "C", 3), 
    ("B", "D", 2)
])

# Draw graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=700, font_size=16)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

# Adjacency matrix
adj_matrix = nx.to_numpy_array(G)
print("Adjacency Matrix:\n", adj_matrix)

# Degree of node
print("Degree of A:", G.degree("A"))

# Shortest path
path = nx.shortest_path(G, source="A", target="D", weight="weight")
print("Shortest path from A to D:", path)

# Centrality
centrality = nx.degree_centrality(G)
print("Centrality:", centrality)