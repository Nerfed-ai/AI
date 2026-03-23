"""Loss functions for training."""

import numpy as np


class CrossEntropyLoss:
    """Cross-entropy loss for classification tasks.

    Expects softmax probabilities as input and integer class labels.
    """

    def __init__(self):
        self.predictions = None
        self.targets = None
        self.batch_size = None

    def forward(self, predictions: np.ndarray, targets: np.ndarray) -> float:
        """Compute loss.

        Args:
            predictions: Softmax probabilities, shape (batch_size, num_classes)
            targets: Integer class labels, shape (batch_size,)

        Returns:
            Scalar loss value.
        """
        self.predictions = predictions
        self.targets = targets
        self.batch_size = predictions.shape[0]

        # Clip to avoid log(0)
        clipped = np.clip(predictions, 1e-12, 1.0 - 1e-12)

        # Pick the predicted probability for each true class
        correct_probs = clipped[np.arange(self.batch_size), targets]

        return -np.mean(np.log(correct_probs))

    def backward(self) -> np.ndarray:
        """Compute gradient of loss w.r.t. softmax input (combined gradient).

        The combined softmax + cross-entropy gradient is simply:
            gradient = predictions - one_hot(targets)
        This is one of the most elegant results in deep learning math.
        """
        grad = self.predictions.copy()
        grad[np.arange(self.batch_size), self.targets] -= 1
        return grad / self.batch_size
