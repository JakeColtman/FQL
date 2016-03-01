from Repository import Repository
from Parser import Parser
from Visualize import visualize
from QueryGenerator import QueryGenerator

def process(repo, parser, queryList):
    for query in queryList:
        repo.add_queries(parser.parse(query))

repo = Repository("repo.pickle")
qg = QueryGenerator(repo)
print(qg.generate_query(["final query"]))