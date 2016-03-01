import json
import os.path

class Repository:

    def __init__(self, file_name):
        self.file_name = file_name
        if os.path.isfile(self.file_name):
            with open(self.file_name) as data_file:
                self.queries = json.load(data_file)
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
        with open(self.file_name, "w") as data_file:
            json.dump(self.queries, data_file)
