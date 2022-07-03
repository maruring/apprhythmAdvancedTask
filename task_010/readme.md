# 先端課題010 良品/不良品の2値分類ができるモデルの開発  
## 動作の前提条件
Docker desktopがインストールされており、動作するのが確認できていること  
インストールしていない場合は以下のリンクからダウンロード  
https://www.docker.com/products/docker-desktop/  

## 環境構築
1. 任意のディレクトリに移動  
2. git clone https://github.com/maruring/apprhythmAdvancedTask.git  
3. cd ~/apptask_010
4. docker build --no-cache -t apptask010 .
5. docker container run -p 8051:8051 --name apptask010  
6. cd home/src  
7. streamlit run app.py --server.port 8051  
8. アドレスバーに「localhost:8051」を打ち込む  

## 動作方法  


## モデル
1. 転移学習
「resnext50_32x4d」,「vgg16」
最終層を2classに変更  
最終層と最終層の1つまえの重みを変更  

2. 自作モデル
