import pickle
import os.path
from QueryGraph.QueryGraph import QueryGraph


class QueryGraphRepo:
    def __init__(self, file_name="", recreate=False):
        self.file_name = file_name
        self.recreate = recreate

    def load(self):
        if os.path.isfile(self.file_name) and not self.recreate:
            with open(self.file_name, "rb") as data_file:
                graph = pickle.load(data_file)
        else:
            graph = QueryGraph()

        return graph

    def save(self, graph: QueryGraph):
        with open(self.file_name, "wb") as data_file:
            pickle.dump(graph, data_file)