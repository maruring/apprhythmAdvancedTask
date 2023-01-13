import torch
import torch.nn as nn
from torchvision import transforms, models

def predict(model_path, img):
    model = models.vgg16()
    model.fc = nn.Linear(4096, 3)

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
        return "Dog"
    elif ans == 1:
        return "Cat"
    else:
        return "Rabbit"