import unittest
from Repository import Repository
from DomainModel.Query import Query
from SqlCode import SqlCode

class RepositoryTests(unittest.TestCase):

    def test_repo_stores_query(self):
        testQuery = Query("test_query", "select company from companies")
        repo = Repository()
        repo.add_query(testQuery)
        self.assertTrue(len(repo.retrieve_all_queries()) == 1)
        self.assertTrue(repo.retrieve_query("test_query") is testQuery)

    def test_repo_keeps_dependencies(self):
        testQuery = SqlCode("with companies as (select company_name, company_id) select company_name from companies", "test_query")
        repo = Repository()
        repo.add_queries(testQuery.queries)
        self.assertEqual(len(repo.retrieve_all_queries()), 2)
        self.assertEqual(repo.retrieve_query("companies").name, repo.retrieve_query("test_query").dependencies[0])

    def test_repo_retrieves_dependencies(self):
        testQuery = SqlCode("with companies as (select company_name, company_id) select company_name from companies", "test_query")
        repo = Repository()
        repo.add_queries(testQuery.queries)
        queries = repo.retrieve_query_with_dependencies("test_query")
        self.assertEqual(len(queries), 2)
        self.assertTrue(testQuery.queries[0] in queries)
        self.assertTrue(testQuery.queries[1] in queries)

    def test_repo_retrieves_dependencies_in_order(self):
        testQuery = SqlCode("with companies as (select company_name, company_id) select company_name from companies", "test_query")
        repo = Repository()
        repo.add_queries(testQuery.queries)
        queries = repo.retrieve_query_with_dependencies("test_query")
        self.assertEqual(len(queries), 2)
        self.assertTrue(testQuery.queries[0] == queries[0])
        self.assertTrue(testQuery.queries[1] == queries[1])

if __name__ == '__main__':
    unittest.main()
