""" this will be the main shape template that all other scene objects will inherit from.
    needs to have: Material, intersect method, hit_info"""

# import abc  # https://docs.python.org/3/library/abc.html
from Material import Material


class Object:  # metaclass=abc.ABCMeta
    def __init__(self, color):
        self.material = Material(color)

    # @abc.abstractmethod
    def intersect(self, ray):
        pass

