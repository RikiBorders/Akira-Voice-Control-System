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
        terms:string: string of terms the user wants to search for (split by spaces)
    RETURNS: 
        None
    DESC: Create a new tab in the user's browser
    and create a google search using the terms the user
    specified.
    '''
    terms = terms.split(' ')
    query = ''
    for i in range(len(terms)):
        query += terms[i]
        if i != len(terms)-1:
            query += '+'

    url = f'https://www.google.com.tr/search?q={query}'
    webbrowser.open_new_tab(url)