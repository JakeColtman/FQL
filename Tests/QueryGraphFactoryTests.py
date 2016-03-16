from QueryGraph.QueryGraph import QueryGraph
from QueryGraph.QueryGraphFactory import QueryGraphFactory
import unittest
from Nodes.SqlCTE import SqlCTENode

class QueryGeneratorTests(unittest.TestCase):
    def test_creates_new_versions_of_nodes(self):
        node = SqlCTENode("test", "TEST")

        factory = QueryGraphFactory()
        query_graph = factory.create_graph_from_node_list([node])
        new_query_graph = factory.create_runnable_graph_from_node(node)

        self.assertFalse(query_graph.get_node_by_name("test") is new_query_graph.get_node_by_name("test"))