import os
import time
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

ROOT = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(ROOT, "..", "resources", "images", "cute_dog.jpg")


def load(path):
    image = cv.imread(path)
    if image is None:
        raise FileNotFoundError(f"Image not found at path: {path}")
    # print(f"Image shape: {image.shape}")      # (rows=H, cols=W, channels)
    # print(f"Image data type: {image.dtype}")  # uint8: 0..255
    # show("Loaded Image", image)
    return image


def show(title, img):
    """Display with OpenCV (expects BGR or single-channel)."""
    cv.imshow(title, img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def gray(image):
    gray_image = np.zeros(image.shape[:2], dtype=np.uint8)
    rows, cols = image.shape[:2]
    for i in range(rows):
        for j in range(cols):
            gray = 0.2989 * image[i, j][2] + 0.5870 * image[i, j][1] + 0.1140 * image[i, j][0]
            gray_image[i, j] = round(gray)
    return gray_image


# Cell 10: Wrap-up, with the formula you've been doing by hand
# Everything in Cells 2 to 8 was this one line (correlation):
#     g(y, x) = sum over i, j of  h(i, j) * f(y+i, x+j)
# Convolution is the same with y-i, x-j. That's the flip you saw in Cell 5.
# Kernels you used:
#   Box:        h = 1/9 everywhere
#   Gaussian:   h is proportional to exp(-(i² + j²) / 2σ²)
#   Separable:  h(i, j) = h1(i) * h1(j)
# The median filter doesn't fit this formula. That's what "non-linear" means.
# After this: port my_filter2d to C++ with reflect-101 padding.
# Prove it on the same I: every row should print 10 10 40 70 100.

# Cell 9: Median filter (non-linear)
# By hand, one "salt" pixel in a flat patch:
# 10  10  10
# 10 255  10
# 10  10  10
# Mean   = (8×10 + 255) / 9 = 335 / 9 = 37.2   (the outlier leaks in)
# Median = sorted: eight 10s, one 255, so the middle value is 10   (the outlier is gone)
# Then add salt-and-pepper noise to ~2% of the dog's pixels (fix the RNG seed).
# Compare cv.GaussianBlur vs cv.medianBlur(..., 3): the Gaussian smears specks, the median deletes them.
# Also: median-blur the impulse image from Cell 5. The single bright pixel disappears completely,
# because a median has no kernel, so it has no impulse response.
def median_demo(I):
    pass

# Cell 8: Scale up to cute_dog.jpg
# Write my_filter2d(img, kernel) with NO per-pixel loop:
#   - pad the image once
#   - loop over the kernel's offsets only (9 iterations for 3×3)
#   - each iteration adds weight × shifted_slice (slices are views, from 00)
# Checks:
#   - grayscale float32: max |mine - cv.GaussianBlur| should be ~1e-5
#   - the flat background should stay ≈ 221 (kernel sums to 1 → flat regions unchanged)
#   - time it vs a naive per-pixel loop (like the ~200× in 00)
#   - show original vs 15×15 box vs 15×15 Gaussian
def my_filter2d(img, kernel):
    pass

# Cell 7: Separability
# Blur the rows with [1, 2, 1] / 4, then the columns with the same kernel.
# Compare with the 2D 3×3 kernel: same numbers, up to float noise.
# Cost per pixel: 3×3 → 9 multiplies in 2D vs 3 + 3 = 6 separated.
#                 15×15 → 225 vs 30. Print these counts.
def separable_blur(I):
    pass

# Cell 6: Gaussian blur by hand
# 3-tap Gaussian (σ = 0 in OpenCV): [0.25, 0.5, 0.25] = [1, 2, 1] / 4. The middle pixel gets the most weight.
# Along the step row, with reflect-101 padding:
#   column 2: 0.25×10 + 0.5×10  + 0.25×100 = 32.5
#   column 3: 0.25×10 + 0.5×100 + 0.25×100 = 77.5
#   box:      10  10  40    70    100
#   Gaussian: 10  10  32.5  77.5  100   <- steeper ramp: smooths but keeps the edge sharper
# The 2D kernel is np.outer of the 1D one: [[1,2,1],[2,4,2],[1,2,1]] / 16. Check it sums to 1.
# Check against cv.GaussianBlur on a float32 copy of I (uint8 would round 32.5).
def gaussian_by_hand(I, mode='reflect'):
    I = np.array(I).astype(np.float32)
    padded = np.zeros((I.shape[0]+2, I.shape[1]+2), dtype=np.float32)
    kernel = np.array([[1, 2, 1],
                        [2, 4, 2],
                        [1, 2, 1]], dtype=np.float32)
    for i in range(0, I.shape[0]):
        for j in range(0, I.shape[1]):                        
            padded[i+1, j+1] = I[i, j]

    if mode == 'reflect':
        padded[:, 0] = padded[:, 2]
        padded[:, -1] = padded[:, -3]   
        padded[0, :] = padded[2, :]
        padded[-1, :] = padded[-3, :]
    print("Padded image:\n", padded)            

    blurred = np.zeros((padded.shape[0]-2, padded.shape[1]-2), dtype=np.float32)
    for i in range(1, padded.shape[0]-1):
        for j in range(1, padded.shape[1]-1):            
            neighborhood = padded[i-1:i+2, j-1:j+2]      
            blurred[i-1, j-1] = np.sum(neighborhood * kernel) / 16
        
    return blurred

# Cell 5: Impulse response, and correlation vs convolution
# New 5×5 image: all zeros, a single 1 at the center (2, 2).
# Lopsided kernel so you can see the flip:
# k = 1 2 3
#     4 5 6
#     7 8 9
# Predict first:
#   cv.filter2D (correlation)          → 3×3 block around center is FLIPPED: 9 8 7 / 6 5 4 / 3 2 1
#   scipy.signal.convolve2d (convolution) → block comes out AS k:            1 2 3 / 4 5 6 / 7 8 9
# Lesson: blurring a single bright pixel prints the kernel itself.
# Box and Gaussian look the same flipped, so this only matters later (Sobel in 02).
def impulse_response(IR):
    IR = np.array(IR).astype(np.float32)
    kernel = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]], dtype=np.float32)
    flipped_kernel = np.flip(kernel)
    conv_output = np.zeros((IR.shape[0]-2, IR.shape[1]-2), dtype=np.float32)
    correlation_output = np.zeros((IR.shape[0]-2, IR.shape[1]-2), dtype=np.float32)
    
    for i in range(1, IR.shape[0]-1):
        for j in range(1, IR.shape[1]-1):
            neighborhood = IR[i-1:i+2, j-1:j+2]
            correlation_value = np.sum(neighborhood * kernel)
            convolution_value = np.sum(neighborhood * flipped_kernel)
            conv_output[i-1, j-1] = convolution_value
            correlation_output[i-1, j-1] = correlation_value
         
    print("Correlation matches OpenCV:", np.allclose(correlation_output, cv.filter2D(IR, -1, kernel)[1:-1, 1:-1]))
    print("Convolution matches scipy:", np.allclose(conv_output, convolve2d(IR, kernel, mode='valid')))            
    return conv_output        

