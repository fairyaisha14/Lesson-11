# Students will manipulate color channels of a static image in real-time by pressing specific keys to apply different color filters, including color tints and intensity adjustments. The image will be updated instantly with each key press.

import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    """Apply a color filter to an image."""
    filtered_image = image.copy()

    if filter_type == "red_tint":
        filtered_image[:, :, 0] = 0  # Remove blue
        filtered_image[:, :, 1] = 0  # Remove green

    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0  # Remove green
        filtered_image[:, :, 2] = 0  # Remove red

    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0  # Remove blue
        filtered_image[:, :, 2] = 0  # Remove red

    elif filter_type == "increase_red":
        filtered_image[:, :, 2] = cv2.add(
            filtered_image[:, :, 2], 50
        )

    elif filter_type == "decrease_blue":
        filtered_image[:, :, 0] = cv2.subtract(
            filtered_image[:, :, 0], 50
        )

    return filtered_image


# Load the image
image_path = "Girl1.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found! Check the image path.")
else:
    filter_type = "original"

    print("Press a key to apply a filter:")
    print("r: Red Tint")
    print("b: Blue Tint")
    print("g: Green Tint")
    print("i: Increase Red Intensity")
    print("d: Decrease Blue Intensity")
    print("o: Original Image")
    print("q: Quit")

    while True:
        filtered_image = apply_color_filter(image, filter_type)

        cv2.imshow("Filtered Image", filtered_image)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('r'):
            filter_type = "red_tint"
        elif key == ord('b'):
            filter_type = "blue_tint"
        elif key == ord('g'):
            filter_type = "green_tint"
        elif key == ord('i'):
            filter_type = "increase_red"
        elif key == ord('d'):
            filter_type = "decrease_blue"
        elif key == ord('o'):
            filter_type = "original"
        elif key == ord('q'):
            print("Exiting...")
            break
        elif key != 255:
            print("Invalid key! Use r, b, g, i, d, o, or q.")

    cv2.destroyAllWindows()
