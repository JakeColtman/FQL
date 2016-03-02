from Repository import Repository
from Query import Query

class QueryGenerator:

    def __init__(self, repository):
        self.repo = repository

    def _get_relevant_queries_from_repo(self, query_names):
        output = []
        newDeps = query_names
        while len(newDeps) != 0:
            dependentQueries = [self.repo.retrieve_query(x) for x in newDeps]
            output.extend(dependentQueries)
            newDepsNonFlat = [x.dependencies for x in dependentQueries]
            newDeps = [item for sublist in newDepsNonFlat for item in sublist]
        final_output = []
        for queryName in output[::-1]:
            if queryName not in final_output:
                final_output.append(queryName)
        return final_output

    def generate_query(self, query_names):
        order_output = self._get_relevant_queries_from_repo(query_names)
        if len(order_output) == 1: return order_output[0].query
        #order_output = list(reversed(order_output))
        output = "with "
        for item in order_output[:-1]:
            output += "{0} as ({1}),".format(item.name, item.query)
        output = output[:-1]
        output += order_output[-1].query
        return output

class TestQueryGenerator:
    def __init__(self, cte_lookup: dict, final_query: str):
        self.cte_lookup = cte_lookup
        self.final_query = final_query.lower()

    def generate(self):
        if self.cte_lookup == {}: return self.final_query

        output = "with "
        for cte in self.cte_lookup:
            output += "{0} as ( select * from {1} ),".format(cte.lower(), self.cte_lookup[cte].lower())
        output = output[:-1]
        output += " " + self.final_query
        print( output)
        return output