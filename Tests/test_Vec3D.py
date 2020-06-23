from Vec3D import Vec3D


def test_vec_dot():
    ans = vec1.vec_dot(vec2)
    assert ans == -13.9


def test_vec_sub():
    ans = vec1.vec_sub(vec2)
    assert ans.x == 0.5 and ans.y == -1.2 and ans.z == -8


def test_vec_add():
    ans = vec1.vec_add(vec2)
    assert ans.x == 1.5 and ans.y == -2.8 and ans.z == 0


def test_vec_multiplication():
    ans = vec1.vec_mul(-2)
    assert ans.x == -2 and ans.y == 4 and ans.z == 8


def test_vec_normalize():
    ans = vec1.vec_normalize()
    assert round(ans.x, 3) == 0.218 and round(ans.y, 3) == -0.436 and round(ans.z, 3) == -0.873


def test_vec_cross():
    ans = vec1.vec_cross(vec2)
    assert round(ans.x, 3) == -11.2 and round(ans.y, 3) == -6.0 and round(ans.z, 3) == 0.2


vec1 = Vec3D(1, -2, -4)
vec2 = Vec3D(0.5, -0.8, 4)
