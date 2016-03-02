from collections import namedtuple
from Connections.Redshift import RedshiftConnection
from QueryGenerator import TestQueryGenerator
Test = namedtuple("QueryTester", ["query", "tableLookup", "outputTable"])

class QueryTester:

    def __init__(self, connection : RedshiftConnection):
        self.connection = connection

    def run_test(self, test : Test, verbose = False):
        query_generator = TestQueryGenerator(test.tableLookup, test.query)
        query = query_generator.generate()
        results_query = self.connection.run_query(query)

        results_outputtable = self.connection.run_query("select * from {0}".format(test.outputTable))
        success = results_query == results_outputtable
        if verbose:
            return [success, results_query, results_outputtable]
        else:
            return success
