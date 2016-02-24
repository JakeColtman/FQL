import unittest
from Parser import Parser

class ParserTests(unittest.TestCase):
    def test_parser_returns_query_if_given_single_query(self):
        parser = Parser()
        output = parser.parse("SELECT 1")
        self.assertTrue(len(output) == 1)

if __name__ == '__main__':
    unittest.main()
