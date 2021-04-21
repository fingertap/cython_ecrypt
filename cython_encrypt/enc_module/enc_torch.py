import torch
import torch.nn as nn
from torchvision import models as tv_models


class MyModel(nn.Module):
    def __init__(self):
        nn.Module.__init__(self)
        resnet = tv_models.resnet18()
        self.model = nn.Sequential(
            resnet.conv1, resnet.bn1, resnet.relu, resnet.maxpool,
            resnet.layer1, resnet.layer2, resnet.layer3, resnet.layer4
        )

    def forward(self, data):
        return self.model(data)


def test():
    model = MyModel()
    data = torch.rand(1, 3, 64, 64)
    assert model(data).size() == (1, 512, 2, 2)
    return 'OK'
