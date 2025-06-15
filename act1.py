import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('your_image.jpg')  # <-- Replace with your image path
if image is None:
    raise ValueError("Image not found. Check the path to 'your_image.jpg'.")

# Convert from BGR (OpenCV default) to RGB (for matplotlib)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# ---------- 1. Rotate Image ----------
def rotate_image(img, angle):
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)

    # Rotation matrix
    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Compute the new bounding dimensions of the image
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    new_w = int((h * sin) + (w * cos))
    new_h = int((h * cos) + (w * sin))

    # Adjust the rotation matrix
    M[0, 2] += (new_w / 2) - center[0]
    M[1, 2] += (new_h / 2) - center[1]

    rotated = cv2.warpAffine(img, M, (new_w, new_h))
    return rotated

rotated_image = rotate_image(image, 45)
rotated_rgb = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)

# ---------- 2. Crop Image ----------
def crop_image(img, start_x, start_y, width, height):
    return img[start_y:start_y + height, start_x:start_x + width]

cropped_image = crop_image(image, 50, 50, 200, 200)
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)

# ---------- 3. Adjust Brightness ----------
def adjust_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    # Add brightness
    v = cv2.add(v, value)
    v = np.clip(v, 0, 255).astype(np.uint8)

    final_hsv = cv2.merge((h, s, v))
    bright_img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return bright_img

bright_image = adjust_brightness(image, value=50)
bright_rgb = cv2.cvtColor(bright_image, cv2.COLOR_BGR2RGB)

# ---------- Display with matplotlib ----------
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].imshow(image_rgb)
axes[0, 0].set_title("Original Image")
axes[0, 0].axis('off')

axes[0, 1].imshow(rotated_rgb)
axes[0, 1].set_title("Rotated Image (45°)")
axes[0, 1].axis('off')

axes[1, 0].imshow(cropped_rgb)
axes[1, 0].set_title("Cropped Image")
axes[1, 0].axis('off')

axes[1, 1].imshow(bright_rgb)
axes[1, 1].set_title("Brightness Increased")
axes[1, 1].axis('off')

plt.tight_layout()
plt.show()

