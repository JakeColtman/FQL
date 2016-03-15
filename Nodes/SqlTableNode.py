from typing import List

class SqlTableNode:

    def __init__(self, cte_name, text):
        self.cte_name, self.text = cte_name, text

    def get_columns(self):
        return None

    def get_dependencies(self) -> List['Node']:
        return None

    def get_docstring(self):
        return None

    def set_columns(self):
        return None

    def add_dependency_node(self, node : 'Node'):
        return None

    def set_docstring(self):
        return None

    def get_name(self):
        return None