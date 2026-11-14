# 10_photometric_stereo: Photometric stereo: same camera, different lights → surface normals.

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
# I_k = ρ (n · l_k) for each light k
# Stack: I = L g, g = ρ n → g = L⁻¹ I (3 lights) or least squares (more lights)
# ρ = |g|, n = g / |g|

# Cell 8: Real data (optional)
# Try the public DiLiGenT dataset (known lights, ground-truth normals) and compare your error.

# Cell 7: Normals → depth (optional)
# Integrate the normal field into a height map (e.g. Frankot-Chellappa via FFT).
# Your sphere should come back as a dome.
def integrate_normals(n):
    pass

# Cell 6: Shadows and highlights
# Pixels in shadow (I ≈ 0) or specular highlights break the Lambert model.
# Drop the darkest and brightest reading per pixel before solving, and compare error.
def robust_normals(images, L):
    pass

# Cell 5: Check against ground truth
# You know the sphere's true normals. Mean angular error should be < 1° without noise.
# Show the normal map as an RGB image: (n + 1) / 2.
def angular_error(n_est, n_true):
    pass

# Cell 4: Synthetic sphere with your ray tracer
# Render a Lambertian sphere from your C++ ray tracer under 4+ known lights, fixed camera.
# Load the images, stack the per-pixel intensities, solve least squares for every pixel at once (np.linalg.lstsq).
def sphere_normals(images, L):
    pass

# Cell 3: A tilted patch
# n = (0.6, 0, 0.8), ρ = 1 → I = [0.8, 1.0, 0.64]
# Solve → g = (0.6, 0, 0.8), ρ = 1. ✓
# Angle between this normal and the flat one: acos(0.8) = 36.87°.

# Cell 2: Three lights, solve for the normal
# Lights as rows: L = [[0, 0, 1], [0.6, 0, 0.8], [0, 0.6, 0.8]]
# Flat patch, ρ = 0.8 → I = [0.8, 0.64, 0.64]
# g = L⁻¹ I = (0, 0, 0.8) → ρ = |g| = 0.8, n = g / |g| = (0, 0, 1). ✓
def solve_normal(L, I):
    pass

# Cell 1: Lambertian shading by hand
# Brightness I = ρ · (n · l)
#   n = (0, 0, 1), l = (0, 0, 1), ρ = 0.8 → I = 0.8
#   same n, l = (0.6, 0, 0.8)          → I = 0.8 × 0.8 = 0.64
# The surface looks dimmer when the light comes in at an angle.
def lambert(n, l, rho):
    pass


if __name__ == "__main__":
    pass
