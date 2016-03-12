from Repository import Repository
from DomainModel import Query
from QueryGenerator import QueryGenerator

class SqlFile:

    def __init__(self, repo: Repository, file_name: str):
        self.file_name = file_name
        self.repo = repo

    def export(self, query: Query):
        qg = QueryGenerator(self.repo)
        output_text = qg.generate_query(query.name)
        with open(self.file_name, "w") as file_open:
            file_open.write(output_text)
