import speech_recognition as sr

# Initialize the speech recognition engine
r = sr.Recognizer()

# Use the recorded audio as input
with sr.WavFile("output3.wav") as source:
    audio = r.record(source)

try:
    text = r.recognize_google(audio)
    print("Recognized text:", text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Error with speech recognition service:", e)