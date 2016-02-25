import networkx as nx
import matplotlib.pyplot as plt

def visualize(queries):
    G=nx.Graph()
    G.add_nodes_from([x.name for x in queries])

    edges = []
    for query in queries:
        edges += [(query.name, x) for x in query.dependencies]
    print(edges)
    G.add_edges_from(edges)
    nx.draw(G, with_labels=True)
    plt.show()