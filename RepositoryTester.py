from QueryTester import QueryTester
from QueryTester import Test
from Repository import Repository
from Connections.Redshift import RedshiftConnection

class RepositoryTester:

    def __init__(self, connection: RedshiftConnection, tests: list):
        self.tests = tests
        self.connection = connection
    def run_all_tests(self):
        query_tester = QueryTester(self.connection)
        return list(map(query_tester.run_test, self.tests))

