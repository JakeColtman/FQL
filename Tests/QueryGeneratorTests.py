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
        output = qg._get_relevant_queries_from_repo(["1", "2"])
        self.assertTrue(q1 in output)
        self.assertTrue(q2 in output)

    def test_query_generator_finds_second_level_queries(self):
        q1 = Query("1", "", [])
        q2 = Query("2", "", ["3"])
        q3 = Query("3", "", [])
        repo = Repository()
        repo.add_queries([q1,q2,q3])
        qg = QueryGenerator(repo)
        output = qg._get_relevant_queries_from_repo(["1", "2"])
        self.assertTrue(q1 in output)
        self.assertTrue(q2 in output)
        self.assertTrue(q3 in output)

    def test_query_generator_wont_double_add(self):
        q1 = Query("1", "", ["3"])
        q2 = Query("2", "", ["3"])
        q3 = Query("3", "", [])
        repo = Repository()
        repo.add_queries([q1,q2,q3])
        qg = QueryGenerator(repo)
        output = qg._get_relevant_queries_from_repo(["1", "2"])
        self.assertEqual(len(output) , 3)

    def test_query_generator_returns_in_dependency_order_simple(self):
        q1 = Query("1", "", ["3"])
        q2 = Query("2", "", ["3"])
        q3 = Query("3", "", [])
        repo = Repository("")
        repo.add_queries([q1,q2,q3])
        qg = QueryGenerator(repo)
        output = qg._get_relevant_queries_from_repo(["1", "2"])
        output.reverse()
        for ii, query in enumerate(output):
            for jj, secondQuery in enumerate(output):
                if jj <= ii: continue
                self.assertTrue(query.name not in secondQuery.dependencies)
        print(output)

    def test_qg_returns_the_query_if_no_deps(self):
        q1 = Query("1", "select 1", [])
        repo = Repository("test.json")
        repo.add_query(q1)
        qg = QueryGenerator(repo)
        self.assertEqual("select 1", qg.generate_query(["1"]))

    def test_qg_returns_a_query_with_all_dependencies_in(self):
        q1 = Query("Q1", "select 1", [])
        q2 = Query("Q2", "select 2", [])
        q3 = Query("Q3", "select 3", [])
        repo = Repository("test.json")
        repo.add_queries([q1,q2,q3])
        qg = QueryGenerator(repo)
        output = qg.generate_query(["Q1", "Q2", "Q3"])
        print("here")
        print(output)
        self.assertTrue("select 1" in output)
        self.assertTrue("select 2" in output)
        self.assertTrue("select 3" in output)
        self.assertTrue("Q2" in output)
        self.assertTrue("Q3" in output)

    def test_qg_does_depth_first(self):
        q1 = Query("Q1", "select 1", [])
        q2 = Query("Q2", "select 2", ["Q1"])
        q3 = Query("Q3", "select 3", ["Q2", "Q1"])
        repo = Repository("dummy.json")
        repo.add_queries([q1,q2,q3])
        qg = QueryGenerator(repo)
        output = qg.generate_query(["Q3"])
        print(output)
        self.assertTrue(output.lower().index("q1") < output.lower().index("q2"))

        q1 = Query("Q1", "select 1", [])
        q2 = Query("Q2", "select 2", ["Q1"])
        q3 = Query("Q3", "select 3", ["Q1", "Q2"])
        repo = Repository("dummy.json")
        repo.add_queries([q1,q2,q3])
        qg = QueryGenerator(repo)
        output = qg.generate_query(["Q3"])
        print(output)
        self.assertTrue(output.lower().index("q1") < output.lower().index("q2"))

if __name__ == '__main__':
    unittest.main()
