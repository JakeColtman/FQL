import networkx as nx
import matplotlib.pyplot as plt
from Repository import Repository

def visualize(queries):
    G = nx.DiGraph()
    G.add_nodes_from([x.name for x in queries])

    edges = []
    for query in queries:
        edges += [(query.name, x) for x in query.dependencies]
    print(edges)
    G.add_edges_from(edges)
    nx.draw(G, with_labels=True)
    plt.show()

def visualize_repository(repo: Repository):
    G = nx.DiGraph()
    allQueries = [repo.queries[x] for x in repo.queries]
    G.add_nodes_from([x.name for x in allQueries])

    edges = []
    for query in allQueries:
        edges += [(x, query.name) for x in query.dependencies]
    print(edges)
    G.add_edges_from(edges)
    nx.draw(G, with_labels=True)
    plt.show()