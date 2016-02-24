class Repository:

    def __init__(self):
        self.queries = []

    def add_query(self, query):
        self.queries.append(query)
        return True
