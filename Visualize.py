import networkx as nx
import matplotlib.pyplot as plt
from Repository import Repository
from DomainModel.Query import Query


def visualize(item):
    if type(item) is Query: visualize_query(item)
    if type(item) is Repository: visualize_repository(item)


def visualize_query(query):
    return
    # G = nx.DiGraph()
    # G.add_nodes_from([x.name for x in query])
    #
    # edges = []
    # for query in queries:
    #     edges += [(query.name, x) for x in query.dependencies]
    # print(edges)
    # G.add_edges_from(edges)
    # nx.draw(G, with_labels=True)
    # plt.show()


def visualize_repository(repo: Repository):
    G = nx.DiGraph()
    queries = repo.retrieve_all_queries()
    G.add_nodes_from([x.name for x in queries])

    edges = []
    for query in queries:
        edges += [(x, query.name) for x in query.dependencies]
    print(edges)
    G.add_edges_from(edges)
    nx.draw(G, with_labels=True)
    plt.show()
