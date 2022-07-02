# 先端課題010 良品/不良品の2値分類ができるモデルの開発  
## 動作の前提条件
Docker desktopがインストールされており、動作するのが確認できていること  
インストールしていない場合は以下のリンクからダウンロード  
https://www.docker.com/products/docker-desktop/  

## 動作方法
XXXXXX  

## モデル
1. 転移学習
「resnext50_32x4d」,「vgg16」
最終層を2classに変更
最終層と最終層の1つまえの重みを変更

2. 自作モデル
