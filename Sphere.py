import numpy as np
import math

from Vec3D import Vec3D
from Ray import Ray
from Object import Object
from Material import Material


class Sphere(Object):

    def __init__(self, center, radius, hit_info, color):
        super().__init__(hit_info, color)
        self.material = Material(color)
        self.hit_info = hit_info
        self.center = Vec3D(center)
        self.radius = float(radius)

    def intersect(self, ray, hit_info):
        # check 3 cases: 1. ray missed sphere. 2. ray hit sphere at one point. 3. ray hit sphere at two points.
        # record Hit details: location, normal, ..
        # need to solve for d: d^2(ldotl) + 2d(ldot(o-c)) + (o-c)dot(o-c) - r^2 = 0. where:
        # d = distance along ray from starting point. l = direction of ray(a unit vector). o = origin of ray.
        # c = center of sphere. r = radius of sphere.
        l = ray.normalize()
        o = ray.origin
        c = self.center
        r = self.radius
        co = o - c  # the vector from center of sphere to origin of ray. direction doesnt matter because in power 2.
        determinant = (l.dot(co)) ** 2 - (co.dot(co) - r ** 2)
        if determinant < 0:  # ray missed the sphere
            return False
        elif determinant == 0:
            # d = -l.dot(co)
            return False  # for simplicity. not sure a ray hitting the exact edge of a sphere would produce much light.
        else:
            # has two intersection points. need to pick closest one to ray origin.
            determinant = math.sqrt(determinant)
            d1 = -l.dot(co) + determinant
            d2 = -l.dot(co) - determinant
            if abs(d2) > abs(d1): # if d1 = -d2 then -l.dot(co)=0 and that means direction of ray in 90deg to co
                return d1
            else:
                return d2
            #  create record of hit position. include: position3d, normal, inside/outside? norm=-norm?
            #  ray.hit_pos = o + l*d
            #  ray.hit_norm = (ray.hit_pos - c)/(math.sqrt((ray.hit_pos - c).dot((ray.hit_pos - c))))

    def sphere_norm(self,point):
        return point.sub(self.center).normalize()


sphere = Sphere(radius=5, center=(15, 0, 0))
hitting_ray = Ray(origin=(0, 0, 0), direction=(3, 0, 0))
sphere.intersect(ray=hitting_ray)
