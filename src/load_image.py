# src/load_image.py
from PIL import Image
import numpy as np

def load_image(path: str, grayscale=True):
    """
    Load an image from the given path and normalize it to 0-1.
    """
    img = Image.open(path)
    if grayscale:
        img = img.convert("L")
    arr = np.array(img) / 255.0
    return arr
