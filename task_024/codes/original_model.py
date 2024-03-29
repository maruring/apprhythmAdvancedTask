import torch
from torch import optim as optim
from torch import nn as nn
import torchvision
from torchvision import datasets, transforms

#ネットワーク構成
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        # nn.Conv2d(入力チャンネル数,出力チャンネル数,カーネルサイズ)
        self.layer1 = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=5, padding=2),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.layer2 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=5, padding=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.fc = nn.Linear(256*256*2, 3)

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x