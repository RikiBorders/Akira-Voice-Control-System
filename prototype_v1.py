import speech_recognition as sr
import re

def mainloop():
    print('run')
    
    # Listen for audio
    rc = sr.Recognizer()
    keyword = 'Akira' # keyword to initiate ocmmand listening
    with sr.Microphone() as source:

        rc.adjust_for_ambient_noise(source, duration=5)

        print('talk')
        audio = rc.listen(source)

    try:
        print(rc.recognize_google(audio))
    except sr.UnknownValueError:
        print('Audio not understood')



mainloop()
