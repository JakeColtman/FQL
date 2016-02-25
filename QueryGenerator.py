from Repository import Repository

class QueryGenerator:

    def __init__(self, repository):
        self.repo = repository

    def _get_relevant_queries_from_repo(self, queries):
        output = []
        newDeps = [x.name for x in queries]
        while len(newDeps) != 0:
            depName = newDeps.pop(0)
            if depName in [x.name for x in output]: continue
            dependentQuery = self.repo.retrieve_query(depName)
            output.append(dependentQuery)
            newDeps += dependentQuery.dependencies
        print(output)
        return output

    def generate_query_with(self, query_names):
        return ""

