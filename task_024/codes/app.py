import streamlit as st
from pred import pred
from PIL import Image

model_path = "./models/vgg16.pth"

st.title('先端課題024 犬,猫,ウサギの判定')
uploaded_file = st.file_uploader("Choose a file")

if st.button("判定"):
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img)
        result = pred(model_path=model_path, img=img)
        st.write(result)
    else:
        st.write("ファイルをアップロードしてください")

else:
    pass
