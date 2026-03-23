"""Neural network layers built from scratch using only NumPy."""

import numpy as np


class Linear:
    """Fully connected (dense) layer: output = input @ weights + bias."""

    def __init__(self, in_features: int, out_features: int):
        # He initialization — good default for ReLU networks
        scale = np.sqrt(2.0 / in_features)
        self.weights = np.random.randn(in_features, out_features) * scale
        self.bias = np.zeros((1, out_features))

        # Cache for backprop
        self.input = None

        # Gradients
        self.grad_weights = None
        self.grad_bias = None

    def forward(self, x: np.ndarray) -> np.ndarray:
        self.input = x
        return x @ self.weights + self.bias

    def backward(self, grad_output: np.ndarray) -> np.ndarray:
        self.grad_weights = self.input.T @ grad_output
        self.grad_bias = np.sum(grad_output, axis=0, keepdims=True)
        return grad_output @ self.weights.T


class ReLU:
    """Rectified Linear Unit: max(0, x)."""

    def __init__(self):
        self.mask = None

    def forward(self, x: np.ndarray) -> np.ndarray:
        self.mask = x > 0
        return x * self.mask

    def backward(self, grad_output: np.ndarray) -> np.ndarray:
        return grad_output * self.mask


class Softmax:
    """Softmax activation — converts logits to probabilities."""

    def __init__(self):
        self.output = None

    def forward(self, x: np.ndarray) -> np.ndarray:
        # Subtract max for numerical stability
        shifted = x - np.max(x, axis=1, keepdims=True)
        exp_x = np.exp(shifted)
        self.output = exp_x / np.sum(exp_x, axis=1, keepdims=True)
        return self.output

    def backward(self, grad_output: np.ndarray) -> np.ndarray:
        # When paired with cross-entropy loss, the gradient simplifies
        # to (predicted - true). We pass the gradient through directly
        # because our loss function already computes this combined gradient.
        return grad_output
