# 04_sift: SIFT: find blobs at the right scale, give each a direction and a 128-number fingerprint.

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
# Scale space L(x, y, σ) = G(σ) * I
# DoG D = L(kσ) - L(σ) ≈ (k - 1) σ² ∇²G * I
# Keypoint = 3D extremum of D, kept if |D| ≥ 0.03 and Tr(H)² / Det(H) < (r+1)² / r.
# Descriptor = 4×4×8 normalized gradient histograms.

# Cell 8: Compare with OpenCV
# cv.SIFT_create().detectAndCompute on the dog.
# - Count keypoints, draw them with cv.drawKeypoints (DRAW_RICH_KEYPOINTS shows size + angle).
# - Overlay your DoG extrema: most strong ones should line up with OpenCV's.
# Full hand SIFT is long: matching in 05 can use OpenCV's descriptors once yours agree on location.
def compare_with_opencv():
    pass

# Cell 7: Descriptor: 4×4 cells × 8 bins = 128
# Rotate the neighborhood to the keypoint direction, split into 4×4 cells,
# 8-bin gradient histogram per cell → 128 numbers.
# Normalize, clip at 0.2, normalize again (cuts the effect of strong lighting edges):
#   [3, 4] → [0.6, 0.8] → clip → [0.2, 0.2] → [0.707, 0.707]
def descriptor(gray, kp):
    pass

# Cell 6: Orientation histogram
# Around each keypoint: 36 bins of 10° each, every pixel votes its gradient angle,
# weighted by magnitude (× a Gaussian window). Peak bin = keypoint direction.
# Toy: 3 pixels at 40° with magnitude 2, 1 pixel at 200° with magnitude 3 → bin 40-50° wins (6 vs 3).
# This is what makes SIFT rotation invariant.
def orientation(gray, kp):
    pass

# Cell 5: Reject weak and edge-like points
# Contrast: drop |D| < 0.03 (with the image scaled to 0..1).
# Edges: from the 2×2 Hessian H, keep only if trace(H)² / det(H) < (r + 1)² / r, r = 10 → 12.1
#   H = diag(10, 1):  (11)² / 10 = 12.1   → right at the limit
#   H = diag(20, 1):  (21)² / 20 = 22.05  → rejected (edge-like)
def filter_keypoints(kps, dogs):
    pass

# Cell 4: Extrema in the DoG stack
# A keypoint candidate is bigger (or smaller) than all 26 neighbors:
# 8 in its own DoG + 9 above + 9 below.
# Build a 3×3×3 toy cube with one center value 5 and the rest 1..4 → it's a max.
# Change one neighbor to 6 → not a max anymore.
def find_extrema(dogs):
    pass

# Cell 3: Difference of Gaussians (DoG)
# DoG = G(kσ) - G(σ) ≈ scaled Laplacian, and much cheaper.
# SIFT uses σ0 = 1.6, k = 2^(1/3) ≈ 1.26:
#   σ = 1.6, 2.02, 2.54, 3.2, 4.03  (5 blurs → 4 DoGs per octave)
# Then halve the image and repeat (next octave).
def dog_pyramid(gray, octaves=4):
    pass

# Cell 2: Characteristic scale by hand
# Scale-normalized Laplacian response at the blob center, σ² · (-∇²G * f).
# Compute it for σ from 0.5 to 8. It peaks at σ = 3.5 = the blob's half-width.
# So the filter "finds" the blob size by itself. That's scale selection.
def characteristic_scale():
    pass

# Cell 1: Gaussian blur at several scales (1D first)
# 1D blob: 7 ones in a row of zeros.
# Blur it with σ = 1, 2, 3.5, 5. Use cv.getGaussianKernel (σ = 1, size 5 is 0.0545 0.2442 0.4026 0.2442 0.0545).
# Watch the bump spread and flatten as σ grows.
def blur_1d_scales():
    pass


if __name__ == "__main__":
    pass
