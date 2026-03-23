"""MNIST data loading and preprocessing."""

import gzip
import os
import struct
import urllib.request

import numpy as np

MNIST_URL = "https://storage.googleapis.com/cvdf-datasets/mnist/"
DATA_DIR = os.path.join(os.path.dirname(__file__), "mnist_data")

FILES = {
    "train_images": "train-images-idx3-ubyte.gz",
    "train_labels": "train-labels-idx1-ubyte.gz",
    "test_images": "t10k-images-idx3-ubyte.gz",
    "test_labels": "t10k-labels-idx1-ubyte.gz",
}


def _download(filename: str):
    """Download a file from the MNIST mirror if not already cached."""
    os.makedirs(DATA_DIR, exist_ok=True)
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(MNIST_URL + filename, filepath)
    return filepath


def _read_images(filepath: str) -> np.ndarray:
    """Parse IDX image file format."""
    with gzip.open(filepath, "rb") as f:
        magic, num, rows, cols = struct.unpack(">IIII", f.read(16))
        data = np.frombuffer(f.read(), dtype=np.uint8)
    return data.reshape(num, rows * cols).astype(np.float32) / 255.0


def _read_labels(filepath: str) -> np.ndarray:
    """Parse IDX label file format."""
    with gzip.open(filepath, "rb") as f:
        magic, num = struct.unpack(">II", f.read(8))
        data = np.frombuffer(f.read(), dtype=np.uint8)
    return data


def load_mnist() -> tuple:
    """Download and load the full MNIST dataset.

    Returns:
        (train_images, train_labels, test_images, test_labels)
        - Images are flattened to (N, 784) and normalized to [0, 1]
        - Labels are integers 0-9
    """
    train_images = _read_images(_download(FILES["train_images"]))
    train_labels = _read_labels(_download(FILES["train_labels"]))
    test_images = _read_images(_download(FILES["test_images"]))
    test_labels = _read_labels(_download(FILES["test_labels"]))

    return train_images, train_labels, test_images, test_labels


def mini_batches(images: np.ndarray, labels: np.ndarray, batch_size: int = 64):
    """Yield shuffled mini-batches from the dataset."""
    indices = np.random.permutation(len(images))
    for start in range(0, len(images), batch_size):
        batch_idx = indices[start : start + batch_size]
        yield images[batch_idx], labels[batch_idx]
