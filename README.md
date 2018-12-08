# VRChatPianoRoomSimulatorMidiInputToKeyboard
## Requirements
```
pip install pynput
pip install python-rtmidi
pip install mido
```
I only tested this on a CASIO CDP-120. So for now I'll say you need that model or a simliar model of keyboard.
## Instructions
run this ***BEFORE*** you open VRChat
```
python main.py
```
or
```
py -2 main.py
```
depending on what your system wants.
Once you're at the piano in the simulator room, switch to the experimental layout.
**now play your heart out**
## Overview
I tried to use 3rd party things that people were suggesting and they weren't quite doing it so I figured I'd do it myself. Initially I was having port issues and thought it would be impossible. However, I found out that VRChat actually searches for midi ports when it opens which is why I was having issues Currently right shift and numpad enter don't work so I'll fix those when it starts bothering me enough.
