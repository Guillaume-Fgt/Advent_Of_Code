import networkx as nx

with open("Day_25_Snowverload/puzzle_input.txt") as f:
    data=f.read().splitlines()

G=nx.Graph()
for line in data:
    node,linked=line.split(":")
    for other in linked.split():
        G.add_edge(node,other)

G.remove_edges_from(nx.minimum_edge_cut(G))
a,b=nx.connected_components(G)
print(len(a)*len(b))
