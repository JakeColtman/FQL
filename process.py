from Repository import Repository
from Parser import Parser
from Visualize import visualize, visualize_repository
from QueryGenerator import QueryGenerator
from Connections.Redshift import RedshiftConnection

def process(repo, parser, queryList):
    for query in queryList:
        repo.add_queries(parser.parse(query))

#repo = Repository("repo.pickle")
#qg = QueryGenerator(repo)
#print(qg.generate_query(["final query"]))
#visualize_repository(repo)

with open("connection_string.txt", "r") as file_open:
    connString = file_open.read()

conn = RedshiftConnection(connString)
print(conn.run_query("select 1"))
