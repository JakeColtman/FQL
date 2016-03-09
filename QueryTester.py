from collections import namedtuple
from Connections.Redshift import RedshiftConnection
from QueryGenerator import TestQueryGenerator
Test = namedtuple("QueryTester", ["id", "query", "tableLookup", "outputTable"])

class QueryTester:

    def __init__(self, connection : RedshiftConnection):
        self.connection = connection

    def run_test(self, test : Test, verbose = False):
        query_generator = TestQueryGenerator(test.id, test.tableLookup, test.query)
        query = query_generator.generate()
        results_query = self.connection.run_query(query)

        results_outputtable = self.connection.run_query("select * from {0} where test_id = {1}".format(test.outputTable, str(test.id)))
        formattedOutput = [x[:-1] for x in results_outputtable]
        success = True
        for result in results_query:
            if result not in formattedOutput: success = False
        if verbose:
            return [success, results_query, formattedOutput]
        else:
            return success
