import streamlit as st
from PIL import Image, ImageOps
import pandas as pd
import numpy as np
from keras.models import load_model

st.title('先端課題038 顔認証')

st.write('顔画像をアップロードしてください')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(image)
    st.image(image)

    if st.button('predict'):
        np.set_printoptions(suppress=True)
        model = load_model("./model/keras_Model.h5", compile=False)
        class_names = open("./model/labels.txt", "r").readlines()
        
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        # resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
        # turn the image into a numpy array
        image_array = np.asarray(image)
        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
        # Load the image into the array
        data[0] = normalized_image_array

        # Predicts the model
        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        st.write(class_name[2:])