from Repository import Repository
from Parser import Parser
from Visualize import visualize, visualize_repository
from QueryGenerator import QueryGenerator
from Connections.Redshift import RedshiftConnection
from RepositoryTester import RepositoryTester
from QueryTester import Test
from SqlCode import split_out_ctes, parse_query_to_detailed, identify_dependencies_in_query_list
from RepositoryTester import setup_repository_test_suite
from RepositoryTester import RepositoryTest


def process(repo, parser, queryList):
    for query in queryList:
        repo.add_queries(parser.parse(query))


#qg = QueryGenerator(repo)
#print(qg.generate_query(["final query"]))
#visualize_repository(repo)

with open("connection_string.txt", "r") as file_open:
    connString = file_open.read()

conn = RedshiftConnection(connString)
#test = Test("select 1", {}, "custom.temp_test")
#tester = RepositoryTester(conn, [test])
#print(tester.run_all_tests())


sqlCode = """ with companies as
                (
                    select company_id, name
                    from companies
                ),
                accounts as
                (
                    select account_id, name
                    from
                    testtable
                )
                select name
                from
                accounts
        """


textQueries = split_out_ctes(sqlCode, "final_query")
print(textQueries)
parsedQueries = [parse_query_to_detailed(x) for x in textQueries]
parsedQueries[-1].dependencies.append("accounts")
print(parsedQueries)
repo = Repository("repo5.pickle")
repo.add_queries(parsedQueries)

rtest = RepositoryTest(conn, repo, "tests", 1)
rtest.find_biggest_testable_node()