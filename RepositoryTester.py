from QueryTester import QueryTester
from QueryTester import Test
from Repository import Repository
from Connections.Redshift import RedshiftConnection

def setup_repository_test_suite(connection: RedshiftConnection, repo: Repository, schema = "tests"):
    queries = repo.retrieve_all_queries()

    dropQuery = "DROP TABLE {0}"
    rawQuery = "CREATE TABLE {0} ({1})"
    rawColumn = "{0} varchar(255)"

    for query in queries:

        columns = ""
        print(query.query["columns"])
        for column in query.query["columns"]:
            if column == "\n": continue
            columns += rawColumn.format(column) + ","
        columns = columns[:-1]
        connection.run_query(dropQuery.format(schema + "." + query.name))
        connection.run_query(rawQuery.format(schema + "." + query.name, columns))
        print(rawQuery.format(schema + "." + query.name, columns))


class RepositoryTester:

    def __init__(self, connection: RedshiftConnection, tests: list):
        self.tests = tests
        self.connection = connection
    def run_all_tests(self):
        query_tester = QueryTester(self.connection)
        return list(map(query_tester.run_test, self.tests))

