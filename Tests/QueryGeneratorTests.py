import unittest
from Repository import Repository
from DomainModel.Query import Query
from QueryGenerator import QueryGenerator
from SqlCode import SqlCode

class QueryGeneratorTests(unittest.TestCase):

    def test_constructs_single_query_no_deps(self):
        code = SqlCode("select company_name, company_id from companies", "companies")
        repo = Repository()
        repo.add_queries(code.queries)
        qg = QueryGenerator(repo)
        output = qg.generate_query("companies")
        self.assertEqual(output.lower(), "select company_name, company_id from companies")

    def test_contructs_query_with_single_cte(self):
        code = SqlCode("with companies as (select company_name, company_id) select company_name from companies", "company_names")
        repo = Repository()
        repo.add_queries(code.queries)
        qg = QueryGenerator(repo)
        output = qg.generate_query("company_names")
        self.assertEqual(output.lower(), "with companies as (select company_name, company_id) select company_name from companies")

    def test_contructs_cte_with_single_cte(self):
        code = SqlCode("with companies as (select company_name, company_id) select company_name from companies", "company_names")
        repo = Repository()
        repo.add_queries(code.queries)
        qg = QueryGenerator(repo)
        output = qg.generate_query("companies")
        self.assertEqual(output.lower(), "select company_name, company_id")

if __name__ == '__main__':
    unittest.main()
