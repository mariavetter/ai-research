import speech_recognition as sr

print(sr.__version__)

r = sr.Recognizer()

audioFile = sr.AudioFile('audio.wav')
with audioFile as source:
    audio = r.record(source)

print(r.recognize_google(audio))