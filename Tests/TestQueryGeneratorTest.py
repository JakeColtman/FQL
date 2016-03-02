import unittest
from QueryGenerator import TestQueryGenerator

class TestQueryGeneratorTest(unittest.TestCase):

    def test_no_ctes_returns_just_the_query(self):
        qg = TestQueryGenerator({}, "select 1")
        test_query = qg.generate()
        self.assertEqual(test_query, "select 1")

    def test_no_ctes_return_query_lower(self):
        qg = TestQueryGenerator({}, "Select 1")
        test_query = qg.generate()
        self.assertEqual(test_query, "select 1")

    def test_handles_single_cte(self):
        ctes = {"test_cte":"test_table"}
        qg = TestQueryGenerator(ctes, "Select 1")
        test_query = qg.generate()

        self.assertEqual(test_query, "with test_cte as ( select * from test_table ) select 1")

    def test_handles_multiple_ctes(self):
        ctes = {"test_cte":"test_table", "test_cte2": "test_table2"}
        qg = TestQueryGenerator(ctes, "Select 1")
        test_query = qg.generate()

        self.assertEqual(test_query, "with test_cte as ( select * from test_table ),test_cte2 as ( select * from test_table2 ) select 1")

if __name__ == '__main__':
    unittest.main()
