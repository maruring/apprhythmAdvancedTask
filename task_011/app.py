import streamlit as st
import pyaudio
import shutil
import os
import wave
from pred import pred
import glob

# 基本設定
frames = []
audio_path = []
audio = None
frame = None

rate = 44100
input_device_index = 1
frames_per_buffer = 1024
chunk = 2**11
rec_time = 10

def audiostart():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16,
                        rate=rate,
                        channels=1,
                        input_device_index=input_device_index,
                        input=True,
                        frames_per_buffer=frames_per_buffer)
    return audio, stream


def audiostop(audio, stream):
    stream.stop_stream()
    stream.close()
    audio.terminate()

def REC():
    # 音声ディレクトリにあるmp3ファイルを削除
    shutil.rmtree('audios')
    os.mkdir('audios')
    # 録音開始
    st.write("録音中")
    for i in range(0, int(rate / chunk * rec_time)):
        audio, frame = audiostart()
        frames.append(frame.read(chunk))

    st.write("録音終了")

    audiostop(audio, frame)
    wav = wave.open("./audios/input.wav", 'wb')
    wav.setnchannels(1)
    wav.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wav.setframerate(rate)
    wav.writeframes(b''.join(frames))
    wav.close()

def voice_pred():
    st.write("推論中...")
    audio_path = glob.glob("./audios/*")
    result = pred(audio_path)
    st.write("推論結果")
    st.write(result)



st.title("先端課題011 自動文字起こし")
st.button("録音開始", on_click=REC)
st.button("推論開始", on_click=voice_pred)

