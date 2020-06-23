from Vec3D import Vec3D
from Renderer import hemisphere_sample2


# receives hit_norm and outputs a random direction in that hemisphere.
def test_hemisphere_sample():
    hit_norm = Vec3D(0, 0, 1)
    for _ in range(100):
        dir = hemisphere_sample(hit_norm)
        print("znorm", _, dir.x, dir.y, dir.z)
        assert dir.z > 0
        assert -1 < dir.x < 1
        assert -1 < dir.y < 1

    hit_norm2 = Vec3D(0, 1, 0)
    for _ in range(100):
        dir = hemisphere_sample(hit_norm2)
        print("ynorm", _, dir.x, dir.y, dir.z)
        assert dir.y > 0
        assert -1 < dir.z < 1
        assert -1 < dir.x < 1

    hit_norm3 = Vec3D(1, 0, 0)
    for _ in range(100):
        dir = hemisphere_sample(hit_norm3)
        print("xnorm", _, dir.x, dir.y, dir.z)
        assert dir.x > 0
        assert -1 < dir.y < 1
        assert -1 < dir.z < 1

def test_hemisphere_sample2():
    hit_norm = Vec3D(0, 0, 1)
    for _ in range(100):
        dir = hemisphere_sample2(hit_norm)
        print("znorm", _, dir.x, dir.y, dir.z)
        assert dir.z > 0
        assert -1 < dir.x < 1
        assert -1 < dir.y < 1

    hit_norm2 = Vec3D(0, 1, 0)
    for _ in range(100):
        dir = hemisphere_sample2(hit_norm2)
        print("ynorm", _, dir.x, dir.y, dir.z)
        assert dir.y > 0
        assert -1 < dir.z < 1
        assert -1 < dir.x < 1

    hit_norm3 = Vec3D(1, 0, 0)
    for _ in range(100):
        dir = hemisphere_sample2(hit_norm3)
        print("xnorm", _, dir.x, dir.y, dir.z)
        assert dir.x > 0
        assert -1 < dir.y < 1
        assert -1 < dir.z < 1
