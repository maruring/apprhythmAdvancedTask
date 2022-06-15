# 先端課題008_視線推定
## 動作の前提条件
docker desktopがインストールされていること  
されていない場合は以下のリンクを参考にインストール  
https://docs.docker.jp/docker-for-windows/install.html

## 環境作成
power shellで以下のコマンドを実行
1. docker pull maruring/apptask:008
2. task_008ディレクトリに移動
3. docker container run -p 8051:8051 --name apptask008 -v /src:/home -it maruring/apptask:008
4. cd home
5. streamlit run app.py --server.port 8051
6. アドレスバーに「localhost:8501」を打ち込む

## 実行
1. 拡張子が「.mp4」か「.avi」の200MB以下の動画をアップロード(動画がない場合は「example.mp4」を使用してください)  
2. 「目視推定実行」ボタンを押下  
3. **処理には5分ほどかかります**  
4. 「ダウンロード」ボタンを押下  
5. 目視推定の動画がダウンロードされます  

## 使用ライブラリ
dlib #機械学習系ライブラリ  
imutils #OpenCVの補助  
imutils import face_utils  
numpy  
cv2  
os  
streamlit #フロント部分  
io  
tempfile  
glob  
sys  
