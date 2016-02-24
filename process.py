def process(repo, parser, queryList):
    for query in queryList:
        repo.add_queries(parser.parse(query))