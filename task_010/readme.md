# 先端課題010 良品/不良品の2値分類ができるモデルの開発  
## 動作の前提条件
Docker desktopがインストールされており、動作するのが確認できていること  
インストールしていない場合は以下のリンクからダウンロード  
https://www.docker.com/products/docker-desktop/  

## 環境構築
1. 任意のディレクトリに移動  
2. git clone https://github.com/maruring/apprhythmAdvancedTask.git  
3. cd ~/apptask_010
4. docker build --no-cache -t apptask010 . (40分くらいかかります)  
5. docker container run -p 8051:8051 --name apptask010 -it apptask010 /bin/bash
6. streamlit run app.py --server.port 8051
7. アドレスバーに「localhost:8051」を打ち込む  

## 動作方法  
1. 判定用のモデルを選択  
2. 写真をアップロード  
![1](https://user-images.githubusercontent.com/58333988/177221770-306a1698-caa6-42a7-8c5e-a83c4e3f0ca8.PNG)  
3. 「判定」を押下  
![2](https://user-images.githubusercontent.com/58333988/177221803-409657a6-3663-445f-a104-8fdf402b58a4.PNG)  
4. 判定用に使用した写真と判定結果が表示されます  
![3](https://user-images.githubusercontent.com/58333988/177221822-d11a67d9-a168-4fa3-895e-4de830a041d1.PNG)  


## モデル
1. 転移学習
「resnext50_32x4d」,「vgg16」  
最終層を2classに変更  
最終層と最終層の1つまえの重みを変更  

2. 自作モデル  
![original pth](https://user-images.githubusercontent.com/58333988/177040515-bb89db95-18d3-4021-aa9c-a8af897c01eb.png)

## 使用したデータセット  
https://www.mvtec.com/company/research/datasets/mvtec-ad/  
上記のメタルナットのデータセットを使用
