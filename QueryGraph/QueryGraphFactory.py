from QueryGraph.QueryGraph import QueryGraph


class QueryGraphFactory:
    def create_complete_graph_from_node(self, node):
        graph = QueryGraph()
        graph.add_node(node)
        return graph

    def create_quickest_graph_from_node(self, node):
        graph = QueryGraph()
        graph.add_node(node)
