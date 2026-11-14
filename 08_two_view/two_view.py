# 08_two_view: Two-view geometry: two cameras, one point — epipolar lines and triangulation. (C++ port with Eigen.)

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

# Cell 8: Wrap-up, with the formula you've been doing by hand
# x2ᵀ E x1 = 0, E = [t]× R
# F = K2⁻ᵀ E K1⁻¹ (pixel version)
# Epipolar line l2 = E x1. Side-by-side cameras: Z = f B / d.

# Cell 7: C++ port with Eigen
# Port the 8-point algorithm and triangulation (Eigen::JacobiSVD).
# Prove it on the synthetic set: same E (up to sign/scale) and same 3D points as Python.

# Cell 6: Real pair
# Take two photos of a textured scene with the camera calibrated in 07.
# SIFT + ratio test (05) → cv.findEssentialMat with RANSAC → recoverPose → triangulate.
# Draw epipolar lines on both images; matching points must sit on them.
# Plot the sparse 3D points with matplotlib.
def real_pair():
    pass

# Cell 5: 8-point algorithm on synthetic data
# Make 20 random 3D points, project into both cameras (rotate camera 2 a bit too).
# Build the 8-point system, SVD, enforce rank 2. Compare with cv.findEssentialMat,
# and get R, t back with cv.recoverPose. t comes back only up to scale.
def eight_point(x1s, x2s):
    pass

# Cell 4: Triangulate by hand
# Depth from disparity: Z = f · B / d = 500 × 1 / 50 = 10. ✓
# Then X = (x - cx) · Z / f = 100 × 10 / 500 = 2, Y = 50 × 10 / 500 = 1 → (2, 1, 10) back.
# Check with cv.triangulatePoints.
def triangulate(P1, P2, x1, x2):
    pass

# Cell 3: Epipolar line
# E @ x1 = (0, 1, -0.1) → the line 0·x + 1·y - 0.1 = 0 → y = 0.1.
# So the match in image 2 must lie on the same (normalized) row. Side-by-side cameras → horizontal epipolar lines.
def epipolar_line(E, x1):
    pass

# Cell 2: Essential matrix by hand
# Normalized coords (divide out K): x1 = (0.2, 0.1, 1), x2 = (0.1, 0.1, 1).
# Camera 2 = camera 1 moved +1 in x, so t = (-1, 0, 0), R = I, and E = [t]× R:
#   E = [[0, 0, 0], [0, 0, 1], [0, -1, 0]]
# Check the epipolar constraint: x2ᵀ E x1 = 0.
def essential_by_hand():
    pass

# Cell 1: Two cameras by hand
# Both cameras: f = 500, center (320, 240). Camera 2 is 1 unit to the right (baseline B = 1).
# Point (2, 1, 10):
#   camera 1 sees (2, 1, 10) → (420, 290)
#   camera 2 sees (1, 1, 10) → (370, 290)
# Same row, x shifted by 50 px. That shift is the disparity.
def two_cameras():
    pass


if __name__ == "__main__":
    pass
