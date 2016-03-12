import unittest
from SqlCode import SqlCode

class SqlCodeTests(unittest.TestCase):

    def test_identifies_single_select_column(self):
        code = SqlCode("select column from testTable", "")
        self.assertEqual(["column"], code.queries[0].column_names())

    def test_identifies_multiple_select_columns(self):
        code = SqlCode("select column, column2 from testTable", "")
        self.assertTrue("column" in code.queries[0].column_names())
        self.assertTrue("column2" in code.queries[0].column_names())

    def test_identifies_multiple_select_columns_with_alias(self):
        code = SqlCode("select column as c1, column2 as c2 from testTable", "")
        self.assertTrue("c1" in code.queries[0].column_names())
        self.assertTrue("c2" in code.queries[0].column_names())

    def test_identifies_table_of_simple_query(self):
        code = SqlCode("select column, column2 from testTable", "")
        self.assertEqual(["testTable"], code.queries[0].table_names())

    def test_identifies_tables_of_simple_join_query(self):
        code = SqlCode("select column, column2 from testTable join testTable2 on testTable.test = testTable2.test", "")
        self.assertTrue("testTable" in code.queries[0].table_names())
        self.assertTrue("testTable2" in code.queries[0].table_names())

    def test_identifier_multiple_ctes_table(self):
        code = SqlCode("with testCTE as (select 1, 2 from platform), testCTE2 as (select 2,4 from thfjf) select 2, 3 from testCTE")
        self.assertEqual("platform", code.queries[0].table_names()[0])

    def test_parse_single_cte(self):
        code = SqlCode("with testCTE as (select 1, 2 from platform) select 2, 3 from testCTE")
        self.assertEqual(code.queries[0].name, "testCTE")
if __name__ == '__main__':
    unittest.main()
