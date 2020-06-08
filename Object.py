""" this will be the main shape template that all other scene objects will inherit from.
    needs to have: Material, intersect method, hit_info"""

# import abc  # https://docs.python.org/3/library/abc.html
from Material import Material


class Object:  # metaclass=abc.ABCMeta
    def __init__(self, hit_info, color):
        self.material = Material(color)
        self.hit_info = hit_info

    # @abc.abstractmethod
    def intersect(self, ray, hit_info):
        pass


asd = Object((1,2,3),(1,0,0))
print(asd.material.color)
print(asd.hit_info)
