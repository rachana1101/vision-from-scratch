# 12_splats: Gaussian splatting: represent a scene as many soft colored blobs and render them.

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
# α_i(x) = o_i · exp(-½ (x - μ_i)ᵀ Σ_i⁻¹ (x - μ_i))
# C(x) = Σ_i c_i α_i Π_{j<i} (1 - α_j)
# Σ_2D = J W Σ_3D Wᵀ Jᵀ

# Cell 6: Full 3D splatting on your COLMAP scene
# Feed the 11_colmap output to a public 3DGS implementation (for example gsplat or nerfstudio).
# Train, render a few novel views, compare with held-out photos (PSNR).

# Cell 5: Fit 2D splats to the dog (PyTorch)
# Make N 2D Gaussians with learnable mean, covariance, color, opacity.
# Render with your composite function, L1 loss against the dog, optimize with Adam.
# Watch the image appear blob by blob. (pip install torch first.)
def fit_2d_splats(img, N):
    pass

# Cell 4: Color from spherical harmonics (degree 0)
# Splats store color as SH coefficients. Degree 0 = same color from every direction:
#   color = 0.28209 · c0 + 0.5    → c0 = 1 gives 0.782
# Higher degrees let the color change with viewing angle.

# Cell 3: From 3D blob to screen size
# A 3D Gaussian of size σ = 0.1 at depth Z = 10, f = 500:
#   on-screen size ≈ f · σ / Z = 500 × 0.1 / 10 = 5 px
# Full version: Σ_2D = J W Σ_3D Wᵀ Jᵀ (W = camera rotation, J = projection Jacobian, from 06).
def project_cov(Sigma3, R, f, Z):
    pass

# Cell 2: Alpha compositing front to back
# Red splat α = 0.5 in front of a blue splat α = 0.5:
#   color = 0.5 · red + (1 - 0.5) · 0.5 · blue = (0.5, 0, 0.25)
#   light still passing through (transmittance) = 0.5 · 0.5 = 0.25
def composite(colors, alphas):
    pass

# Cell 1: One 2D Gaussian splat by hand
# Center (2, 2), covariance = identity, opacity 0.8.
#   alpha at (2, 2) = 0.8
#   alpha at (3, 2) = 0.8 · exp(-0.5 · 1²) = 0.485
#   alpha at (4, 2) = 0.8 · exp(-0.5 · 2²) = 0.108
# Render it on a 5×5 grid and print it.
def splat_2d(mean, cov, opacity, H, W):
    pass


if __name__ == "__main__":
    pass
