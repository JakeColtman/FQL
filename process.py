from Nodes.Node import SqlTableNode
from QueryGraph.QueryGraphFactory import QueryGraphFactory
from Parser.SqlParser import SqlCodeParser
from DomainModel.Columns.ColumnFactory import ColumnFactory
from QueryGraph.QueryGraphFactory import QueryGraphFactory
from QueryGraph.QueryGraphVisualizer import QueryGraphVisualizer
parser = SqlCodeParser(ColumnFactory(), "with accounts as (select account_id from test ) select account_id from accounts", "final_query")

QueryGraphVisualizer(QueryGraphFactory().create_complete_graph_from_node(parser.nodes[-1])).visualize()

