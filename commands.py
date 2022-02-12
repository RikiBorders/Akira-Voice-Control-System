'''
This file holds all of Akira's 
executable commands. This file does not include 
command parsing, speech recognition, or anything else
related directly to the main voice control system. 
'''

import webbrowser



def web_search(terms):
    '''
    PARAMS:
        terms:list: list of terms the user wants to search for
    RETURNS: 
        None
    DESC: Create a new tab in the user's browser
    and create a google search using the terms the user
    specified.
    '''
    print('run')