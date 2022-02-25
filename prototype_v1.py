import speech_recognition as sr
from pocketsphinx import LiveSpeech
import re
import time
from commands import *
import json

# Initialize microphone and recognizer
rc = sr.Recognizer()
source = sr.Microphone()


def callback(rc, audio):
    '''
    PARAMS:
        rc:sr.Recognizer object: recognizer object for audio processing
        audio:audio object: Audio generated by user speech.
    RETURNS: None
    DESC: 
        Callback function when audio is heard. This function is 
        called in a separate thread (created by the listen_in_background
        function call).
    '''
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
    '''
    PARAMS: None
    RETURNS: None
    DESC: 
        Listen for the user to issue a command to Akira. 
        After a command is issued, identify the command
        (handled by process_command), and execute it.
    '''

    # Begin listening for accompanying command
    print("Activated. Recognizing main command...")
    audio_data = rc.listen(source, phrase_time_limit=5)
    command = rc.recognize_google(audio_data).lower()

    # Identify command type
    c_type, terms = process_command(command)
    
    if c_type == 'web_search' and terms:
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
    cmd_map = build_cmd_map()
    result = (None, None)

    parsed = command.split(' ')
    # parsed = strip_prefix(parsed)

    if parsed[0] not in cmd_map: # Check if command is valid
        return result
    else:
        
        # Get the target command
        for elem in cmd_map[parsed[0]]:
            full_cmd = elem[0].split(' ')

            for i in range(len(parsed)):
                if i == len(full_cmd): break
                
                # full command has been matched
                elif i == len(full_cmd)-1 and full_cmd[i] == parsed[i]: 
                    return (elem[1], ' '.join(parsed[i+1:]) ) # convert the command (in list form) into string w/o command stub

    return result


def strip_prefix(command, commands):
    '''
    PARAMS:
        command:list: parsed command to process
        commands:set: set of first words for each command. For example, the 
                      command 'What's the weather like' would store 'What's'
                      in this set.
    RETURNS:
        command:list: command stripped of its prefix words. This can also
                      return null.
    DESC:
        Iteratively pop the first element on the command list
        until the first word matches the first word of some command
        in commands
    '''
    while command and command[0] not in commands:
        command = command[1:]

    return command


def build_cmd_map():
    '''
    PARAMS: None
    RETURNS: cmd_map:dict: Hashmap containing all commands
    DESC:
        This function will build the command map used for identifying commands.
        The key in cmd_map is the first word of the command. the value
        is a list of commands that share the same first word, & the command. I.e 
        'what time is it' and 'what is the temperature' would be stored
        as: cmd_map[what] = [('what time is it', c_type), ('what is the temperature', c_type)]
    '''

    # JSON FORMATTING
    # JSON file is formatted with the first word of the command as the key,
    # and the value as the full command. Furthermore, each word/command pair
    # also has a command k/v pair, formatted as "cmd":"c_type", where
    # "c_type" is the command to be executed, and identified by this function
    # (process_command)  
    cmd_map = {}

    # Read in JSON file 
    json_file = open('commands.json')
    data = json.load(json_file)

    for subdict in data['commands']: # Parse & add commands to command map
        if subdict['first'] not in cmd_map:
            cmd_map[subdict['first']] = [(subdict['full'], subdict['cmd'])]

        else: # Add to existing key
            cmd_map[subdict['first']].append((subdict['full'], subdict['cmd']))

    json_file.close()
    return cmd_map


def main():
    '''
    PARAMS: None
    RETURNS: None
    DESC:
        Program entry point & main function.
        This function spawns a new thread that will listen in the 
        background for the user to initiate command to Akira.
    '''
    # Create background thread for command listening
    rc.listen_in_background(source, callback, phrase_time_limit=3)
    time.sleep(10000) # Time to listen


main()
