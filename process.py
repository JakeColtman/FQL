from Connections.Looker.LookerFile import LookerFile
from Connections.SQL.Redshift import RedshiftConnection
from Repository import Repository
from RepositorySearcher import RepositorySearcher
from SqlCode import SqlCode


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
                    -- description
                    select company_id, name
                    from companies
                ),
                accounts as
                (
                    /* Im the accounts */
                    select account_id, name
                    from
                    testtable
                )
                select name
                from
                accounts
        """
code = SqlCode(sqlCode)
repo = Repository("repo6.pickle")
file = LookerFile(repo, "testExport.sql")
repo.add_queries(code.queries)
searcher = RepositorySearcher(repo)
found = searcher.get_best_guesses("final_query")
print(repo.retrieve_query_with_dependencies(found[0].name))
file.export(found[0])