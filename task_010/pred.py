import torch
import torch.nn as nn
from torchvision import transforms, models
from original_model import Net

def pred(model_path, img):
    model = None

    #モデル読み込み
    if "original" in model_path:
        model = Net()
    elif "vgg16" in model_path:
        model = models.vgg16()
        model.fc = nn.Linear(4096, 2)
    elif "resnext" in model_path:
        model = models.resnext50_32x4d()
        model.fc = nn.Linear(2048, 2)

    model.load_state_dict(torch.load(model_path))
    model.eval()

    #ファイル読み込み
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                  std=[0.229, 0.224, 0.225])
    ])

    img = transform(img).unsqueeze(0)

    #予測
    output = model(img)
    softmax = nn.Softmax(dim=1)
    _, pred = torch.max(output, 1)
    ans = pred[0].item()
    if ans == 0:
        return "不良品"
    else:
        return "良品"
