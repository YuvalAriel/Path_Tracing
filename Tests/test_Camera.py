from Camera import Camera


# (noam) This is not a test. Consider asserting. If random is an issue consider injecting the variance,
# and reduce it to zero for the test
def test_gen_rand_ray():
    cam = Camera(10, 10)
    for x in range(0, cam.img_width):
        for y in range(0, cam.img_height):
            ray = cam.gen_rand_ray(x, y)
            print(ray.direction.x, ray.direction.y, ray.direction.z)
