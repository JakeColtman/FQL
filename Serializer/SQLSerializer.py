from QueryGraph.QueryGraph import QueryGraph
from Nodes.Node import Node

class SqlSerializer:

    def __init__(self, graph: QueryGraph):

        self.graph = graph

    def serialize_to_node(self, node: Node):

        nodeList = self.graph.get_ordered_node_list_from_node(node)

        if len(nodeList) == 1:
            return nodeList[0].get_text()

        output = "with "
        for item in nodeList[:-1]:
            output += "{0} as ({1}),".format(item.get_name(), item.get_text()) + "\n"
        output = output[:-2]
        output += "\n"
        output += nodeList[-1].text
        return output

    def serialize(self):
        node = self.graph.list_of_nodes_on_which_nothing_depends()[0]
        return self.serialize_to_node(node)