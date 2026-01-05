# src/hologram_generator.py
import numpy as np

def generate_hologram(object_image, reference_wave):
    """
    Create interference pattern (hologram) from object and reference wave
    """
    object_wave = np.fft.fftshift(np.fft.fft2(object_image))
    hologram = np.abs(object_wave + reference_wave) ** 2
    return hologram
