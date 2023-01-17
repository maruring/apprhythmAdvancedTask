import streamlit as st
from pred import predict
from PIL import Image
import torch
from torchvision import transforms

model_path = "./model/original.pth"

st.title('先端課題024 犬,猫,ウサギの判定')
uploaded_file = st.file_uploader("Choose a file")

if st.button("判定"):
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img)
        result = predict(model_path=model_path, img=img)
        st.write(result)
    else:
        st.write("ファイルをアップロードしてください")

else:
    pass
