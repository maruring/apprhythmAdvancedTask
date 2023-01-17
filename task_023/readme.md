# 先端課題023 犬と猫とウサギの画像分類モデルの作成and検証

## Note
現状、modelの精度は80%を超えていないが、とりあえず提出しています。  
modelは改善していきます。

## 動作の前提条件
1. Docker desktopがインストールされており、動作するのが確認できていること  
インストールしていない場合は以下のリンクからダウンロード  
https://www.docker.com/products/docker-desktop/  
2. TRAINディレクトリの構造が以下の構造になっており、各ディレクトリに画像が入っていること(Lineworks Driveからダウンロードする)
./TRAIN  
├Cat  
├Dog  
└Rabbit
3. TESTディレクトリ内にテスト画像が入っていること(Lineworks Driveからダウンロードする)

## 環境構築
1. コマンドプロンプトを起動
2. 任意のディレクトリに移動
3. git clone https://github.com/maruring/apprhythmAdvancedTask.git
4. cd ~/apptask_023
5. docker-compose up -d --build(15分ぐらいかかります)
6. アドレスバーに「localhost:8888」を打ち込む

## 動作方法
1. codesの中の PreProcess.ipynb を開く
2. shift + Enterで上から順に実行する(学習には、30分ぐらいかかります)
3. codesの中の Evaluation.ipynb を開く
4. shift + Enterで上から順に実行する
5. scoreが80%以上になっていることを確認する
