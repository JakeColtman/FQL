from QueryGraph.QueryGraph import QueryGraph
import unittest
from Nodes.SqlCTE import SqlCTENode

class QueryGeneratorTests(unittest.TestCase):
    def test_add_node(self):
        graph = QueryGraph()
        node = SqlCTENode("test", "test")
        graph.add_node(node)
        self.assertEqual(graph.get_node_by_name("test"), node)

    def test_node_list_contains_all_nodes(self):
        graph = QueryGraph()
        node = SqlCTENode("test", "test")
        node1 = SqlCTENode("test1", "test")
        node2 = SqlCTENode("test2", "test")
        node3 = SqlCTENode("test3", "test")
        graph.add_node(node)
        graph.add_node(node1)
        graph.add_node(node2)
        graph.add_node(node3)

        for n in [node, node2, node3, node1]:
            self.assertEquals([n], graph.get_ordered_node_list_from_node(n))

    def test_node_list_contains_all_nodes(self):
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

        self.assertEquals([node3, node2, node1, node], graph.get_ordered_node_list_from_node(node))
        self.assertEquals([node3, node2, node1], graph.get_ordered_node_list_from_node(node1))

    def test_value_replace_updates_text(self):
        oldGraph = QueryGraph()
        oldGraph.add_node(SqlCTENode("test", "Im the text content of the test node"))

        newGraph = QueryGraph()
        newGraph.add_node(SqlCTENode("test", "im the new content"))

        oldGraph.value_replace(newGraph)

        self.assertEqual(oldGraph.get_node_by_name("test").get_text(),"im the new content")

    def test_value_replace_updates_docstring(self):
        oldGraph = QueryGraph()
        node = SqlCTENode("test", "Im the text content of the test node")
        node.set_docstring("im a doc string")
        oldGraph.add_node(node)
        newNode = SqlCTENode("test", "Im the text content of the test node")
        newNode.set_docstring("im a new doc string")
        newGraph = QueryGraph()
        newGraph.add_node(newNode)

        oldGraph.value_replace(newGraph)

        self.assertEqual(oldGraph.get_node_by_name("test").get_docstring(),"im a new doc string")

    def test_value_replace_doesnt_change_structure(self):
        oldGraph = QueryGraph()
        node = SqlCTENode("test", "Im the text content of the test node")
        oldGraph.add_node(node)
        newNode = SqlCTENode("test2", "Im the text content of the test node")
        newGraph = QueryGraph()
        newGraph.add_node(newNode)

        oldGraph.value_replace(newGraph)

        self.assertTrue(node is oldGraph.node_lookup["test"])
        self.assertEqual(len(oldGraph.node_lookup), 1)

