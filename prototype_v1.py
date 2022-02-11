import speech_recognition as sr
from pocketsphinx import LiveSpeech
import re
import time


# Initialize microphone and recognizer
rc = sr.Recognizer()
source = sr.Microphone()


def callback(rc, audio):
    print('callback run')

    # key-words to initiate command listening
    keywords = [('hey akira', 1), ('akira', 1)] 
    try:
        speech_as_text = rc.recognize_sphinx(audio, keyword_entries=keywords)

        # Look for your "hey akira" keyword in speech_as_text
        if "akira" in speech_as_text or "hey akira":
            print('identified')
            recognize_main()

    except sr.UnknownValueError:
        print("Oops! Didn't catch that")


def recognize_main():
    # Begin listening for accompanying command
    print("Activated. Recognizing main command...")
    audio_data = rc.listen(source)


def mainloop():
    print('main run')
    rc.listen_in_background(source, callback, phrase_time_limit=3)
    time.sleep(10000) # Time to listen



mainloop()
