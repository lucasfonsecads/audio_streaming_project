"""
Module to train the audio model using PyTorch.
"""

import torch
from src.model import AudioModel

def train():
    """
    Train the AudioModel with dummy data.
    """
    model = AudioModel()
    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    
    # Dummy data
    inputs = torch.randn(10)
    targets = torch.randn(1)
    
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    loss.backward()
    optimizer.step()

if __name__ == "__main__":
    train()
