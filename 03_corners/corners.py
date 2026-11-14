# 03_corners: Corners: places where the image changes in two directions at once (Harris).

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

# Cell 10: Wrap-up, with the formula you've been doing by hand
# M = Σ w(x, y) [[Ix², IxIy], [IxIy, Iy²]]
# R = det(M) - k · trace(M)² = λ1λ2 - k(λ1 + λ2)²
# R > 0 big → corner, R < 0 → edge, |R| small → flat.

# Cell 9: Invariance check
# - Rotate the dog 30° (cv.warpAffine): corners move with the image → rotation invariant.
# - Scale it down 0.5×: some corners vanish, new ones appear → NOT scale invariant.
# That failure is the whole reason for SIFT (04).
def invariance_check():
    pass

# Cell 8: Scale up to cute_dog.jpg and compare
# - Compare with cv.cornerHarris(gray, blockSize=2, ksize=3, k=0.04).
#   Raw R values differ in scale (different window/Sobel scaling), so compare the TOP-N corner locations, not raw numbers.
# - Draw your corners and OpenCV's on the dog. Flat background should have none.
def corners_on_dog():
    pass

# Cell 7: Harris on the full image + non-max suppression
# Vectorized: compute Ix², Iy², IxIy for every pixel, Gaussian-blur each one
# (that's the "sum over a window", with weights), then R per pixel.
# Keep local maxima of R above a threshold (e.g. 1% of max R).
# Run on the corner patch first: the strongest R should sit at the corner of the 2×2 block.
def harris_image(gray, k=0.04):
    pass

# Cell 6: Shi-Tomasi: min eigenvalue
# Score = min(λ1, λ2).  flat 0, edge 0, corner 300.
# Simpler rule, often better corners. cv.goodFeaturesToTrack uses it.
def shi_tomasi(M):
    pass

# Cell 5: Harris response R
# R = det(M) - k · trace(M)², k = 0.04
#   flat:   0 - 0.04 × 0²     = 0
#   edge:   0 - 0.04 × 300²   = -3600     (negative → edge)
#   corner: 90000 - 0.04 × 600² = 75600   (big positive → corner)
# No eigenvalues needed: det and trace are cheap.
def harris_response(M, k=0.04):
    pass

# Cell 4: Eigenvalues tell the story
# Eigenvalues of M = how much the window changes in its two main directions.
#   flat:   λ = 0, 0        → no change anywhere
#   edge:   λ = 300, 0      → change in one direction only
#   corner: λ = 300, 300    → change in both
# Check with np.linalg.eigvalsh.
def eigen_view(M):
    pass

# Cell 3: Structure tensor M by hand (toy numbers)
# For a window, M = sum of [[Ix², Ix·Iy], [Ix·Iy, Iy²]].
# Toy case, edge: 3 pixels with Ix = 10, Iy = 0 → ΣIx² = 300 → M = [[300, 0], [0, 0]]
# Toy case, corner: add 3 pixels with Iy = 10 → M = [[300, 0], [0, 300]]
# Flat: M = [[0, 0], [0, 0]]
def structure_tensor(Ix, Iy):
    pass

# Cell 2: Gradients of each patch
# Use Sobel (from 02) to get Ix and Iy for each patch. Print them.
#   flat:   Ix = 0, Iy = 0 everywhere
#   edge:   Ix ≠ 0 along the boundary, Iy = 0
#   corner: Ix ≠ 0 AND Iy ≠ 0 near the corner
def gradients(patch):
    pass

# Cell 1: Build three tiny patches
# Make three 5×5 float32 patches:
#   flat:   all 10
#   edge:   left half 10, right half 100 (like I from 01)
#   corner: all 10 except the bottom-right 2×2 block = 100
# Before any math, guess: which ones change if you slide a small window up? sideways? both?
def build_patches():
    pass


if __name__ == "__main__":
    pass
