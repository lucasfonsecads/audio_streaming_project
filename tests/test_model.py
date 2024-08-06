import unittest
import torch
from src.model import AudioModel

class TestAudioModel(unittest.TestCase):
    def test_model_forward(self):
        model = AudioModel()
        input_tensor = torch.randn(10)
        output_tensor = model(input_tensor)
        self.assertEqual(output_tensor.shape, torch.Size([1]))

if __name__ == '__main__':
    unittest.main()
