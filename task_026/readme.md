# 先端課題026 AutoMLライブラリの比較

## 動作の前提条件

1. Docker desktopがインストールされており、動作するのが確認できていること
   インストールしていない場合は以下のリンクからダウンロード
   https://www.docker.com/products/docker-desktop/
2. filesディレクトリ内に配布されたtrain.csvとtest.csvが存在すること

## 環境構築

1. Windows	PowerShellを起動
2. 任意のディレクトリに移動
3. git clone https://github.com/maruring/apprhythmAdvancedTask.git
4. cd ~/apptask_026
5. docker-compose up -d --build(3分ぐらいかかります)
6. 任意のブラウザを開く
7. アドレスバーに「localhost:8888」を打ち込む

## 動作方法

1. codes内の autogluon_code.ipynb を開く
2. codes内の autokeras_code.ipynb を開く
3. codes内の FLAML_code.ipynb を開く
4. 1~3の各ファイルをshift + Enterで上から順に実行する(処理には15分ぐらいかかります)
5. 各ファイルごとの精度を確認する
