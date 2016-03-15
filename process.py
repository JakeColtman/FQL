from Nodes.Node import SqlTableNode
from QueryGraph.QueryGraphFactory import QueryGraphFactory
from Parser.SqlParser import SqlCodeParser
from DomainModel.Columns.ColumnFactory import ColumnFactory

parser = SqlCodeParser(ColumnFactory(), "with accounts as (select account_id from test ) select account_id from accounts", "final_query")
for node in parser.nodes:
    print(node.get_name())
    print(node.get_dependencies())


