from typing import List
from DomainModel.Columns import Column

class SqlCTENode:

    def __init__(self, name, text):
        self.name, self.text = name, text
        self.dependencies = []
    def get_columns(self):
        return None

    def get_dependencies(self) -> List['Node']:
        return self.dependencies

    def get_docstring(self):
        return None

    def add_column(self, column: Column):
        return None

    def add_dependency_node(self, node : 'Node'):
        self.dependencies.append(node)

    def set_docstring(self):
        return None

    def get_name(self):
        return self.name