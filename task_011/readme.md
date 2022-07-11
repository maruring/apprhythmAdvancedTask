# 先端課題011 自動文字起こし  
## 動作の前提条件
- Docker desktopがインストールされており、動作するのが確認できていること  
インストールしていない場合は以下のリンクからダウンロード  
https://www.docker.com/products/docker-desktop/  


## 環境構築  
1. 任意のディレクトリに移動  
2. git clone https://github.com/maruring/apprhythmAdvancedTask.git  
3. cd ~/apptask_011  
4. conda create -n apptask011 python=3.8
5. y を押下
6. conda activate apptask011  
7. pip install --upgrade pip  
8. pip install ./PyAudio-0.2.11-cp38-cp38-win_amd64.whl  
9. pip install ./python_Levenshtein-0.12.2-cp38-cp38-win_amd64.whl  
10. pip install streamlit  
11. pip install huggingsound  
12. streamlit run app.py --server.port 8051  
13. アドレスバーに「localhost:8051」を打ち込む(勝手にブラウザが開いた場合はスキップ)

## 動作方法
1. 「録音開始」を押下  
2. 10秒間録音されるので**日本語**で何か話してください  
3. 「録画終了」という文字が出現したら録音は終わっています  
4. 「推論開始」を押下(最初の推論には3分ほどかかります)  
5. 録音中に話した言葉が文字で表示されます  

## 使用したモデル
vumichien/wav2vec2-large-xlsr-japanese-hiragana  
