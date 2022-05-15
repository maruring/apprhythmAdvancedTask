import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torchvision.models.detection.mask_rcnn import MaskRCNNPredictor

# Faster R-CNN
# 物体検出アルゴリズムの１つで、画像内の潜在的なオブジェクトの境界ボックスとクラススコア（物体を含む四角形と、物体が何か）の両方を予測するモデルです。

# Mask R-CNN
# Faster R-CNN の改良版で 物体検知を四角形(box)で判断するだけではなく、ピクセル単位（mask）で判定します。

def get_instance_segmentation_model(num_classes):
    # cocoでトレーニング済みのモデルをロード
    model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)

    # 分類器の入力値特徴数を取得
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    # モデルの最終出力を変更
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

    # mask分類気の入力特徴数を取得
    in_features_mask = model.roi_heads.mask_predictor.conv5_mask.in_channels
    hidden_layer = 256

    model.roi_heads.mask_precictor = MaskRCNNPredictor(in_features_mask,hidden_layer,num_classes)

    return model
