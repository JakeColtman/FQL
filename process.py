from Repository import Repository
from Parser import Parser
from Visualize import visualize

def process(repo, parser, queryList):
    for query in queryList:
        repo.add_queries(parser.parse(query))

repo = Repository()
process(repo, Parser(), ["with test_cte as (SELECT 1),test_cte2 as (SELECT 3 )  Select 2"])
print(repo.queries)

parser = Parser()
output = parser.parse("with test_cte as (SELECT 1),test_cte2 as (SELECT 3 )  Select * from test_cte left join test_cte2")
visualize(output)