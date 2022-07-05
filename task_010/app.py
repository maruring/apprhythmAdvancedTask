import streamlit as st #フロント部分
import torch
from torchvision import transforms
from pred import pred
from PIL import Image

st.title("先端課題008 良品/不良品 判定")

model_choice = st.radio("モデルを選択してください",
                 ("resnex50_32x5d", "vgg16", "original"))

#モデルを選択
if model_choice ==  "resnex50_32x5d":
    model_path = "./models/resnext50_32x4d.pth"
elif model_choice == "vgg16":
    model_path = "./models/vgg16.pth"
elif model_choice == "original":
    model_path = "./models/original.pth"

uploaded_file = st.file_uploader(label="写真をアップロードしてください", type=['png', 'jpeg'])

if st.button("判定"):
    if not uploaded_file== None:
        img = Image.open(uploaded_file)
        st.image(img)
        result = pred(model_path=model_path, img=img)
        st.write(result)
    else:
        st.write("ファイルをアップロードしてください")

else:
    pass