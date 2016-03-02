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

if __name__ == '__main__':
    unittest.main()
