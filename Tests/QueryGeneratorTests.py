import unittest
from Repository import Repository
from Query import Query
from QueryGenerator import QueryGenerator

class QueryGeneratorTests(unittest.TestCase):

    def test_query_generator_finds_first_level_queries(self):
        q1 = Query("1", "", [])
        q2 = Query("2", "", [])
        q3 = Query("3", "", [])
        repo = Repository()
        repo.add_queries([q1,q2,q3])
        qg = QueryGenerator(repo)
        output = qg._get_relevant_queries_from_repo([q1,q2])
        self.assertTrue(q1 in output)
        self.assertTrue(q2 in output)

if __name__ == '__main__':
    unittest.main()
