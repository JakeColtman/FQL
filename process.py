from Connections.Looker.LookerFile import LookerFile
from Connections.SQL.Redshift import RedshiftConnection
from Repository import Repository
from RepositorySearcher import RepositorySearcher
from RepositoryTester import RepositoryTest, RepositoryTester
from SqlCode import SqlCode


def process(repo, parser, queryList):
    for query in queryList:
        repo.add_queries(parser.parse(query))

code = SqlCode("with testCTE as (select 1, 2 from platform), testCTE2 as (select 2,4 from thfjf) select 2, 3 from testCTE")