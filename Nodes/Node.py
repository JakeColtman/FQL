from abc import ABCMeta, abstractmethod
from Nodes.SqlTableNode import SqlTableNode
from Nodes.LookerView import LookerViewNode
from Nodes.SqlCTE import SqlCTENode
from typing import List

class Node(metaclass=ABCMeta):

    @abstractmethod
    def get_columns(self):
        return None

    def get_text(self):
        return None

    def set_text(self):
        return None

    @abstractmethod
    def get_name(self):
        return None

    @abstractmethod
    def get_dependencies(self) -> List['Node']:
        return None

    @abstractmethod
    def get_docstring(self):
        return None

    @abstractmethod
    def add_column(self):
        return None

    @abstractmethod
    def add_dependency_node(self, node : 'Node'):
        return None

    @abstractmethod
    def set_docstring(self):
        return None

Node.register(SqlTableNode)
Node.register(LookerViewNode)
Node.register(SqlCTENode)