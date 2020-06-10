from Ray import Ray
from Vec3D import Vec3D
from math import pi
from math import tan
import random


# By convention, orient the camera along the negative z-axis
# The default position of a camera is the origin of the world, coordinates (0, 0, 0).
# The image plane is exactly 1 unit away from the origin.
# when i'll want to change the camera view point: follow the link below:
# https://www.scratchapixel.com/lessons/3d-basic-rendering/computing-pixel-coordinates-of-3d-point/mathematics-computing-2d-coordinates-of-3d-points
# https://www.scratchapixel.com/lessons/mathematics-physics-for-computer-graphics/lookat-function


class Camera:
    def __init__(self, img_width, img_height, cam_center=(0, 0, 0), fov=90):
        self.cam_center = Vec3D(cam_center[0], cam_center[1], cam_center[2])
        self.fov = float(fov)
        self.img_width = int(img_width)
        self.img_height = int(img_height)
        self.img_aspect = float(img_width / img_height)  # assuming width>height

    # generate a ray from the cam_center to middle of each pixel. need to express the middle of each pixel as 3D point.
    # https://www.scratchapixel.com/lessons/3d-basic-rendering/ray-tracing-generating-camera-rays/generating-camera-rays
    def gen_rand_ray(self, pixelx, pixely):  # add rng parameter later.
        # normalize pixel position to frame dimensions. now in NDC space. (Normalized Device Coordinates).
        # pixel 0,0 is the one located at upper left. right motion is positive for x. down motion is positive for y.
        pixelNDCx = (pixelx + 0.5) / self.img_width  # added 0.5 to shift to pixel center.
        pixelNDCy = (pixely + 0.5) / self.img_height
        # this produces pixels in the range 0-0.999. remap to Screen Space where points left of y axis are x-negative.
        pixelScreenx = 2 * pixelNDCx - 1
        pixelScreeny = 1 - 2 * pixelNDCy
        # now pixels are in the range of -1 to 1. still need to account for aspect ratio:
        pixelCamerax = pixelScreenx * self.img_aspect  # now they range from [-aspect, +aspect]
        pixelCameray = pixelScreeny
        # adjust for fov when the camera is positioned one unit away from the img plane and y ranges from -1 to 1 then:
        # fov = alpha = pi/4  # arctang of(1/1) * 2 =  π pi/4 . fov = field of view = alpha. alpha should be expressed in radians.
        # if alpha = 90 then no zoom. fov>90 then zoom out, fov<90 zoom in. tan(45)=1.
        zoom_effect = tan(self.fov / 2 * pi / 180)
        pixelCamerax *= zoom_effect  # undo comment when fov!=90 . change to round to 1 and not 0.9999
        pixelCameray *= zoom_effect
        # final point in pixel = (pixelcamerax, pixelcameray, -1). add rng to sample several inside each pixel.
        pixel_size = zoom_effect * 2 / self.img_height
        # create a variable whose value ranges from [-pixel_size/2,pixel_size/2] using the rng.
        rnd_addition = random.uniform(-pixel_size / 2, pixel_size / 2)
        # print(random.uniform(-pixel_size / 2, pixel_size / 2))
        point = Vec3D(pixelCamerax + rnd_addition, pixelCameray + rnd_addition, -1)
        ray_dir = point.vec_sub(self.cam_center)

        # print("camera", pixelx, pixely, ray_dir.x, ray_dir.y, ray_dir.z)

        return Ray(origin=self.cam_center, direction=ray_dir.vec_normalize())
