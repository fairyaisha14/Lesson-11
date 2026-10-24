import cv2
import numpy as np
import os

os.makedirs("images", exist_ok=True)

image = cv2.imread("Girl1.jpg")

if image is None:
    print("Girl1.jpg not found!")
    exit()

red, green, blue = 1.0, 1.0, 1.0
tint = None

while True:
    img = image.astype(float).copy()

    img[:, :, 2] *= red
    img[:, :, 1] *= green
    img[:, :, 0] *= blue

    if tint == "r":
        img[:, :, 1:] *= 0.4
    elif tint == "g":
        img[:, :, 0] *= 0.4
        img[:, :, 2] *= 0.4
    elif tint == "b":
        img[:, :, :2] *= 0.4

    img = np.clip(img, 0, 255).astype("uint8")
    cv2.imshow("Colour Filters", img)

    key = cv2.waitKey(0)

    if key == ord("r"):
        tint = "r"
    elif key == ord("g"):
        tint = "g"
    elif key == ord("b"):
        tint = "b"
    elif key == ord("i"):
        red = min(2.0, red + 0.1)
    elif key == ord("d"):
        blue = max(0.0, blue - 0.1)
    elif key == 82:
        green = min(2.0, green + 0.1)
    elif key == 84:
        red = max(0.0, red - 0.1)
    elif key == ord("s"):
        name = input("Filename: ")
        name = "".join(c if c.isalnum() or c in "_-" else "_" for c in name)
        cv2.imwrite(f"images/{name or 'image'}.png", img)
        print("Image saved!")
    elif key == ord("0"):
        red = green = blue = 1.0
        tint = None
    elif key == ord("q"):
        break

cv2.destroyAllWindows()