from Sphere import Sphere
import numpy as np
from Plane_Disk import Disk
from Plane_Disk import Plane


class Scene:
    """class that holds all objects in the scene as a list"""

    def __init__(self, x, *args):
        self.obj_list = []
        self.obj_list.append(x)
        self.environment_color = np.zeros(3)
        for i in args:
            self.obj_list.append(i)

    def obj_intersect(self, ray, obj):
        if isinstance(obj, Sphere):
            return obj.sphere_intersect(ray)
        elif isinstance(obj, Disk):
            return obj.disk_intersect(ray)
        elif isinstance(obj, Plane):
            return obj.plane_intersect(ray)
        else:
            print("obj not valid")
            return False

    # iterate over all objects in scene and check if intersected. find closest intersection.
    def find_closest_intersection(self, ray):  # needs to return: hit_material, hit_position, norm.
        # optimize: arrange objects so that first obj is at the top left corner (where the rays start).
        # optimize: divide objects into 2|4 according to their location on the x,y axis.
        current_closest = float("infinity")
        for i, obj in enumerate(self.obj_list):
            t = self.obj_intersect(ray, obj)
            if t is not False and t < current_closest:
                current_obj_index, current_closest = i, t
        if current_closest == float("infinity"):
            return None, None, None
        hit_position = ray.origin.vec_add(ray.norm_dir.vec_mul(current_closest * 0.998))  # by 0.998 to prevent casting a ray into sphere
        # TODO handle case of reflective materials. would need to mul bu 1.001 so hit position is inside the obj.
        hit_obj = self.obj_list[current_obj_index]  # TODO handle this exception.
        norm = hit_obj.get_hit_norm(hit_position)  # produce norm on hit_obj.
        print("hit_obj is",hit_obj,)
        return hit_obj.material, hit_position, norm
