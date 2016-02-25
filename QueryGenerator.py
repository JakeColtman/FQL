from Repository import Repository
from Query import Query

class QueryGenerator:

    def __init__(self, repository):
        self.repo = repository

    def _get_relevant_queries_from_repo(self, query_names):
        output = []
        newDeps = query_names
        while len(newDeps) != 0:
            depName = newDeps.pop(0)
            if depName in [x.name for x in output]: continue
            dependentQuery = self.repo.retrieve_query(depName)
            output.append(dependentQuery)
            newDeps += dependentQuery.dependencies
        print(output)
        return output

    def generate_query(self, query_names):
        order_output = self._get_relevant_queries_from_repo(query_names)
        if len(order_output) == 1: return order_output[0].query
