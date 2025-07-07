import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile

model = whisper.load_model("base")  # "small" or "medium" for better accuracy

def record_audio(filename="output.wav", duration=5):
    fs = 44100
    print("🎙️ Speak now...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    scipy.io.wavfile.write(filename, fs, audio)
    return filename

def transcribe_audio(filename):
    result = model.transcribe(filename,fp16=False, language="ur")
    return result['text'].lower()
