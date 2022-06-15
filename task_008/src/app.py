import streamlit as st #フロント部分
import io
import cv2 as cv
import numpy as np
import sys
import tempfile
import head_pose_predictor as head
import glob
import os

st.title("先端課題008 視線推定")

uploaded_file = st.file_uploader(label="動画をアップロードしてください", type=['mp4', 'avi'])

if st.button("目視推定実行"):
    if not uploaded_file== None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())
        vf = cv.VideoCapture(tfile.name)
        dir_no = str(len(glob.glob("/result/*")) + 1)
        img_no = 0

        while vf.isOpened():
            ret, frame = vf.read()

            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            pred_frame = head.pred_head_pose(frame)
            height, width, layer = pred_frame.shape
            # 保存するディレクトリを作成
            save_dir = f"./result/{dir_no}"
            if os.path.exists(save_dir):
                pass
            else:
                os.mkdir(save_dir)

            # フォルダに画像を保存
            cv.imwrite(f'./result/{dir_no}/{str(img_no)}.jpg', pred_frame)
            img_no += 1
        
        # sizeを格納
        size = (width, height)
        print(size)
        # encoder(for mp4)
        fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
        # output file name, encoder, fps, size(fit to image size)
        video = cv.VideoWriter(f'./{save_dir}/result.mp4', fourcc, 25.0, size)

        for img_path in glob.glob(save_dir + "/*.jpg"):
            img = cv.imread(img_path)
            video.write(img)
        
        vf.release()
        video.release()

        video_file = open(f'./{save_dir}/result.mp4', 'rb')
        video_bytes = video_file.read()

        st.download_button(
            label="Download result",
            data=video_file,
            file_name='result.mp4',
            )

    else:
        st.write("ファイルをアップロードしてください")

else:
    pass