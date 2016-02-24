import unittest
from Parser import Parser

class ParserTests(unittest.TestCase):
    def test_parser_returns_query_if_given_single_query(self):
        parser = Parser()
        output = parser.parse("SELECT 1")
        self.assertTrue(len(output) == 1)

    def test_parser_splits_queries_on_semicolon(self):
        parser = Parser()
        output = parser.parse("SELECT 1 ; Select 2")
        self.assertTrue(len(output) == 2)
        self.assertEqual(" Select 2", output[-1])

if __name__ == '__main__':
    unittest.main()
