from engine import train_one_epoch, evaluate
import utils
import transforms as T

def get_transform(train):
    transforms = []
    # 画像をTensorに変換
    transforms.append(T.ToTensor())

    if train:
        # トレーニングの場合、ランダムに画像と教師データを水平方向に反転します。（鏡に映すイメージ
        transforms.append(T.RandomHorizontalFlip(0.5))

    return T.Compose(transforms)