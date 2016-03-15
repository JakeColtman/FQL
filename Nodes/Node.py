from abc import ABCMeta, abstractmethod

class Node(metaclass=ABCMeta):

    @abstractmethod
    def get_columns(self):
        return None

    @abstractmethod
    def get_dependencies(self):
        return None

    @abstractmethod
    def get_docstring(self):
        return None

    @abstractmethod
    def set_columns(self):
        return None

    @abstractmethod
    def set_dependencies(self):
        return None

    @abstractmethod
    def set_docstring(self):
        return None