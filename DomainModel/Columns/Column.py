from DomainModel.Columns.ColumnTypes import ColumnType, ColumnKind
import sqlparse

class Column:
    def __init__(self, name: str, c_type: ColumnType, c_kind: ColumnKind):
        self.name, self.c_type, self.c_kind = name, c_type, c_kind

