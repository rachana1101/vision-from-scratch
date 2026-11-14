# 09_stereo: Stereo: disparity for every pixel, then depth.

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
# d(x, y) = argmin_d Σ_window |L(x, y) - R(x - d, y)|
# Z = f B / d,  ΔZ ≈ Z² Δd / (f B)

# Cell 7: Point cloud
# cv.reprojectImageTo3D(disparity, Q) → 3D points. Color them from the left image and plot or save a .ply.
def point_cloud(disp, Q, img):
    pass

# Cell 6: Your own rectified pair
# Use the 08 pose (or cv.stereoCalibrate) → cv.stereoRectify → cv.initUndistortRectifyMap → cv.remap.
# After rectification, matching points should share the same row. Draw horizontal lines to check.
def rectify_own_pair():
    pass

# Cell 5: Compare with OpenCV on a real rectified pair
# Download a Middlebury stereo pair (public dataset; it's already rectified and has ground truth).
# Compare your map with cv.StereoBM_create and cv.StereoSGBM_create.
# Error vs ground truth: % of pixels off by more than 1.
def compare_opencv(left, right):
    pass

# Cell 4: Window size trade-off
# Try w = 3, 9, 21.
# Small windows: noisy, but sharp object borders. Big windows: smooth, but borders bleed.
# That trade-off is why SGBM exists.
def window_sweep():
    pass

# Cell 3: Disparity map with loops, then vectorized
# For every pixel, try d = 0..max_d, sum of absolute differences over a window, pick the min.
# Vectorized trick (like 01's my_filter2d): build a cost volume, one shifted image per d, then box-filter each slice.
def block_matching(left, right, max_d, w):
    pass

# Cell 2: Match one pixel by hand (SAD)
# Left row:  10 10 10 10 50 90 10 10 10 10
# Right row: 10 10 50 90 10 10 10 10 10 10   (same row, shifted 2 left)
# Window = 3 pixels around left x = 5 (values 50 90 10). For each disparity d, compare with right x = 5 - d:
#   d = 0: 120   d = 1: 120   d = 2: 0   d = 3: 160
# Smallest cost → d = 2. ✓
def sad_1d(left, right, x, w, max_d):
    pass

# Cell 1: Depth from disparity, table
# f = 500, B = 1:
#   d = 50 → Z = 10    d = 25 → Z = 20    d = 5 → Z = 100
# Depth error per 1 px of disparity error: ΔZ ≈ Z² / (f B)
#   Z = 10 → 0.2     Z = 100 → 20
# Far things are much less accurate.
def depth_table(f, B):
    pass


if __name__ == "__main__":
    pass
