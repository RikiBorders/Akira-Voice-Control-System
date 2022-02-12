import speech_recognition as sr
from pocketsphinx import LiveSpeech
import re
import time
from commands import *

# Initialize microphone and recognizer
rc = sr.Recognizer()
source = sr.Microphone()


def callback(rc, audio):
    # key-words to initiate command listening
    keywords = [('hey akira', 1), ('akira', 1)] 
    
    try:
        speech_as_text = rc.recognize_sphinx(audio, keyword_entries=keywords)

        # Look for your "hey akira" keyword in speech_as_text
        if "akira" in speech_as_text or "hey akira":
            recognize_main()

    except sr.UnknownValueError:
        print("Speech unrecognizable")



def recognize_main():
    # Begin listening for accompanying command
    print("Activated. Recognizing main command...")
    audio_data = rc.listen(source, phrase_time_limit=5)
    command = rc.recognize_google(audio_data).lower()

    # Identify command type
    c_type, terms = process_command(command)

    if c_type == 'web_search':
        web_search(terms)
    else:
        print('unknown')
    

def process_command(command):
    '''
    PARAMS:
        command:str: full spoken command issued to Akira
    RETURNS:
        result:tuple: Contains the following data:
            c_type:string: command type
            clipped:string: full command with identifying keyword stub removed
    DESC: Process command type
    ''' 
    websearch_kwds = set(['look up', 'google', 'search'])

    result = (None, None)
    parsed = command.split(' ')

    if parsed[0] in websearch_kwds or parsed[0]+' '+parsed[1] in websearch_kwds:
        c_type = 'web_search'

        if parsed[0] in websearch_kwds:
            parsed.pop(0)
        else:
            parsed = parsed[2:]

        result = (c_type, ' '.join(parsed))


    return result


def mainloop():
    # Create background thread for command listening
    rc.listen_in_background(source, callback, phrase_time_limit=3)
    time.sleep(10000) # Time to listen



mainloop()
