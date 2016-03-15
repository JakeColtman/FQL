from QueryGraph.QueryGraph import QueryGraph
from typing import List
from Nodes.Node import Node
from Nodes.PlaceholderNode import PlaceholderNode

class QueryGraphFactory:
    def create_runnable_graph_from_node(self, node):
        graph = QueryGraph()
        graph.add_node(node)
        depList = node.get_dependencies()
        while len(depList) != 0:
            [graph.add_node(x) for x in depList]
            dependentNodes = [x.get_dependencies() for x in depList]
            depList = [item for sublist in dependentNodes for item in sublist]
        return graph

    def create_truncated_runnable_graph_from_node(self, node, stopping_names: List[str]):
        graph = QueryGraph()
        graph.add_node(node)
        depList = node.get_dependencies()
        while len(depList) != 0:
            stoppedList, addList = [x for x in depList if x.get_name() in stopping_names], [x for x in depList if x.get_name() in stopping_names]
            [graph.add_node(x) for x in addList]
            for item in stoppedList:
                graph.add_node(PlaceholderNode(item.get_name(), ""))
            dependentNodes = [x.get_dependencies() for x in depList]
            depList = [item for sublist in dependentNodes for item in sublist]
        return graph

    def extract_connected_graph_of_nodes(self, query_graph: QueryGraph,  node : Node):
        graph = QueryGraph()

        total_included = [node]
        additions = True
        while additions:
            additions = False

            for nodeName in query_graph.node_lookup:
                node_considered = query_graph.node_lookup[nodeName]
                if node_considered in total_included:
                    continue
                if any([node_x in node_considered.get_dependencies() or node_considered in node_x.get_dependencies() for node_x in total_included]):
                    total_included.append(node_considered)
                    additions = True

        [graph.add_node(x) for x in total_included]

        return graph

    def create_graph_from_node_list(self, node_list: List[Node]):
        graph = QueryGraph()
        for node in node_list:
            graph.add_node(node)

        return graph
