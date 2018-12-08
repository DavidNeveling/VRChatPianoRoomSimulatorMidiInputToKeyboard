# VRChatPianoRoomSimulatorMidiInputToKeyboard
## Requirements
If you don't already have them, install python 2 and pip, then run
```
pip install pynput
pip install python-rtmidi
pip install mido
```
I only tested this on a CASIO CDP-120. So for now I'll say you need that model or a simliar model of keyboard.
## Instructions
Find the name of your input ports using
```
print mido.get_input_names()
```
Whichever input port looks right to you keep track of the name as *nameOfChoice*. Then replace the code segment
```
inputstring = open('../midi/maininput.txt').readline()
print inputstring
inport = mido.open_input(inputstring)
```
with
```
inport = mido.open_input(nameOfChoice)
```
Then run this ***BEFORE*** you open VRChat
```
python main.py
```
or
```
py -2 main.py
```
depending on what your system wants.
Once you're at the piano in the simulator room, switch to the experimental layout.
**now play your heart out**.
Hit the bottom note when you want to exit. (haven't tested this I just assumed it would work)
## Overview
I tried to use 3rd party things that people were suggesting and they weren't quite doing it so I figured I'd do it myself. Initially I was having port issues and thought it would be impossible. However, I found out that VRChat actually searches for midi ports when it opens which is why I was having issues Currently right shift and numpad enter don't work so I'll fix those when it starts bothering me enough.