# Cell 4: Borders (padding)
# Pad I by 1 on each side, run the same loop, and get a full 5×5 output.
# Predict each mode before running:
#   Zero padding:  corner (0, 0) = 4×10 / 9 = 4.44   corner (0, 4) = 4×100 / 9 = 44.4   (fake dark vignette)
#   Reflect-101:   row 10 10 10 100 100 pads to [10] 10 10 10 100 100 [100]
#                  (mirror one step inside the edge; the edge pixel is not repeated)
#                  every output row: 10  10  40  70  100
# Check: cv.blur(I, (3, 3)) should match your reflect-101 version exactly.
# Gotcha: np.pad(mode='reflect') == OpenCV BORDER_REFLECT_101.
#         np.pad(mode='symmetric') == OpenCV BORDER_REFLECT (repeats the edge). Print one padded row to confirm.
def pad_and_blur(I, mode):
    I = np.array(I).astype(np.float32)
    padded = np.zeros((I.shape[0]+2, I.shape[1]+2), dtype=np.float32)

    for i in range(1, I.shape[0]):
        for j in range(1, I.shape[1]):                        
            padded[i+1, j+1] = I[i, j]
            
    
    if mode == 'reflect':
        padded[:, 0] = padded[:, 2]
        padded[:, -1] = padded[:, -3]   
        padded[0, :] = padded[2, :]
        padded[-1, :] = padded[-3, :]
        
    return box_blur_loop(padded)

