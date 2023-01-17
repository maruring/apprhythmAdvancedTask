# 先端課題024 犬と猫とウサギの画像分類Webアプリケーション

## 動作の前提条件
1. Docker desktopがインストールされており、動作するのが確認できていること  
インストールしていない場合は以下のリンクからダウンロード  
https://www.docker.com/products/docker-desktop/  

## 環境構築
1. コマンドプロンプトを起動
2. 任意のディレクトリに移動
3. git clone https://github.com/maruring/apprhythmAdvancedTask.git
4. cd ~/apptask_024
5. docker-compose up -d --build(15分ぐらいかかります)
6. 任意のブラウザを開く
7. アドレスバーに「localhost:8501」を打ち込む

## 動作方法
1. 「Browse files」ボタンを押下する
2. 犬か猫かウサギのファイルを選択する
![base1](https://user-images.githubusercontent.com/58333988/212811456-f5a713db-9c8a-498f-9f1d-dd956afb4459.PNG)

3. 「判定」ボタンを押下する
![base2](https://user-images.githubusercontent.com/58333988/212811473-3d774cf3-9a2f-4a2a-a684-119e9f5cafa7.PNG)
