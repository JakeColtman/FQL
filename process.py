from Nodes.Node import SqlTableNode
from QueryGraph.QueryGraphFactory import QueryGraphFactory

graph_factory = QueryGraphFactory()

node = SqlTableNode()



print(graph_factory.create_complete_graph_from_node(node).node_lookup)

