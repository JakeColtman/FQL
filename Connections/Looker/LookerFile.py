from Repository import Repository
from DomainModel.Query import Query
from QueryGenerator import QueryGenerator
from DomainModel.Column import Column

class LookerFile:

    def __init__(self, repo: Repository, file_name: str):
        file_name = file_name.replace("looker_", "")
        self.repo, self.file_name = repo, file_name

        with open(r"Connections/Looker/base_view.txt", "r") as file_open:
            self.base = file_open.read()

        with open(r"Connections/Looker/base_view_field.txt", "r") as file_open:
            self.base_field = file_open.read()

    def export(self, query: Query):
        qg = QueryGenerator(self.repo)
        output_sql_text = qg.generate_query(query.name)

        fields = self.format_fields(query.columns)

        output_text = self.base.format(query.name.replace("looker_", ""), query.columns[0].name, output_sql_text, fields)

        with open(self.file_name, "w") as file_open:
            file_open.write(output_text)

    def format_fields(self, columns):
        output = ""
        for column in columns:
            output += self.format_field(column) + "\n"
        return output

    def format_field(self, column: Column):

        if column.identifier in ["id", "date", "bool", "is"] or column.sql_type == "varchar(255)":
            field_type = "Dimension"
        else:
            field_type = "Measure"

        if column.sql_type == "boolean":
            looker_type = "yesno"
        elif column.sql_type == "varchar(255)":
            looker_type = "string"
        elif column.sql_type == "int":
            looker_type = "number"
        elif column.sql_type == "float":
            looker_type = "number"
        elif column.sql_type == "timestamp":
            looker_type = "date"
        else:
            looker_type = "string"
        return self.base_field.format(column.name, looker_type, field_type)
