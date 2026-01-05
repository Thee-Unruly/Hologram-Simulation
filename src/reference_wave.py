# src/reference_wave.py
import numpy as np

def generate_plane_wave(shape):
    """
    Generate a simple plane reference wave with given shape (rows, cols)
    """
    rows, cols = shape
    x = np.linspace(-1, 1, cols)
    y = np.linspace(-1, 1, rows)
    X, Y = np.meshgrid(x, y)
    wave = np.exp(1j * 2 * np.pi * X)  # simple plane wave along X
    return wave
