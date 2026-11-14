# 05_matching: Matching: pair up descriptors between two images, then find the transform that explains the pairs.

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
# match = argmin_j ||d_i - d_j||, kept if d1 / d2 < 0.75
# x' ~ H x (3×3, 8 unknowns, 4 points), solved by SVD of A h = 0
# RANSAC tries N = log(1 - p) / log(1 - w^s)

# Cell 7: Scale up: dog vs warped dog
# Warp the dog with a known H (rotate + scale + shift). SIFT both, match, ratio test, RANSAC.
# - Your H vs the known H, and vs cv.findHomography(..., cv.RANSAC).
# - cv.drawMatches: inliers in one color, outliers in another.
def match_dog():
    pass

# Cell 6: RANSAC loop
# Each try: pick 4 matches, fit H (your DLT), count points that land within 3 px.
# Keep the H with the most inliers, refit on all its inliers.
# Test on synthetic points: 20 true correspondences + 20 random junk → should recover H.
def ransac_homography(src, dst, thresh=3.0):
    pass

# Cell 5: RANSAC: how many tries?
# If 50% of matches are inliers, the chance that 4 random picks are all inliers = 0.5⁴ = 0.0625.
# Tries needed for 99% confidence: log(0.01) / log(1 - 0.0625) = 71.4 → 72.
# Try inlier rates 0.3, 0.5, 0.8 and print the table. Low inlier rate gets expensive fast.
def ransac_iterations(inlier_ratio, p=0.99, s=4):
    pass

# Cell 4: Homography from 4 points by hand
# A unit square mapped to a 2×-scaled, shifted square:
#   (0,0)→(10,20)  (1,0)→(12,20)  (0,1)→(10,22)  (1,1)→(12,22)
# Expected H = [[2, 0, 10], [0, 2, 20], [0, 0, 1]]
# Build the 8×9 DLT matrix A (2 rows per point), take the SVD, last row of Vᵀ reshaped 3×3, divide by H[2,2].
# Check: cv.getPerspectiveTransform gives the same H.
def homography_dlt(src, dst):
    pass

# Cell 3: Lowe's ratio test
# Compare the best distance d1 to the second best d2. Keep if d1 / d2 < 0.75.
#   d1 = 0.3, d2 = 0.8 → 0.375 → keep (clearly better than the runner-up)
#   d1 = 0.5, d2 = 0.6 → 0.833 → reject (ambiguous, e.g. repeating texture)
def ratio_test(dists, thresh=0.75):
    pass

# Cell 2: Brute-force nearest neighbor
# Make 3 query and 3 train descriptors. Build the 3×3 distance table by broadcasting (no loops).
# Each query's match = argmin of its row. Write the table on paper first.
def brute_force(q, t):
    pass

# Cell 1: Distance between two descriptors
# Tiny 3-number descriptors: a = [1, 0, 2], b = [2, 1, 0]
# L2 distance = sqrt(1² + 1² + 2²) = sqrt(6) = 2.449
# Check with np.linalg.norm(a - b).
def l2(a, b):
    pass


if __name__ == "__main__":
    pass
