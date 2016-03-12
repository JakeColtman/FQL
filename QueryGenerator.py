from Repository import Repository
from DomainModel.Query import Query

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
        print(final_output)
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
    def __init__(self, repo: Repository, node_name: str, simulated_nodes: list, test_id: int):
        self.repo = repo
        self.node_name = node_name
        self.simulated_nodes = simulated_nodes
        self.test_id = test_id

    def get_dependency_graph(self, query, simulated_nodes):
        output = []
        newDeps = query.dependencies
        while len(newDeps) != 0:
            dependentQueries = [self.repo.retrieve_query(x) for x in newDeps]
            output.extend(dependentQueries)
            newDepsNonFlat = [x.dependencies for x in dependentQueries if x.name not in simulated_nodes]
            newDeps = [item for sublist in newDepsNonFlat for item in sublist]
        final_output = []
        for queryName in output[::-1]:
            if queryName not in final_output:
                final_output.append(queryName)
        return final_output

    def generate(self):

        node = self.repo.retrieve_query(self.node_name)

        if node.dependencies == []:
            return node.query["string"]

        dep_graph = self.get_dependency_graph(node, self.simulated_nodes)
        output = "with "
        for query in dep_graph:
            if query.name in self.simulated_nodes:
                output += "{0} as ( select * from tests.{0} where test_id = {1} ),".format(query.name, str(self.test_id))
            else:
                output += "{0} as ({1}),".format(query.name, query.query["string"])
        output = output[:-1]
        output += " " + node.query["string"]
        return output