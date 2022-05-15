from create_dataset import PennFunDataset
from Fine_tuning import get_instance_segmentation_model
from train_and_evaluation_funcs import get_transform
import torch
import utils
from engine import train_one_epoch, evaluate

import os

path = r'C:\Users\marur\PycharmProjects\apprhythmAdvancedTask\task_002\PennFudanPed'
dataset = PennFunDataset(path, get_transform(train=True))
dataset_test = PennFunDataset(path, get_transform(train=False))


torch.manual_seed(1)
indices = torch.randperm(len(dataset)).tolist()
dataset = torch.utils.data.Subset(dataset, indices[:-50])
dataset_test = torch.utils.data.Subset(dataset_test, indices[-50:])


# トレーニングと検証のデータローダーを定義します
data_loader = torch.utils.data.DataLoader(
    dataset, batch_size=2, shuffle=True, num_workers=4,
    collate_fn=utils.collate_fn)

data_loader_test = torch.utils.data.DataLoader(
    dataset_test, batch_size=1, shuffle=False, num_workers=4,
    collate_fn=utils.collate_fn)

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

# 教師データは、背景と人の2クラスのみです
num_classes = 2

# ヘルパー関数を使用してモデルを取得します
model = get_instance_segmentation_model(num_classes)
# モデルを適切なデバイスに移動します
model.to(device)

# オプティマイザを構築します
params = [p for p in model.parameters() if p.requires_grad]
optimizer = torch.optim.SGD(params, lr=0.005,
                            momentum=0.9, weight_decay=0.0005)

# 学習率を3エポックごとに10分の1に減らす学習率スケジューラ
lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer,
                                               step_size=3,
                                               gamma=0.1)

# 10エポックでトレーニング
num_epochs = 10

if __name__ == '__main__':
    for epoch in range(num_epochs):
        print(epoch)
        # 1エポックのトレーニング
        train_one_epoch(model, optimizer, data_loader, device, epoch, print_freq=10)
        # 学習率を更新する
        lr_scheduler.step()
        # テストデータセットで評価する
        evaluate(model, data_loader_test, device=device)