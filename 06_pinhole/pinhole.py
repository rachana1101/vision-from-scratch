# 06_pinhole: Pinhole camera: where does a 3D point land in the image? (C++ port with Eigen at the end.)

import os
import time
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

DOG = os.path.join(os.path.dirname(__file__), "..", "resources", "images", "cute_dog.jpg")


def show(title, img):
    """Display with OpenCV (expects BGR or single-channel)."""
    cv.imshow(title, img)
    cv.waitKey(0)
    cv.destroyAllWindows()

# Cell 9: Wrap-up, with the formula you've been doing by hand
# x ~ K [R | t] X
# K = [[fx, 0, cx], [0, fy, cy], [0, 0, 1]]
# Radial distortion: x_d = x (1 + k1 r² + k2 r⁴ + ...)

# Cell 8: C++ port with Eigen
# Port project_KRt to C++ with Eigen::Matrix3d / Vector3d.
# Prove it: (2, 1, 10) → (420, 290), and the cube corners match Python to 1e-9.

# Cell 7: Check with OpenCV + draw a cube
# cv.projectPoints([[2, 1, 10]], rvec=0, tvec=0, K, None) → (420, 290).
# Then project the 8 corners of a cube and draw its edges on a blank image.
# Move the camera and redraw: you've built a tiny renderer.
def draw_cube():
    pass

# Cell 6: Lens distortion
# Radial distortion on a normalized point (x, y) = (0.4, 0.3), k1 = -0.2:
#   r² = 0.16 + 0.09 = 0.25, factor = 1 + k1·r² = 0.95 → (0.38, 0.285)
# Points far from the center move more. Negative k1 = barrel distortion.
def distort(x, y, k1):
    pass

# Cell 5: Vanishing point
# Parallel lines with direction d = (1, 0, 1) all meet at K @ d:
#   K @ [1, 0, 1] = [820, 240, 1] → (820, 240)
# Draw a few parallel 3D lines, project them, extend them: they meet there.
def vanishing_point(K, d):
    pass

# Cell 4: Move the camera
# Shift the camera 1 unit right. In camera coordinates the point is now (1, 1, 10) → (370, 290).
# Write the full P = K [R | t] with R = I, t = [-1, 0, 0].
# Then try a small rotation about Y and predict which way the point slides.
def project_KRt(K, R, t, P):
    pass

# Cell 3: Same thing as a matrix
# K = [[500, 0, 320], [0, 500, 240], [0, 0, 1]]
# K @ [2, 1, 10] = [4200, 2900, 10] → divide by the last number → (420, 290).
# Homogeneous coordinates: the divide by Z happens at the very end.
def project_K(K, P):
    pass

# Cell 2: Move the point farther away
# Same point at Z = 20: x = 370, y = 265.
# Twice as far → half the offset from the center. That's perspective.

# Cell 1: Project one point by hand
# Camera: f = 500 px, image center (cx, cy) = (320, 240). Point (X, Y, Z) = (2, 1, 10).
#   x = f · X / Z + cx = 500 × 2 / 10 + 320 = 420
#   y = f · Y / Z + cy = 500 × 1 / 10 + 240 = 290
def project(P, f, cx, cy):
    pass


if __name__ == "__main__":
    pass
