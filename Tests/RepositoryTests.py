import unittest
from Repository import Repository
from Query import Query

class RepositoryTests(unittest.TestCase):
    def test_repo_stores_query(self):
        testQuery = Query("Test", "SELECT 1", [])
        repo = Repository()
        repo.add_query(testQuery)
        self.assertTrue(len(repo.queries.keys()) == 1)
        self.assertTrue(repo.retrieve_query("Test") is testQuery)

    def test_repo_keeps_dependencies(self):
        testQuery = Query("Test", "SELECT 1", ["TestDEP"])
        repo = Repository()
        repo.add_query(testQuery)
        self.assertTrue(len(repo.queries.keys()) == 1)
        self.assertTrue(repo.retrieve_query("Test").dependencies[0] == "TestDEP")


if __name__ == '__main__':
    unittest.main()
