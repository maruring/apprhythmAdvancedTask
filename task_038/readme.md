# 先端課題038 顔認証システムの開発

## 動作の前提条件
Docker desktopがインストールされており、動作するのが確認できていること
インストールしていない場合は以下のリンクからダウンロード
[https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

## 環境構築
1. コマンドプロンプトを起動
2. 任意のディレクトリに移動
3. git clone [https://github.com/maruring/apprhythmAdvancedTask.git](https://github.com/maruring/apprhythmAdvancedTask.git)
4. cd ~/apptask_038
5. docker-compose up -d --build(3分ぐらいかかります)
6. 任意のブラウザを開く
7. アドレスバーに「localhost:8501」を打ち込む

## 動作方法
1. 顔画像をuploadする
2. predict ボタンを押下する
3. 結果が表示される