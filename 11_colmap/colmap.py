# 11_colmap: COLMAP: run full structure-from-motion, then read its output and check it by hand.

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

# Cell 7: Wrap-up, with the formula you've been doing by hand
# Bundle adjustment: minimize Σ_images Σ_points || x_ij - π(K, R_i, t_i, X_j) ||²
# over all cameras and points at once. COLMAP = SIFT + matching + RANSAC + triangulation + BA.

# Cell 6: Compare with your 08 two-view result
# Take two of the images and run your 08 pipeline. Align its points to COLMAP's (scale differs!) and compare.
# More views + bundle adjustment = cleaner, denser points.
def compare_two_view():
    pass

# Cell 5: Your mean reprojection error vs COLMAP's
# Loop over all observations, compute the mean error, and compare with COLMAP's reported value.
# That number is what bundle adjustment minimized.
def mean_reprojection_error():
    pass

# Cell 4: Reproject one 3D point yourself
# Toy check first: point (0, 0, 10), R = I, t = (1, 0, 0), f = 500, center (320, 240)
#   camera coords (1, 0, 10) → (370, 240)
# Then take a real 3D point from points3D.txt, project it into an image that sees it (x ~ K (R X + t)),
# compare with the 2D point COLMAP stored. Error should be ~1 px or less.
def reproject(K, R, t, X):
    pass

# Cell 3: Quaternion → rotation by hand
# images.txt stores rotation as a quaternion (qw, qx, qy, qz).
# Example q = (0.7071, 0, 0.7071, 0) = 90° about Y:
#   R = [[0, 0, 1], [0, 1, 0], [-1, 0, 0]]
#   R @ (0, 0, 10) = (10, 0, 0)
# Write quat_to_R and check it gives this matrix.
def quat_to_R(q):
    pass

# Cell 2: Parse cameras.txt
# Read the camera model and parameters into a K matrix (f, cx, cy).
# Compare f with what you got for the same camera in 07.
def read_cameras(path):
    pass

# Cell 1: Shoot and run
# Take 30-60 overlapping photos walking around one object (lots of texture, no shiny surfaces).
# Install COLMAP. Run feature extraction → matching → mapper, export as TXT model
# (cameras.txt, images.txt, points3D.txt) into 11_colmap/data/.


if __name__ == "__main__":
    pass
