from enum import Enum

class ColumnType(Enum):
    int = 1
    float = 2
    date = 3
    percent = 4
    string = 5
    money = 6

class ColumnKind(Enum):
    dimension = 1
    measure = 2