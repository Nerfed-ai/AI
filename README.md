# Neural Network from Scratch

A fully functional neural network built using **only NumPy** — no PyTorch, no TensorFlow. Trains on MNIST handwritten digits and achieves ~97% accuracy.

## What You'll Learn

- **Forward propagation** — how data flows through layers
- **Backpropagation** — how gradients flow backward to update weights
- **Gradient descent** — how the network learns from mistakes
- **Activation functions** — ReLU and Softmax
- **Cross-entropy loss** — measuring prediction quality
- **Mini-batch training** — efficient stochastic gradient descent

## Project Structure

```
neural_net_from_scratch/
├── layers.py       # Linear, ReLU, Softmax layers
├── loss.py         # Cross-entropy loss function
├── network.py      # NeuralNetwork class (ties it all together)
├── data.py         # MNIST download and preprocessing
└── train.py        # Training loop
```

## Quick Start

```bash
pip install -r requirements.txt
python -m neural_net_from_scratch
```

MNIST data is downloaded automatically on first run.

## Architecture

```
Input (784) → Linear → ReLU → Linear → ReLU → Linear → Softmax → Output (10)
   28×28 pixels     128 neurons    64 neurons     10 digit classes
```

## Next Steps

Ideas to extend this project:
- Add dropout regularization
- Implement momentum or Adam optimizer
- Add a convolutional layer
- Visualize learned weights
- Save/load trained models
- Try on Fashion-MNIST or CIFAR-10
