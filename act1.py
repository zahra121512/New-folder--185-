import cv2
import numpy as np

def display_image(title, image):
    """Utility function to display an image."""
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def apply_color_filter(image, filter_type, intensity=50):
    """Apply the specified color filter to the image."""
    filtered_image = image.copy()
    
    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0  # Green channel
        filtered_image[:, :, 0] = 0  # Blue channel
    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0  # Green
        filtered_image[:, :, 2] = 0  # Red
    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0  # Blue
        filtered_image[:, :, 2] = 0  # Red
    elif filter_type == "increase_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], intensity)
    elif filter_type == "decrease_red":
        filtered_image[:, :, 2] = cv2.subtract(filtered_image[:, :, 2], intensity)
    elif filter_type == "increase_green":
        filtered_image[:, :, 1] = cv2.add(filtered_image[:, :, 1], intensity)
    elif filter_type == "decrease_green":
        filtered_image[:, :, 1] = cv2.subtract(filtered_image[:, :, 1], intensity)
    elif filter_type == "decrease_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], intensity)
    
    return filtered_image

def save_image(image):
    """Allow the user to save the filtered image."""
    filename = input("Enter a name for the image (without the extension): ")
    filename = "".join(c for c in filename if c.isalnum() or c in ('_', '-'))
    cv2.imwrite(f"images/{filename}.png", image)
    print(f"Image saved as images/{filename}.png")

def interactive_color_filter(image_path):
    """Interactive activity for real-time color filter application."""
    image = cv2.imread(image_path)
    if image is None:
        print("Error: image not found.")
        return

    print("\nSelect an option:")
    print("r - red tint")
    print("b - blue tint")
    print("g - green tint")
    print("i - increase red intensity")
    print("d - decrease red intensity")
    print("u - increase green intensity")
    print("x - decrease green intensity")
    print("q - quit")

    while True:
        filter_type = input("Enter your choice: ").lower()

        if filter_type == "r":
            filtered_image = apply_color_filter(image, "red_tint")
        elif filter_type == "b":
            filtered_image = apply_color_filter(image, "blue_tint")
        elif filter_type == "g":
            filtered_image = apply_color_filter(image, "green_tint")
        elif filter_type == "i":
            filtered_image = apply_color_filter(image, "increase_red", intensity=50)
        elif filter_type == "d":
            filtered_image = apply_color_filter(image, "decrease_red", intensity=50)
        elif filter_type == "u":
            filtered_image = apply_color_filter(image, "increase_green", intensity=50)
        elif filter_type == "x":
            filtered_image = apply_color_filter(image, "decrease_green", intensity=50)
        elif filter_type == "q":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
            continue

        display_image("Filtered Image", filtered_image)

        save_choice = input("Do you want to save this image? (yes/no): ")
        if save_choice.lower() == "yes":
            save_image(filtered_image)

# Example usage
# interactive_color_filter("images/example.jpg")