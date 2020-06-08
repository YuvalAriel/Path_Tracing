from Camera import Camera


def test_gen_rand_ray():
    cam = Camera(6, 6)
    for x in range(0, cam.img_width):
        for y in range(0, cam.img_height):
            ray = cam.gen_rand_ray(x, y)
            # print(ray.origin.x,ray.origin.y,ray.origin.z, ray.direction.x, ray.direction.y,ray.direction.z)
