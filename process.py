from Nodes.Node import SqlTableNode
from QueryGraph.QueryGraphFactory import QueryGraphFactory
from Parser.SqlParser import SqlCodeParser
from DomainModel.Columns.ColumnFactory import ColumnFactory
from QueryGraph.QueryGraphFactory import QueryGraphFactory
from QueryGraph.QueryGraphVisualizer import QueryGraphVisualizer
from Nodes.SqlCTE import SqlCTENode
from typing import List

node1 = SqlCTENode("1", "1")
node2 = SqlCTENode("2", "1")
node3 = SqlCTENode("3", "1")
node4 = SqlCTENode("4", "1")

node4.add_dependency_node(node3)
node3.add_dependency_node(node2)
node2.add_dependency_node(node1)

oldGraph = QueryGraphFactory().create_graph_from_node_list([node3, node1, node2, node4])

graph = QueryGraphFactory().create_truncated_runnable_graph_from_node(node4, '3')
QueryGraphVisualizer(graph).visualize()