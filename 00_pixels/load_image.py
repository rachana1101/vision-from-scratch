import os
import time
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(ROOT, "..", "resources", "images", "cute_dog.jpg")


def show(title, img):
    """Display with OpenCV (expects BGR or single-channel)."""
    cv.imshow(title, img)
    cv.waitKey(0)
    cv.destroyAllWindows()


# ---------- Cell 1: Load ----------
def cell1_load(path):
    image = cv.imread(path)
    if image is None:
        raise FileNotFoundError(f"Image not found at path: {path}")
    print(f"Image shape: {image.shape}")      # (rows=H, cols=W, channels)
    print(f"Image data type: {image.dtype}")  # uint8: 0..255
    show("Loaded Image", image)
    return image


# ---------- Cell 2: One pixel ----------
def cell2_pixel(image):
    print(f"Image pixel: {image[100, 200, 0]}")  # [B G R] -> blue is first 


# ---------- Cell 3: Matplotlib, 3 panels ----------
def cell3_matplotlib(image, gray):
    plt.figure()  # Creates new figure window
        
    plt.subplot(131)  
    plt.imshow(image) 
    plt.title('wrong colors') 

    plt.subplot(132)  
    plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))  # Convert BGR to RGB for correct display
    plt.title('RGB')

    plt.subplot(133)  
    plt.imshow(gray, cmap='gray')
    plt.title('gray')

    plt.show()

# ---------- Cell 4: Grayscale by hand ----------
def cell4_gray_loop(image):
    gray_image = np.zeros(image.shape[:2], dtype=np.uint8)
    rows, cols = image.shape[:2]
    for i in range(rows):
        for j in range(cols):
            gray = 0.2989 * image[i, j][2] + 0.5870 * image[i, j][1] + 0.1140 * image[i, j][0]
            gray_image[i, j] = round(gray)
    return gray_image


def cell4_gray_vectorized(image):
    #same formula on whole channels, no loops
    b, g, r = image[:,:,0], image[:,:,1], image[:,:,2]
    gray_image = 0.2989 * r + 0.5870 * g + 0.1140 * b
    #return gray_image.astype(np.uint8)
    return np.round(gray_image).astype(np.uint8)



def cell4_proof(image):
    t0 = time.perf_counter()
    mine = cell4_gray_loop(image)
    t1 = time.perf_counter()
    mineTime = t1 - t0
    print(f"loop time: {t1 - t0:.4f}s")
    print(f"gray pixel value at (100, 200): {mine[100, 200]}")  # expect 221

    opencv = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    show("My Gray", mine)
    show("OpenCV Gray", opencv)

    t0 = time.perf_counter()
    vec = cell4_gray_vectorized(image)
    t1 = time.perf_counter()
    vectorizedTime = t1 - t0
    print(f"vectorized time: {t1 - t0:.4f}s")

    print(f"loop time / vectorized time: {mineTime / vectorizedTime:.2f}x faster")

    #print max absolute difference (cast to int first!)
    print(f"max absolute difference: {np.max(np.abs(mine.astype(int) - opencv.astype(int)))}")
    print(np.count_nonzero(mine != opencv))
    return mine


# ---------- Cell 5: Crop ----------
def cell5_crop(image):
    # crop 100x100, print shape, zero it, observe view vs copy
    img = image.copy()  # Make a copy to avoid modifying the original image

    cropped = img[100:200, 100:200]
    print(f"Cropped shape: {cropped.shape}")
    cropped[:] = 0  # This will modify the original image since cropped is a view
    show("Cropped and Zeroed", cropped)
    show("Original Image After Cropping", img)  # The original image will also be
    print(f"np.shares_memory(cropped, img): {np.shares_memory(cropped, img)}")  # True, since cropped is a view

    crop = image[100:200, 100:200].copy()
    show("Cropped Image", crop)
    crop[:] = 0  # This will not affect the original image since crop is a copy
    show("Original Image After Copying", image)  # The original image will remain unchanged
    print(f"np.shares_memory(crop, image): {np.shares_memory(crop, image)}")  # False, since crop is a copy

# ---------- Cell 6: Brightness ----------
def cell6_brightness(gray):
    #+100 on uint8 (see the wraparound), then fix it
    wrapped = (gray + 100)
    show("Wrapped Image", wrapped)
    print(f"Wrapped pixel value at (100, 200): {wrapped[100, 200]}")  # This may wrap around
    brightened = np.clip(gray.astype(np.int16) + 100, 0, 255).astype(np.uint8)
    show("Brightened Image", brightened)
    print(f"Brightened pixel value at (100, 200): {brightened[100, 200]}")  # This should not wrap around

    if np.array_equal(brightened, cv.add(gray, 100)):
        print("Brightened image matches OpenCV's add function.")
    else:
        print("Brightened image does not match OpenCV's add function.")


# ---------- Cell 7: Histogram ----------
def cell7_histogram(gray):
    #np.bincount over 0..255, plot it
    hist = np.bincount(gray.flatten(), minlength=256)
    plt.bar(range(256), hist)
    plt.title("Histogram")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.show()
    print(hist.sum())
    print(np.array_equal(hist, np.histogram(gray, bins=256, range=(0, 256))[0]))    


if __name__ == "__main__":
    image = cell1_load(IMAGE_PATH)
    cell2_pixel(image)
    gray = cell4_proof(image)
    cell3_matplotlib(image, gray)
    cell5_crop(image)
    cell6_brightness(gray)
    cell7_histogram(gray)