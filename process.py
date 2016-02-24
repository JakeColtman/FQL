from Repository import Repository
from Parser import Parser

def process(repo, parser, queryList):
    for query in queryList:
        repo.add_queries(parser.parse(query))

repo = Repository()
process(repo, Parser(), ["with test_cte as (SELECT 1),test_cte2 as (SELECT 3 )  Select 2"])
print(repo.queries)
