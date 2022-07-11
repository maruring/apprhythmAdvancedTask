from huggingsound import SpeechRecognitionModel

def pred(audio_path):
    model = SpeechRecognitionModel("vumichien/wav2vec2-large-xlsr-japanese-hiragana")
    transcriptions = model.transcribe(audio_path)
    result = transcriptions[0].get("transcription")
    return result