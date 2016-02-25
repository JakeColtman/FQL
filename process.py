from Repository import Repository
from Parser import Parser
from Visualize import visualize
from QueryGenerator import QueryGenerator

def process(repo, parser, queryList):
    for query in queryList:
        repo.add_queries(parser.parse(query))

repo = Repository()
bigQuery = """"""
parser = Parser()
output = parser.parse(bigQuery)
repo.add_queries(output)
qg = QueryGenerator(repo)
print(qg.generate_query(["final query"]))