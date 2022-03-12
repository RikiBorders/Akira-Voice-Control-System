# Akira: A Cross-platform Voice Control System

## Overview 

Voice control system that can be shared across multiple platforms, automating a variety of tasks for users.
This project aims to automate a variety of tasks for users, and improve general quality of life by connecting 
all user devices, regardless of brand or device type. By connecting user devices, users can seamlessly retrieve
data from device B, while using device A. If a user is far from home, for example, and has their phone, but forgot an important document
on their personal computer, then Akira can (prospectively) retrieve the document remotely and deliver to the user. 



## Contributions

Anybody is welcome to contribute to this project - contributions are encouraged. While I am working on this project without the intent 
of having additional developers consistently contributing to this repository, any contributions are welcomed and would bring
fresh, unique ideas to Akira. If issues are found, also please be sure to create an issue ticket! 

Any features being actively worked on are specified in the [Projects tab](https://github.com/RikiBorders/Akira-Voice-Control-System/projects?type=beta).
I will try to keep this as up to date as possible, though I'm unfortunately not psychic and cannot promise if that tab will be used
for the entire duration of this project's development.

General feature requests or contributions can be submitted by the [Issues tab](https://github.com/RikiBorders/Akira-Voice-Control-System/issues).
If you have any additional questions, feel free to contact me! (Contact info not yet uploaded)

### Adding Commands

Adding commands can be confusing at first, but after adding a command the process should become much more clear. When implementing the command itself (i.e, the function called by akira such as a web search), write the function itself and any accompanying functions in [commands.py](https://github.com/RikiBorders/Akira-Voice-Control-System/blob/main/commands.py). When the command has been implemented, it must be added to the 'command map'. The command map is a dictionary that stores all commands. To add a command to the command map, create a new sub-dictionary to [commands.json](https://github.com/RikiBorders/Akira-Voice-Control-System/blob/main/commands.json). Key descriptions can be found directly below:

- "first": the first word of the command (even if the command is only one word long)
- "full": the entire command (parameters do not need to be included in the value for this key)
- "cmd": After Akira parses commands, this string is returned to signal what command to execute. In other words, "cmd" is used to signal what function to call when the command            is identified
- "params": Boolean indicating if the command has parameters or not. Parameters always come after the command stub. For example, consider the command "Look up how to ride a bike". "Look up" would be the command stub (there is an entry where the full command is "look up"), and "how to ride a bike" would be the parameter.

After the command function is written, and the command is added to the json file, the function associated with the command can be called in the *recognize_main* function in [prototype_v1.py](https://github.com/RikiBorders/Akira-Voice-Control-System/blob/main/prototype_v1.py). This is done by creating a new 'elif' case in *recognize_main*, and calling the function associated with the command within the elif case.

## Usage

To use Akira, simply clone this repository and run the *prototype_v1.py* file. This file relies on *commands.py*, which
holds the executable commands. 


Any commands that Akira executes are held in *commands.py*. Executing internet searches, retrieving files, and finding
videos are examples of executable commands. Anything related to voice detection, text to speech, text parsing, etc. 
Are contained within *prototype_v1.py*.

## Codebase

At the moment, Akira's codebase is relatively simple, but when this project reaches the point of implementing cross-platform functionality, 
I anticipate that the codebase will become much more convoluted than now. Currently, the codebase is as follows:

- prototype_v1.py : The entry point of the program. This contains all logic related to voice detection, and facilitates the execution and comprehension of spoken commands.
- commands.py : Contains all command functions used by Akira. These commands are called in prototype_v1.py, and complete a large variety of tasks.
- commands.json : Json file containing dictionary objects that hold commands Akira can understand, as well as the command type (c_type in prototype_v1.py).
