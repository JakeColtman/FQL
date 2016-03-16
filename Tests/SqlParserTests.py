import unittest
from Parser.SqlParser import SqlCodeParser
from DomainModel.Columns.ColumnFactory import ColumnFactory
from Nodes.SqlTableNode import SqlTableNode
from Nodes.SqlCTE import SqlCTENode
class SQLParserTests(unittest.TestCase):

    def test_identifies_single_select_column(self):
        text = "select column from testTable"
        parser = SqlCodeParser(ColumnFactory(), text, "test").get_node_list()

        self.assertEqual(["column"], [x.name for x in parser[0].get_columns()])

    def test_identifies_multiple_select_columns(self):
        text = "select column, column2 from testTable"
        parser = SqlCodeParser(ColumnFactory(), text, "test").get_node_list()
        print([x.name for x in parser[0].get_columns()])
        self.assertTrue("column" in [x.name for x in parser[0].get_columns()])
        self.assertTrue("column2" in [x.name for x in parser[0].get_columns()])

    def test_identifies_multiple_select_columns_with_alias(self):
        text = "select column as c1, column2 as c2 from testTable"
        parser = SqlCodeParser(ColumnFactory(), text, "test").get_node_list()
        self.assertTrue("c1" in [x.name for x in parser[0].get_columns()])
        self.assertTrue("c2" in [x.name for x in parser[0].get_columns()])

    def test_parser_correctly_process_simple_query(self):
        text = "select column from testTable"
        parser = SqlCodeParser(ColumnFactory(), text, "test").get_node_list()
        self.assertEqual(1, len(parser))
        self.assertEqual([], parser[0].get_dependencies())

    def test_parsers_dependency_single_cte(self):
        text = "with testCTE as (select 1, 2 from platform) select 2, 3 from testCTE"
        parser = SqlCodeParser(ColumnFactory(), text, "test").get_node_list()
        self.assertEqual(2, len(parser))
        self.assertEqual([], parser[0].get_dependencies())
        self.assertEqual(1, len(parser[1].get_dependencies()))
        self.assertEqual("testCTE", parser[1].get_dependencies()[0].name)

    def test_parsers_dependency_two_ctes_joined(self):
        text = "with testCTE as (select 1, 2 from platform), testCTE2 as (select 2,4 from thfjf) select 2, 3 from testCTE left join testCTE2 on 1 = 1"
        parser = SqlCodeParser(ColumnFactory(), text, "test").get_node_list()
        self.assertEqual(3, len(parser))
        self.assertEqual([], parser[0].get_dependencies())
        self.assertEqual([], parser[1].get_dependencies())
        self.assertEqual(2, len(parser[2].get_dependencies()))
        self.assertTrue("testCTE" in [x.get_name() for x in parser[2].get_dependencies()])
        self.assertTrue("testCTE2" in [x.get_name() for x in parser[2].get_dependencies()])
        self.assertEqual(type(parser[0]),SqlTableNode )
        self.assertEqual(type(parser[1]),SqlTableNode )
        self.assertEqual(type(parser[2]),SqlCTENode )

if __name__ == '__main__':
    unittest.main()
