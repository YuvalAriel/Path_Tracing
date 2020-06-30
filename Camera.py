from Ray import Ray
from Vec3D import Vec3D
import random


class Camera:
    """
    Generate a ray from camera center to the middle of each pixel. with a random addition that ranges uniformly
    within the limits of the size of the pixel.
    # https://www.scratchapixel.com/lessons/3d-basic-rendering/ray-tracing-generating-camera-rays/generating-camera-rays

    Parameters:
        img_width, img_height - resolution, the image width and height.Their product is the amount of pixels.
        cam_center=(0, 0, 0) - camera center and the origin of the rays. at the moment this cannot be changed.
        fov=90  - field of view in angles. extent of the observable world.
            zoom out when larger than 90 and zoom in when smaller.

    """

    def __init__(self, img_width, img_height, cam_center=(0, 0, 0), fov=90):
        self.cam_center = Vec3D(cam_center[0], cam_center[1], cam_center[2])
        self.fov = float(fov)
        self.img_width = int(img_width)
        self.img_height = int(img_height)
        if img_width >= img_height:
            self.img_aspect = float(img_width / img_height)
        else:
            raise ValueError("invalid camera input: width should be larger than height")

    def gen_rand_ray(self, x_pixel, y_pixel):
        # pixel [0,0] located at upper left. right motion is positive for x. down motion is positive for y.
        pixelNDCx = (x_pixel + 0.5) / self.img_width  # added 0.5 to shift to pixel center.
        pixelNDCy = (y_pixel + 0.5) / self.img_height
        # this produces pixels in the range 0-0.999. remap to Screen Space where points left of y axis are x-negative.
        pixelScreenx = 2 * pixelNDCx - 1
        pixelScreeny = 1 - 2 * pixelNDCy
        # now pixels are in the range of -1 to 1. still need to account for aspect ratio:
        pixelScreenx *= self.img_aspect  # now they range from [-aspect, +aspect]

        pixel_size = 2 / self.img_height
        rnd_addition = random.uniform(-pixel_size / 2, pixel_size / 2)

        # By convention: orient the camera along the negative z-axis. image plane is exactly 1 unit away from the origin
        point = Vec3D(pixelScreenx + rnd_addition, pixelScreeny + rnd_addition, -1)

        ray_dir = point.vec_sub(self.cam_center)

        return Ray(origin=self.cam_center, direction=ray_dir.vec_normalize())
