# 07_calibration: Calibration: recover K and distortion from photos of a checkerboard.

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
# Each view: H = K [r1 r2 t] (up to scale)
# r1 ⟂ r2 and |r1| = |r2| give 2 equations per view on K → 3+ views solve it (Zhang's method)
# Then refine everything by minimizing total reprojection error.

# Cell 6: Undistort
# cv.undistort one photo. Straight edges near the image border should get straighter.
# Show before / after side by side.
def undistort_demo(K, dist):
    pass

# Cell 5: Real photos
# Print a checkerboard (9×6 inner corners), tape it flat, take ~15 photos at different angles with one camera
# (don't change zoom). Put them in 07_calibration/data/.
# cv.findChessboardCorners → cv.cornerSubPix → cv.calibrateCamera.
# Aim for RMS < 0.5 px. Print K and the distortion coefficients.
def calibrate_real(folder):
    pass

# Cell 4: Reprojection error by hand
# Observed corner (421, 289), predicted (420, 290):
#   error = sqrt(1² + 1²) = 1.414 px
# RMS over two corners with errors² of 2 and 0: sqrt((2 + 0) / 2) = 1.0 px
def reprojection_error(obs, pred):
    pass

# Cell 3: Calibrate the synthetic views
# cv.calibrateCamera on the 3 synthetic views. It should give back f = 500, center (320, 240),
# distortion ≈ 0, and RMS error ≈ 0 (no noise yet).
# Then add 0.5 px noise to the image points and watch the estimates wobble.
def calibrate_synthetic():
    pass

# Cell 2: Plane → image is a homography
# With Z = 0, the third column of R drops out:
#   x ~ K [r1 r2 t] [X, Y, 1]  → a 3×3 homography per view.
# Fit H for each view with your DLT from 05 and check it maps the grid onto the projected points.
def homography_per_view(obj, img):
    pass

# Cell 1: Synthetic checkerboard with a known camera
# Make a 9×6 grid of 3D points on the plane Z = 0 (square size 1).
# Use the 06 camera (f = 500, center 320, 240). Project the grid from 3 different poses.
# You now have "photos" where you KNOW the right answer.
def synthetic_views():
    pass


if __name__ == "__main__":
    pass
