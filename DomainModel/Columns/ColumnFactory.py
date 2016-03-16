from DomainModel.Columns.Column import Column
from DomainModel.Columns.ColumnTypes import ColumnKind, ColumnType
import sqlparse

class ColumnFactory:

    def __init__(self):
        pass

    def create_column(self, column_text):
        if type(column_text) == sqlparse.sql.Identifier and column_text.has_alias():
            return Column(column_text.get_alias(), ColumnType.string, ColumnKind.dimension)
        elif type(column_text) == sqlparse.sql.Identifier:
            return Column(column_text.get_name(), ColumnType.string, ColumnKind.dimension)
        else:
            print(column_text)
            return Column(str(column_text), ColumnType.string, ColumnKind.dimension)
