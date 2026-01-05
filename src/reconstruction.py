# src/reconstruction.py
import numpy as np

def reconstruct_hologram(hologram):
    """
    Reconstruct image from hologram (digital back-propagation)
    """
    reconstruction = np.fft.ifft2(np.fft.ifftshift(hologram))
    return np.abs(reconstruction)