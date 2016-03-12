import pickle
import os.path

class Repository:

    def __init__(self, file_name = "", recreate = False):
        self.file_name = file_name
        if os.path.isfile(self.file_name) and not recreate:
            with open(self.file_name, "rb") as data_file:
                self.queries = pickle.load(data_file)
        else:
            self.queries = {}

    def add_query(self, query):
        self.queries[query.name] = query

    def add_queries(self, queries):
        [self.add_query(x) for x in queries]

    def retrieve_query(self, name):
        return self.queries[name]

    def retrieve_query_with_dependencies(self, name):
        output = []
        newDeps = [name]
        while len(newDeps) != 0:
            dependentQueries = [self.retrieve_query(x) for x in newDeps]
            output.extend(dependentQueries)
            newDepsNonFlat = [x.dependencies for x in dependentQueries]
            newDeps = [item for sublist in newDepsNonFlat for item in sublist]
        final_output = []
        for queryName in output[::-1]:
            if queryName not in final_output:
                final_output.append(queryName)
        return final_output


    def save(self):
        with open(self.file_name, "wb") as data_file:
            output = self.queries
            pickle.dump(output, data_file)

    def retrieve_all_queries(self):
        return [self.queries[x] for x in self.queries]



