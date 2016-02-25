class Repository:

    def __init__(self):
        self.queries = []

    def add_query(self, query):
        self.queries.append(query)
        return True

    def add_queries(self, queries):
        return all([self.add_query(x) for x in queries])

    def retrieve_query(self, name):
        return []
