from Sphere import Sphere
from Ray import Ray


def test_intersect():
    sphere = Sphere(radius=5, center=(15, 0, 0))
    hitting_ray = Ray(origin=(0, 0, 0), direction=(3, 0, 0))
    missing_ray = Ray(origin=(1, 1, 1), direction=(-1, 0, 0))
    assert sphere.intersect(ray=hitting_ray)
    assert sphere.intersect(ray=missing_ray) is False
