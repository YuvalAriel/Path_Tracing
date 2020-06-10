from Ray import Ray
from Sphere import Sphere
from Scene import Scene


def test_find_closest_intersection():
    sphere1 = Sphere(radius=1, center=(10, 0, 0))
    sphere2 = Sphere(radius=1, center=(6, 0, 0))
    sphere3 = Sphere(radius=1, center=(4, 0, 0))
    scene = Scene(sphere1, sphere2, sphere3)
    hitting_ray = Ray(origin=(0, 0, 0), direction=(1, 0, 0))
    missing_ray = Ray(origin=(0, 0, 0), direction=(0, 1, 0))

    hit_obj_material1, hit_positi1, nor1 = scene.find_closest_intersection(missing_ray)
    hit_obj_material2, hit_positi2, nor2 = scene.find_closest_intersection(hitting_ray)
    print("done")
    assert hit_positi1 is None
    assert round(hit_positi2.x) == 3
