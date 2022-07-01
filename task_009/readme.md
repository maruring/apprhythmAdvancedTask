# 先端課題009 Teachable Machineを用いたモデルの自動生成  
## 全体の流れ
1. モデルを選択
2. データの収集
3. モデル作成
4. テスト
5. モデルのエクスポート

## モデルの選択  
Teachable Machineでは「画像」、「音声」、「ポーズ」の3つからモデルを選択することができる。  
今回の課題は下記の内容である  
**片腕を垂直方向にあげているポーズと片腕を水平方向にあげているポーズを判定するモデルを構築**  
ポーズによって判断を行うため「ポーズ」のモデルを使用する  
ポーズのモデルを選択  
![1](https://user-images.githubusercontent.com/58333988/176896187-0fe784a2-16be-45ca-8f65-57635abff892.PNG)  

## データ収集  
Teachable MachineではWebカメラからの撮影でデータを収集することが可能であるため、その機能を活用して  
「片腕を垂直方向にあげているポーズ」と「片腕を水平方向にあげているポーズ」の学習データを収集する。  
「Webカメラ」を押下  
![2](https://user-images.githubusercontent.com/58333988/176896310-c71891b7-d7fb-4928-8608-dce5137789df.PNG)  
「長押しして録画」を押下して、腕を垂直方向に上げた写真と水平方向に上げた写真をとります    
顔をスプレーで塗りつぶしているので、黒くなっていますが、本来は黒くなりません  
![3](https://user-images.githubusercontent.com/58333988/176896910-0a5e6c6e-4f55-4fd7-9d31-31fe2db51bca.PNG)  
最後のそれぞれのclass名を変更します  
![4](https://user-images.githubusercontent.com/58333988/176898140-0b595f13-fdb6-4586-b600-1f8a49a31271.PNG)  


## モデル作成
「モデルをトレーニングする」を押下  
![5](https://user-images.githubusercontent.com/58333988/176898149-81ea8b9d-dc6f-478a-9595-dc824836a699.PNG)  
トレーニングが始まっていることが確認できます  
![6](https://user-images.githubusercontent.com/58333988/176898163-a2938acf-1a4c-4936-ac16-51adb06da56e.PNG)  
モデルが完成したのが確認できました。  
![7](https://user-images.githubusercontent.com/58333988/176899141-e8db9d41-ad3d-41b5-8bcd-1cdac8a9baf9.PNG)  


## テスト
腕と垂直方向と水平方向に上げて、判定出来るかを確認します  
きちんと判定できることが確認できました  
![10](https://user-images.githubusercontent.com/58333988/176899749-7c2150d0-8632-44fd-b467-264f323b5f45.PNG)  

## モデルのエクスポート
モデルが完成したので、モデルをエクスポートします  
「モデルをエクスポートする」を押下  
![11](https://user-images.githubusercontent.com/58333988/176900179-181a7852-b1a1-45ab-91ef-e2a27a8ad7a7.PNG)  
アップロード(共有可能なリンク)を選択して「モデルをアップロード」を押下  
![12](https://user-images.githubusercontent.com/58333988/176900310-b7dda63f-6cf7-4b38-89f4-16038ce9b3a2.PNG)  
赤丸部分をメモします  
![13](https://user-images.githubusercontent.com/58333988/176900459-3bf5ff45-b687-4f68-8012-b59da15e42b5.PNG)  

以下のリンクで僕の作成したモデルを試すことができます  
https://teachablemachine.withgoogle.com/models/e27ldtRz6/


