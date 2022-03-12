'''
This file holds all of Akira's 
executable commands. This file does not include 
command parsing, speech recognition, or anything else
related directly to the main voice control system. 
'''
import webbrowser # Websearch functionality
# Audio control (currently used in toggle_mute)
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import time


#####################################################################
#                                                                   #
# The functions below are commands intended for use with Windows OS #
#                                                                   #
#####################################################################

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


def toggle_mute(action, app):
    '''
    PARAMS:
        action:bool: if true, mute the app parameter. If False, unmute.
        app:str: name of the application to mute/unmute. If NoneType, then
                 mute/unmute all applications. This string does not include
                 file extensions (like: .exe)
    RETURNS:
        None
    DESC: Mute or unmute a specific application, or the system. Sound must be playing in
          order to hear the changes take place.
    '''
    sessions = AudioUtilities.GetAllSessions()
            
    if action:
        # Find target app and mute
        for session in sessions:

            volume = session.SimpleAudioVolume

            if not app: # Mute all
                volume.SetMute(1, None)

            # Note: session.process.name will need file extension
            elif session.Process and session.Process.name().upper() == (app+'.exe').upper(): 
                volume.SetMute(1, None)
                break

    else:
        # Unmute target app
        for session in sessions:
            volume = session.SimpleAudioVolume
            
            if not app: # Mute all
                volume.SetMute(0, None)

            elif session.Process and session.Process.name().upper() == (app+'.exe').upper(): 
                volume.SetMute(0, None)
                break


def change_volume(action, app):
    '''
    PARAMS:
        action:bool: if true, increase application volume. Decrease if false.
        app:str: name of the application whos volume will be modified. If NoneType, then
                 increase/decrease volume of all applications. This string does not include
                 file extensions (i.e: .exe)
    RETURNS: None
    DESC: Increase or decrease the volume level of the application 
          with the name passed as the 'app' parameter.
    '''
    sessions = AudioUtilities.GetAllSessions()
            
    if action:
        # Find target app and adjust volume
        for session in sessions:
            
            # Increase all
            if not app: 
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))
                
                level = volume.GetMasterVolumeLevel()
                level = min(0, level+1) # 0 = max volume 
                volume.SetMasterVolumeLevel(level, None)  
                break

            # Increase Volume of specified application
            elif session.Process and session.Process.name().upper() == (app+'.exe').upper(): 
                # Get app audio interface and modify
                t_interface = session.SimpleAudioVolume
                volume = t_interface.GetMasterVolume()
                level = min(1.0, volume + 0.1) # 1.0 = max volume

                t_interface.SetMasterVolume(level, None)
                break

    else:
        # Find target app and adjust volume
        for session in sessions:
            
            # Decrease all
            if not app: 
                # Get audio interface and modify
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))

                level = volume.GetMasterVolumeLevel()
                level = max(-65.25, level - 5.5)
                volume.SetMasterVolumeLevel(level, None)
                break

            # Decrease Volume of specified application
            elif session.Process and session.Process.name().upper() == (app+'.exe').upper(): 
                # Get app audio interface and modify
                t_interface = session.SimpleAudioVolume
                volume = t_interface.GetMasterVolume()
                level = max(0, volume - 0.1) # 0 = min volume

                t_interface.SetMasterVolume(level, None)
                break



change_volume(0, 'chrome')
# change_volume(1, None)