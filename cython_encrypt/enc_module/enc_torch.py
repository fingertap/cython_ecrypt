import torch
import torch.nn as nn
from torchvision import models as tv_models


class MyModel(nn.Module):
    def __init__(self):
        nn.Module.__init__(self)
        self.resnet = tv_models.resnet18()

    def forward(self, data):
        return self.resnet(data)
