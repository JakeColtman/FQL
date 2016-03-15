from DomainModel.Columns.Column import Column
from DomainModel.Columns.ColumnTypes import ColumnKind, ColumnType

class ColumnFactory:

    def __init__(self):
        pass

    def create_column(self, columnText):
        return Column(columnText, ColumnType.string, ColumnKind.dimension)