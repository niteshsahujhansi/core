import speech_recognition as sr

audio_file = ('recording/recording.wav')
r = sr.Recognizer()
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)
try:
    print(r.recognize_google(audio))
except sr.UnknowValueError:
    print('Google speech recognition could not understand audio')
except sr.RequestError:
    print('Could not get result from google speech recognition')
    