# Cell 3: Box-blur every interior pixel with a loop
# Loop only over pixels whose full 3×3 window fits inside the image. 
# That’s rows 1 to 3 and columns 1 to 3, so you get a 3×3 output. 
# Every row should be:
# 10  40  70
# The edge used to jump 10 → 100 in one step. Now it’s a ramp, 10 → 40 → 70. That’s blur, shown with real numbers.
# Also notice that a 5×5 input gave a 3×3 output, because the border pixels have no full neighborhood.
# Cell 4 deals with that.    
def box_blur_loop(I):
    I = np.array(I).astype(np.float32)
    blurred = np.zeros((I.shape[0]-2, I.shape[1]-2), dtype=np.float32)
    for i in range(1, I.shape[0]-1):
        for j in range(1, I.shape[1]-1):            
            neighborhood = I[i-1:i+2, j-1:j+2]            
            blurred_value = neighborhood.sum() / 9
            blurred[i-1, j-1] = blurred_value            

    return blurred

    

# Cell 2: Blur one pixel by hand
# Pick the pixel at row 2, column 2. Its 3×3 neighborhood spans columns 1 to 3:
# 10 10 100
# 10 10 100
# 10 10 100
# Sum = 6×10 + 3×100 = 360, and 360 / 9 = 40.
# Write this cell with plain slicing (I[1:4, 1:4]), a .sum() and a divide by 9, with no loops. 
# Then predict column 3 before you run it. Its window spans columns 2 to 4, so 3×10 + 6×100 = 630, and 630 / 9 = 70.
def blur(I):
    I = np.array(I).astype(np.uint8)
    blurred = I[1:4, 1:4].sum() / 9
    print(f"Blurred pixel value at (2, 2): {blurred}")
    print(f"Predicted blurred pixel value at (2, 3): {I[1:4, 2:5].sum() / 9}")
    
# Cell 1: Build I and print it
# Make it uint8, and print its shape and dtype. 
#
def build_and_print(I):
    print("Input Image:", np.array(I).astype(np.uint8).shape)


if __name__ == "__main__":

    I = [
         [10,  10,  10,  100, 100],
         [10,  10,  10,  100, 100],
         [10,  10,  10,  100, 100],
         [10,  10,  10,  100, 100],
         [10,  10,  10,  100, 100]
        ]
    # build_and_print(I)
    # blur(I)
    # box_blur_loop(I)
    # #box blur with real image
    # show("Real blurred image", box_blur_loop(gray(load(IMAGE_PATH))).astype(np.uint8))
    # #padding 
    # print(pad_and_blur(I, mode='reflect'))
    # print(cv.blur(np.array(I, dtype=np.float32), (3, 3)))
    # show("Box blur with reflect-101 padding", pad_and_blur(gray(load(IMAGE_PATH)), mode='reflect').astype(np.uint8))

    # IR = [
    #         [0,  0,  0,  0,  0],
    #         [0,  0,  0,  0,  0],
    #         [0,  0,  1,  0,  0],
    #         [0,  0,  0,  0,  0],
    #         [0,  0,  0,  0,  0]
    #         ]
    # print("Impulse response:", impulse_response(IR))
    # show("Impulse response", impulse_response(gray(load(IMAGE_PATH))))

    print("Gaussian blur by hand:", gaussian_by_hand(I))
    print(np.allclose(gaussian_by_hand(I), cv.GaussianBlur(np.array(I, dtype=np.float32), (3, 3), 0)))  
    show("Gaussian blur by hand", gaussian_by_hand(gray(load(IMAGE_PATH))).astype(np.uint8))
