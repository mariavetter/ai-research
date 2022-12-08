from pydub import AudioSegment

AudioSegment.from_wav("./Audio_files/audio.wav").export("./Audio_files/audio.mp3", format="mp3")