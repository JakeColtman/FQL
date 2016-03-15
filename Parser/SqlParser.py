import sqlparse
from Nodes.SqlCTE import SqlCTENode
from Nodes.Node import Node
from DomainModel.Columns.ColumnFactory import ColumnFactory
from typing import List
from Nodes.SqlTableNode import create_table_node

class SqlCodeParser:
    def __init__(self, column_factory: ColumnFactory, text: str, final_query_name):

        self.text, self.query_name = text, final_query_name
        self.column_factory = column_factory
        self.nodes = []
        self.split_into_cte_queries()

        newNodeList = []
        for node in self.nodes:
            newNodeList = self._parse_node_contents(node, newNodeList)

        self.nodes = newNodeList

    def get_node_list(self):
        return self.nodes

    def split_into_cte_queries(self):

        tokens = sqlparse.parse(self.text)[0].tokens
        if not any([x.ttype is sqlparse.tokens.Keyword and "with" in x.value for x in tokens]):
            self.nodes.append(SqlCTENode(self.query_name, self.text))
            return
        ii = 0
        while ii < len(tokens):
            if type(tokens[ii]) == sqlparse.sql.IdentifierList:
                ctes = tokens[ii].get_identifiers()
                for cte in ctes:
                    cte_name = cte.value
                    cte_text = str(cte).replace(cte.value + " as", "").strip()[1:-1]
                    self.queries.append(SqlCTENode(cte_name, cte_text))
                break

            if type(tokens[ii]) == type(tokens[ii]) == sqlparse.sql.Identifier:
                cte_name = tokens[ii].value
                cte_text = str(tokens[ii]).replace(tokens[ii].value + " as", "").strip()[1:-1]
                self.nodes.append(SqlCTENode(cte_name, cte_text))
                break

            if tokens[ii].ttype is sqlparse.tokens.DML:
                raise
            ii += 1

        final_query_text = "".join([str(x) for x in tokens[ii + 1:]])
        self.nodes.append(SqlCTENode(self.query_name, final_query_text))

    def _parse_node_contents(self, node: SqlCTENode, node_list: List[SqlCTENode]):

        state = "start"
        tokens = sqlparse.parse(self.text)[0].tokens
        tokens = [x for x in tokens if not (x.ttype is sqlparse.tokens.Whitespace)]
        for token in tokens:

            if type(token) is sqlparse.sql.Comment:
                node.set_docstring(str(token).replace("/*", "").replace("*/", "").replace("--", "").strip())

            if token.ttype is sqlparse.tokens.DML:
                state = "select"
                continue

            if state == "select" and token.ttype is not sqlparse.tokens.Punctuation:
                if token.value.lower() == "from":
                    state = "from"
                    continue

                if type(token) is sqlparse.sql.IdentifierList:
                    for item in token.get_identifiers():
                        node.add_column(self.column_factory.create_column(item))
                    continue
                if token.ttype is not sqlparse.tokens.Punctuation and token.ttype is not sqlparse.tokens.Whitespace and str(token.value) != "\n":
                    print(str(token))
                    column = self.column_factory.create_column(str(token))
                    node.add_column(column)

            if state == "from":

                if type(token) is sqlparse.sql.Where or token.value.lower() == "group":
                    break

                if type(token) is sqlparse.sql.Identifier:
                    tableName = ""
                    if token.has_alias():
                        tableName = str(token).replace(token.get_name(), "").strip()
                    else:
                        tableName = token.get_name()

                    dependency = [x for x in node_list if x.get_name() == tableName]
                    if len(dependency) == 1:
                        node.add_dependency_node(dependency[0])

        if node.get_dependencies() == []:
            node = create_table_node(node)
        node_list.append(node)
        return node_list