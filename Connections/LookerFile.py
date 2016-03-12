from Repository import Repository
from DomainModel.Query import Query
from QueryGenerator import QueryGenerator
from DomainModel.Column import Column

class LookerFile:

    def __init__(self, repo: Repository, file_name: str):
        self.repo, self.file_name = repo, file_name

        self.base = """
        - view: {0}
              derived_table:
                 sql_trigger_value: SELECT * FROM looker_scratch.pdt_trigger_values where view_name = '{0}'
                 sortkeys: [{1}]
                 sql: |
                    {2}

              fields:
                 {3}
        """

    def export(self, query: Query):
        qg = QueryGenerator(self.repo)
        output_sql_text = qg.generate_query(query.name)

        fields = self.format_fields(query.columns)

        output_text = self.base.format(query.name, query.columns[0].name, query.text, fields)

        with open(self.file_name, "w") as file_open:
            file_open.write(output_text)

    def format_fields(self, columns):
        output = ""
        for column in columns:
            output += self.format_field(column)

        return output

    def format_field(self, column: Column):
        base = """
            - dimension: {0}
              type: string
              sql: ${{TABLE}}.{0}
            """

        return base.format(column.name)