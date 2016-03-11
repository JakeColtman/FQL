from QueryTester import QueryTester
from QueryTester import Test
from Repository import Repository
from Connections.Redshift import RedshiftConnection

def setup_repository_test_suite(connection: RedshiftConnection, repo: Repository, schema = "tests"):
    queries = repo.retrieve_all_queries()

    dropQuery = "DROP TABLE {0}"
    rawQuery = "CREATE TABLE {0} ({1} test_id int)"
    rawColumn = "{0} varchar(255)"

    for query in queries:

        columns = ""
        print(query.query["columns"])
        for column in query.query["columns"]:
            if column == "\n": continue
            columns += rawColumn.format(column) + ","
        try:
            connection.run_query(dropQuery.format(schema + "." + query.name))
        except:
            pass
        connection.run_query(rawQuery.format(schema + "." + query.name, columns))
        print(rawQuery.format(schema + "." + query.name, columns))

    connection.run_query("CREATE TABLE {0}.test_details (test_id int, description varchar(max))".format(schema))

class RepositoryTester:

    def __init__(self, connection: RedshiftConnection, repo: Repository, create = False):
        self.repo = repo
        self.connection = connection
        if create: setup_repository_test_suite(connection, repo)

    def run_all_tests(self):
        query_tester = QueryTester(self.connection)
        return list(map(query_tester.run_test, self.tests))

class RepositoryTest:

    def __init__(self, conn: RedshiftConnection, repo:Repository, schema: str, test_id: int):
        self.conn, self.repo, self.id, self.schema = conn, repo, test_id, schema

    def _identify_affected_tables(self):
        allTables = self.conn.run_query("""
            SELECT distinct table_name
            FROM information_schema.tables
            where table_schema = '{0}'""".format(self.schema)
        )
        allTables = [x[0] for x in allTables]

        countQueryRaw = """SELECT count(1) from {0}.{1}
                        where
                        test_id = {2}
                        """

        affectedTables = []

        for table in allTables:
            count = self.conn.run_query(countQueryRaw.format(self.schema, table, self.id))[0][0]
            print(count)
            if count > 0:
                affectedTables.append(table)

        return affectedTables

    def is_node_testable(self, node_name, affectedTables):
        dependencies = self.repo.retrieve_query(node_name).dependencies
        if dependencies == []: return [True, []]
        simulatedNodes = [x for x in dependencies if x in affectedTables]
        missingDependencies = [x for x in dependencies if x not in affectedTables]
        if missingDependencies == []: return [True, simulatedNodes]

        for dependency in missingDependencies:
            depTestable, depSimulatedNodes = self.is_node_testable(dependency, affectedTables)
            print(dependency)
            print(depTestable)
            if not depTestable: return [False, []]
            else:
                simulatedNodes.extend(depSimulatedNodes)
                return [True, list(set(simulatedNodes))]

    def find_biggest_testable_node(self):
        affectedTables = self._identify_affected_tables()

        currentBiggest = 0
        test = None

        for table in affectedTables:
            if table != "final_query": continue
            dependencies = self.repo.retrieve_query(table)
            if dependencies == []: continue
            testable, simulatedNodes = self.is_node_testable(table, affectedTables)
            print(testable, simulatedNodes)
            if testable and len(simulatedNodes) > currentBiggest:
                currentBiggest = len(simulatedNodes)
                test = [table, simulatedNodes]

        print(test)

    def generate_simulated_query(self, node, simulated_nodes):
        output_node = ""
        pass



