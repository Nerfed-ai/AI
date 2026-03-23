"""The neural network — ties layers together into a trainable model."""

import numpy as np
from .layers import Linear, ReLU, Softmax
from .loss import CrossEntropyLoss


class NeuralNetwork:
    """A simple feedforward neural network.

    Architecture: Input -> [Linear -> ReLU] x N -> Linear -> Softmax
    """

    def __init__(self, layer_sizes: list[int], learning_rate: float = 0.01):
        """
        Args:
            layer_sizes: List of layer dimensions.
                         e.g., [784, 128, 64, 10] for MNIST
            learning_rate: Step size for gradient descent.
        """
        self.learning_rate = learning_rate
        self.layers = []

        # Build hidden layers with ReLU activation
        for i in range(len(layer_sizes) - 2):
            self.layers.append(Linear(layer_sizes[i], layer_sizes[i + 1]))
            self.layers.append(ReLU())

        # Output layer with softmax (no ReLU before softmax)
        self.layers.append(Linear(layer_sizes[-2], layer_sizes[-1]))
        self.layers.append(Softmax())

        self.loss_fn = CrossEntropyLoss()

    def forward(self, x: np.ndarray) -> np.ndarray:
        """Run input through all layers."""
        for layer in self.layers:
            x = layer.forward(x)
        return x

    def backward(self, loss_grad: np.ndarray):
        """Backpropagate gradient through all layers (reverse order)."""
        grad = loss_grad
        for layer in reversed(self.layers):
            grad = layer.backward(grad)

    def update_weights(self):
        """Apply gradient descent to all Linear layers."""
        for layer in self.layers:
            if isinstance(layer, Linear):
                layer.weights -= self.learning_rate * layer.grad_weights
                layer.bias -= self.learning_rate * layer.grad_bias

    def train_step(self, x: np.ndarray, targets: np.ndarray) -> float:
        """One full training step: forward -> loss -> backward -> update.

        Returns the loss value.
        """
        predictions = self.forward(x)
        loss = self.loss_fn.forward(predictions, targets)
        loss_grad = self.loss_fn.backward()
        self.backward(loss_grad)
        self.update_weights()
        return loss

    def predict(self, x: np.ndarray) -> np.ndarray:
        """Return predicted class labels."""
        probabilities = self.forward(x)
        return np.argmax(probabilities, axis=1)

    def accuracy(self, x: np.ndarray, targets: np.ndarray) -> float:
        """Compute classification accuracy (0.0 to 1.0)."""
        predictions = self.predict(x)
        return np.mean(predictions == targets)
