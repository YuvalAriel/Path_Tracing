from Sphere import Sphere
import numpy as np


class Scene:
    """class that holds all objects in the scene as a list"""

    def __init__(self, x, *args):
        self.obj_list = []
        self.obj_list.append(x)
        self.environment_color = np.zeros(3)
        for i in args:
            self.obj_list.append(i)

        # iterate over all objects in scene and check if intersected. find closest intersection.
        # fill in hit_info.
        # return true if intersected.

    def obj_intersect(self, ray, obj):
        if isinstance(obj, Sphere):
            # print("call sphere intersect")
            return obj.sphere_intersect(ray)
        else:
            print("obj not sphere")
            return False

    def find_closest_intersection(self, ray):  # needs to return: hit_material, hit_position, norm.
        # optimize: arrange objects so that first obj is at the top left corner (where the rays start).
        current_closest = float("infinity")
        for i, obj in enumerate(self.obj_list):
            d = self.obj_intersect(ray, obj)
            if d < current_closest and d is not False:
                current_obj_index, current_closest = i, d
        if current_closest == float("infinity"):
            return None, None, None
        hit_position = ray.origin.vec_add(ray.norm_dir.vec_multiplication(current_closest * 0.998))  # by 0.988 to prevent casting a ray into sphere
        hit_obj = self.obj_list[current_obj_index]
        norm = hit_obj.get_hit_norm(hit_position)  # produce norm on hit_obj.
        return hit_obj.material, hit_position, norm
