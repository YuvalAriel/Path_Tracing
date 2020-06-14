import math
import sys
import numpy as np
import matplotlib.pyplot as plt

from Vec3D import Vec3D
from Scene import Scene
from Sphere import Sphere
from Material import Material
from Ray import Ray
from Camera import Camera
from Renderer import Renderer



red = [1, 0, 0]
green = [0, 1, 0]
blue = [0, 0, 1]
#(noam) consider inlining these. also abrev again :)
greenM = Material(green)
blueM = Material(blue)
blueMm = Material([0.6,0.6,0])
sphere1 = Sphere(center=(-2, -2, -6), material=Material(red))
sphere2 = Sphere(center=(0, 0, -8), material=greenM)
sphere3 = Sphere(center=(6, 6, -10))
sphere4 = Sphere(center=(0, 7, -10), material=blueMm)

scene = Scene(sphere2, sphere1)
# scene = Scene(sphere1)

cam = Camera(150, 150)  # cam_center=(0.5,0.5,0)

renderer = Renderer(scene, cam)
renderer.render()
