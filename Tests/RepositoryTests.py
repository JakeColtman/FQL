import unittest
from Repository import Repository
from random import randint

class RepositoryTests(unittest.TestCase):
    def test_repo_stores_query(self):
        testint = randint(0,10)
        repo = Repository()
        repo.add_query(testint)
        self.assertTrue(len(repo.queries) == 1)
        self.assertTrue(repo.queries[-1] == testint)


if __name__ == '__main__':
    unittest.main()
