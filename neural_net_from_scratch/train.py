"""Training script — run this to train the neural network on MNIST."""

import numpy as np
from .data import load_mnist, mini_batches
from .network import NeuralNetwork


def train():
    # ------- Configuration -------
    layer_sizes = [784, 128, 64, 10]  # Input(28x28) -> 128 -> 64 -> 10 classes
    learning_rate = 0.1
    epochs = 10
    batch_size = 64

    # ------- Load data -------
    print("Loading MNIST dataset...")
    train_images, train_labels, test_images, test_labels = load_mnist()
    print(f"  Training samples: {len(train_images)}")
    print(f"  Test samples:     {len(test_images)}")

    # ------- Build network -------
    print(f"\nNetwork architecture: {' -> '.join(map(str, layer_sizes))}")
    print(f"Learning rate: {learning_rate}")
    net = NeuralNetwork(layer_sizes, learning_rate=learning_rate)

    # ------- Train -------
    print("\nTraining...\n")
    for epoch in range(1, epochs + 1):
        epoch_losses = []

        for batch_images, batch_labels in mini_batches(
            train_images, train_labels, batch_size
        ):
            loss = net.train_step(batch_images, batch_labels)
            epoch_losses.append(loss)

        avg_loss = np.mean(epoch_losses)
        train_acc = net.accuracy(train_images, train_labels)
        test_acc = net.accuracy(test_images, test_labels)

        print(
            f"  Epoch {epoch:2d}/{epochs}  |  "
            f"Loss: {avg_loss:.4f}  |  "
            f"Train acc: {train_acc:.2%}  |  "
            f"Test acc: {test_acc:.2%}"
        )

    # ------- Final evaluation -------
    print(f"\nFinal test accuracy: {net.accuracy(test_images, test_labels):.2%}")
    print("Done!")


if __name__ == "__main__":
    train()
