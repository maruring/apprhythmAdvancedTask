import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

st.title('先端課題039 streamlit')
st.write('グラフの表示')
# Please write your code!!
st.dataframe(data=pd.read_csv('./data/data.csv'))

st.write('ファイルのアップロード&表示')
# Please write your code!!
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    st.image(image)
    st.balloons()
