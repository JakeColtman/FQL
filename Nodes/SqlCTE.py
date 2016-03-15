from typing import List
from DomainModel.Columns import Column

class SqlCTENode:

    def __init__(self, name, text):
        self.name, self.text = name, text
        self.dependencies = []
        self.columns = []
        self.doc_string = ""

    def get_columns(self):
        return self.columns

    def get_dependencies(self) -> List['Node']:
        return self.dependencies

    def get_docstring(self):
        return None

    def add_column(self, column: Column):
        self.columns.append(column)

    def add_dependency_node(self, node : 'Node'):
        self.dependencies.append(node)

    def set_docstring(self, doc_string: str):
        self.doc_string = doc_string

    def get_name(self):
        return self.name

    def get_text(self):
        return self.text

    def set_text(self, text: str):
        self.text = text