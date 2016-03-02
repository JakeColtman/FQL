from collections import namedtuple

Test = namedtuple("QueryTester", ["queryName", "tableLookup", "outputTable"])

class Tester:

    def __init__(self, connection, query_generator):
        self.connection = connection
        self.query_generator = query_generator

    def run_test(self, test : Test, verbose = True):
        return False
