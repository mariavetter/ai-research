import speech_recognition as sr
import time
import whisper
import pocketsphinx
import os
import pyaudio
import wave
from pydub import AudioSegment

r = sr.Recognizer()

# Words that sphinx should listen closely for. 0-1 is the sensitivity
# of the wake word.
keywords = [("hello", 1), ("hey hello", 1), ]

source = sr.Microphone()


def callback(recognizer, audio):  # this is called from the background thread

    try:
        #model = whisper.load_model("base")
        #speech_as_text = model.transcribe(audio)
        speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries=keywords)
        print(speech_as_text)

        # Look for your "hello" keyword in speech_as_text
        if "hello" in speech_as_text or "hey hello":
            recognize_main()

    except sr.UnknownValueError:
        print("Oops! Didn't catch that")


def recognize_main():
    print("Recognizing Main...")
    #audio_data = r.listen(source)
    FORMAT = pyaudio.paInt16 # 16 bits per sample
    CHANNELS = 1
    RATE = 44100 # Record at 44100 samples per second
    CHUNK = 1024 # Record in chunks of 1024 samples
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "./Audio_files/audio.wav"

    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print("recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("finished recording")


    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    AudioSegment.from_wav("./Audio_files/audio.wav").export("./Audio_files/audio.mp3", format="mp3")

    #print(audio_data)
    # interpret the user's words however you normally interpret them
    model = whisper.load_model("base")
    result = model.transcribe("./Audio_files/audio.mp3")
    print(result)


def start_recognizer():
    r.listen_in_background(source, callback)
    time.sleep(1000000)


start_recognizer()