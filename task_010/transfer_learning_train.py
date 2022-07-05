import torch
from torch import optim as optim
import torch.nn as nn
import torchvision
from torchvision import datasets, models, transforms
import copy

batch_size = 8
num_classes = 2

# 前処理
transform_dict = {
        'train': transforms.Compose(
            [transforms.Resize((256,256)),
             transforms.RandomPerspective(distortion_scale=0.2, p=0.9),
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
    model_path = "./models/vgg16.pth"
    torch.save(model.state_dict(), model_path)
    model.load_state_dict(best_model_wts)

model = models.vgg16(pretrained=True)
# 最終層のアウトプットを変更
model.fc = nn.Linear(4096, num_classes)
# 最適化手法の定義
for name, param in model.named_parameters():
    print("name:" ,name)

# 入力層に近いlayer1.0は重みを変化させない
params_to_update_1 = []
#　最終層に近いlayer4.1は重みを変更する
params_to_update_2 = []
#　変更した最終層fcは重みを変更する
params_to_update_3 = []

# 学習させる層のパラメータ名を指定
update_param_names_1 = ["features.0.weight", "features.0.bias"]

update_param_names_2 = ["classifier.6.weight", "classifier.6.bias"]

update_param_names_3 = ['fc.weight', 'fc.bias']

# パラメータごとに各リストに格納
for name, param in model.named_parameters():

    if update_param_names_1[0] in name:
        param.requires_grad = True
        params_to_update_1.append(param)
        print("params_to_update_1に格納：", name)

    elif name in update_param_names_2:
        param.requires_grad = True
        params_to_update_2.append(param)
        print("params_to_update_2に格納：", name)

    elif name in update_param_names_3:
        param.requires_grad = True
        params_to_update_3.append(param)
        print("params_to_update_3に格納：", name)

# 学習設定
device = torch.device('cpu')
lr = 1e-4
num_epochs = 30

model.to(device)
optim = optim.Adam([
    {'params': params_to_update_1, 'lr': 1e-4},
    {'params': params_to_update_2, 'lr': 1e-4},
    {'params': params_to_update_3, 'lr': 1e-3},
    ], lr=lr, weight_decay=1e-4
)
criterion = nn.CrossEntropyLoss()

# if __name__ == "main":
train_model(model, criterion, optim, num_epochs=num_epochs)