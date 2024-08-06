"""
Module defining the audio model using PyTorch.
"""

from torch import nn

class AudioModel(nn.Module):
    """
    A simple audio model class inheriting from nn.Module.
    """

    def __init__(self):
        super().__init__()
        self.layer = nn.Linear(10, 1)

    def forward(self, x):
        """
        Forward pass of the model.

        Args:
            x (Tensor): Input tensor.

        Returns:
            Tensor: Output tensor after passing through the layer.
        """
        return self.layer(x)
