# src/utils.py
import matplotlib.pyplot as plt

def plot_image(image, title="Image", cmap="gray", save_path=None):
    plt.imshow(image, cmap=cmap)
    plt.title(title)
    plt.axis("off")
    if save_path:
        plt.savefig(save_path, bbox_inches="tight", dpi=200)
    plt.show()
