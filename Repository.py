import pickle
import os.path

class Repository:

    def __init__(self, file_name = "", recreate = False):

        self.file_name = file_name
        if os.path.isfile(self.file_name) and not recreate:
            with open(self.file_name, "rb") as data_file:
                self.column_type_lookups, self.queries = pickle.load(data_file)
        else:
            self.queries = {}
            self.column_type_lookups = {}

    def add_query(self, query):
        self.queries[query.name] = query
        return True

    def add_queries(self, queries):
        return all([self.add_query(x) for x in queries])

    def retrieve_query(self, name):
        return self.queries[name]

    def save(self):
        with open(self.file_name, "wb") as data_file:
            output = [self.column_type_lookups, self.queries]
            pickle.dump(output, data_file)

    def retrieve_all_queries(self):
        return [self.queries[x] for x in self.queries]

    def update_column_type_lookups(self, number_to_update):
        allQueries = self.retrieve_all_queries()
        allColumns = []
        for query in allQueries:
            allColumns.extend(query.query["columns"])
        print("insert type for each column")
        for column in allColumns:
            if column in self.column_type_lookups:
                continue
            else:
                print(column)
                self.column_type_lookups[column] = input()
                number_to_update -= 1
                if number_to_update < 0: return

