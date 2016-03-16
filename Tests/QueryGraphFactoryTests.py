from QueryGraph.QueryGraph import QueryGraph
from QueryGraph.QueryGraphFactory import QueryGraphFactory
import unittest
from Nodes.SqlCTE import SqlCTENode
from Nodes.PlaceholderNode import PlaceholderNode

class QueryGeneratorTests(unittest.TestCase):
    def test_creates_new_versions_of_nodes(self):
        node = SqlCTENode("test", "TEST")

        factory = QueryGraphFactory()
        query_graph = factory.create_graph_from_node_list([node])
        new_query_graph = factory.create_runnable_graph_from_node(node)

        self.assertFalse(query_graph.get_node_by_name("test") is new_query_graph.get_node_by_name("test"))

    def test_truncated_stops_at_trunction(self):

        graph = QueryGraph()

        node = SqlCTENode("test", "test")
        node1 = SqlCTENode("test1", "test")
        node2 = SqlCTENode("test2", "test")
        node3 = SqlCTENode("test3", "test")

        node.add_dependency_node(node1)
        node1.add_dependency_node(node2)
        node2.add_dependency_node(node3)
        graph.add_node(node)
        graph.add_node(node1)
        graph.add_node(node2)
        graph.add_node(node3)

        factory = QueryGraphFactory()
        testGraph = factory.create_truncated_runnable_graph_from_node(node, ["test2"])

        self.assertEqual(type(testGraph.get_node_by_name("test2")), PlaceholderNode)
        print(testGraph.node_lookup)
        self.assertEqual(len(testGraph.node_lookup), 3)

    def test_truncated_placeholder_keeps_dependencies(self):

        graph = QueryGraph()

        node = SqlCTENode("test", "test")
        node1 = SqlCTENode("test1", "test")
        node2 = SqlCTENode("test2", "test")
        node3 = SqlCTENode("test3", "test")

        node.add_dependency_node(node1)
        node1.add_dependency_node(node2)
        node2.add_dependency_node(node3)
        graph.add_node(node)
        graph.add_node(node1)
        graph.add_node(node2)
        graph.add_node(node3)

        factory = QueryGraphFactory()
        testGraph = factory.create_truncated_runnable_graph_from_node(node, ["test2"])

        self.assertEqual(type(testGraph.get_node_by_name("test2")), PlaceholderNode)
        self.assertEqual(testGraph.get_node_by_name("test2").get_dependencies(), node2.get_dependencies())
        self.assertEqual(len(testGraph.node_lookup), 3)