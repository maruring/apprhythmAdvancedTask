# 先端課題022 Webから画像の自動収集

## 動作の前提条件
Docker desktopがインストールされており、動作するのが確認できていること  
インストールしていない場合は以下のリンクからダウンロード  
https://www.docker.com/products/docker-desktop/  

## 環境構築
1. コマンドプロンプトを起動
2. 任意のディレクトリに移動
3. git clone https://github.com/maruring/apprhythmAdvancedTask.git
4. cd ~/apptask_022
5. docker-compose up -d --build
6. 任意のブラウザを開く
7. アドレスバーに「localhost:8888」を打ち込む

## 動作方法
1. codesの中の scraping_images.ipynb を開く
2. shift + Enterで上から順に実行する
3. imgsディレクトリの中にDog, Cat, Rabbitのディレクトリがあり、各ディレクトリに画像が入っていることを確認する
