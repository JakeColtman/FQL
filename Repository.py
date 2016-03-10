import pickle
import os.path

class Repository:

    def __init__(self, file_name = ""):
        self.file_name = file_name
        if os.path.isfile(self.file_name):
            with open(self.file_name, "rb") as data_file:
                self.queries = pickle.load(data_file)
        else:
            self.queries = {}

    def add_query(self, query):
        self.queries[query.name] = query
        return True

    def add_queries(self, queries):
        return all([self.add_query(x) for x in queries])

    def retrieve_query(self, name):
        return self.queries[name]

    def save(self):
        with open(self.file_name, "wb") as data_file:
            pickle.dump(self.queries, data_file)

    def retrieve_all_queries(self):
        return [self.queries[x] for x in self.queries]
