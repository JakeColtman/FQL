import unittest
from SqlCode import parse_query_to_detailed
from Query import Query

class DetailedParser(unittest.TestCase):
    def test_identifies_single_select_column(self):
        query = Query("test", "select column from testTable", [])
        details = parse_query_to_detailed(query).query
        self.assertEqual(["column"], details["columns"])

    def test_identifies_multiple_select_columns(self):
        query = Query("test", "select column, column2 from testTable", [])
        details = parse_query_to_detailed(query).query
        self.assertTrue("column" in details["columns"])
        self.assertTrue("column2" in details["columns"])

    def test_identifies_multiple_select_columns_with_alias(self):
        query = Query("test", "select column as c1, column2 as c2 from testTable", [])
        details = parse_query_to_detailed(query).query
        self.assertTrue("c1" in details["columns"])
        self.assertTrue("c2" in details["columns"])

    def test_identifies_table_of_simple_query(self):
        query = Query("test", "select column, column2 from testTable", [])
        details = parse_query_to_detailed(query).query
        self.assertEqual(["testTable"], details["tables"])

    def test_identifies_simple_where(self):
        query = Query("test", "select column, column2 from testTable where test", [])
        details = parse_query_to_detailed(query).query
        self.assertEqual("test", details["where"])

    def test_identifies_complex_where(self):
        query = Query("test", "select column, column2 from testTable where test = 1 or test = 2", [])
        details = parse_query_to_detailed(query).query
        self.assertEqual("test = 1 or test = 2", details["where"])

    def test_identifies_tables_of_simple_join_query(self):
        query = Query("test", "select column, column2 from testTable join testTable2 on testTable.test = testTable2.test", [])
        details = parse_query_to_detailed(query).query
        self.assertTrue("testTable" in details["tables"])
        self.assertTrue("testTable2" in details["tables"])

if __name__ == '__main__':
    unittest.main()
