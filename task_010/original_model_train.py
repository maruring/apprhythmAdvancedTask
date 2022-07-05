import torch
from torch import optim as optim
from torch import nn as nn
import torch.nn.functional as F
import torchvision
from torchvision import datasets, transforms
import copy

batch_size = 8
num_epochs = 30

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
        self.fc = nn.Linear(256*256*2, 2)

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x

# 前処理
transform_dict = {
        'train': transforms.Compose(
            [transforms.Resize((256,256)),
             transforms.RandomHorizontalFlip(),
             transforms.ToTensor(),
             transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                  std=[0.229, 0.224, 0.225]),
             ]),
        'test': transforms.Compose(
            [transforms.Resize((256,256)),
             transforms.ToTensor(),
             transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                  std=[0.229, 0.224, 0.225]),
             ])}

# データセットの準備
data_folder = "./Dataset"
transform = transform_dict["train"]
data = torchvision.datasets.ImageFolder(root=data_folder, transform=transform)

# trainとテストの分離
train_ratio = 0.8
train_size = int(train_ratio * len(data))
# int()で整数に。
val_size = len(data) - train_size
data_size = {"train": train_size, "val": val_size}

data_train, data_val = torch.utils.data.random_split(data, [train_size, val_size])

# データローダー
train_loader = torch.utils.data.DataLoader(data_train, batch_size=batch_size, shuffle=True)
val_loader = torch.utils.data.DataLoader(data_val, batch_size=batch_size, shuffle=False)
dataloaders = {"train": train_loader, "val": val_loader}

device = torch.device('cpu')
model = Net().to(device)

#最適化手法の定義
criterion = nn.CrossEntropyLoss()
optim = optim.Adam(model.parameters(), lr=1e-4)

# 学習
def train_model(model, criterion, optimizer, scheduler=None, num_epochs=25):
    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0

    for epoch in range(num_epochs):
        print(f'Epoch {epoch}/{num_epochs - 1}')
        print('-' * 10)

        # Each epoch has a training and validation phase
        for phase in ['train', 'val']:
            if phase == 'train':
                model.train()  # Set model to training mode
            else:
                model.eval()  # Set model to evaluate mode

            running_loss = 0.0
            running_corrects = 0

            # Iterate over data.
            for inputs, labels in dataloaders[phase]:
                inputs = inputs.to(device)
                labels = labels.to(device)

                # zero the parameter gradients
                optimizer.zero_grad()

                # forward
                # track history if only in train
                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs)
                    _, preds = torch.max(outputs, 1)
                    loss = criterion(outputs, labels)

                    # backward + optimize only if in training phase
                    if phase == 'train':
                        loss.backward()
                        optimizer.step()

                # statistics
                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)

            epoch_loss = running_loss / data_size[phase]
            epoch_acc = running_corrects.double() / data_size[phase]

            print(f'{phase} Loss: {epoch_loss:.4f} Acc: {epoch_acc:.4f}')

            # deep copy the model
            if phase == 'val' and epoch_acc > best_acc:
                best_acc = epoch_acc
                best_model_wts = copy.deepcopy(model.state_dict())

    print(f'Best val Acc: {best_acc:4f}')

    # load best model weights
    model_path = "./models/original.pth"
    torch.save(model.state_dict(), model_path)
    model.load_state_dict(best_model_wts)

if __name__ == "main":
    train_model(model, criterion, optim, num_epochs=num_epochs)