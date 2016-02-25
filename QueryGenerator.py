from Repository import Repository

class QueryGenerator:

    def __init__(self, repository):
        self.repo = repository

    def _get_relevant_queries_from_repo(self, queries):
        output = []
        for query in queries:
            output.append(self.repo.retrieve_query(query.name))
        print(output)
        return output

    def generate_query_with(self, query_names):
        return ""

