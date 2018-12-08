import time, mido, sys
from pynput import keyboard
from pynput.keyboard import Key, KeyCode, Controller

control = Controller()
inputstring = open('../midi/maininput.txt').readline()
print inputstring
inport = mido.open_input(inputstring)
while True:
    for msg in inport:
        note = msg.dict()['note']
        nType = msg.dict()['type']
        if nType == 'note_on':
			if note == 1:
				sys.exit('app exit')
			if note == 36:
				control.press('z')
				control.release('z')
			if note == 37:
				control.press('s')
				control.release('s')
			if note == 38:
				control.press('x')
				control.release('x')
			if note == 39:
				control.press('d')
				control.release('d')
			if note == 40:
				control.press('c')
				control.release('c')
			if note == 41:
				control.press('v')
				control.release('v')
			if note == 42:
				control.press('g')
				control.release('g')
			if note == 43:
				control.press('b')
				control.release('b')
			if note == 44:
				control.press('h')
				control.release('h')
			if note == 45:
				control.press('n')
				control.release('n')
			if note == 46:
				control.press('j')
				control.release('j')
			if note == 47:
				control.press('m')
				control.release('m')
			if note == 48:
				control.press(Key.tab)
				control.release(Key.tab)
			if note == 49:
				control.press('1')
				control.release('1')
			if note == 50:
				control.press('q')
				control.release('q')
			if note == 51:
				control.press('2')
				control.release('2')
			if note == 52:
				control.press('w')
				control.release('w')
			if note == 53:
				control.press('e')
				control.release('e')
			if note == 54:
				control.press('4')
				control.release('4')
			if note == 55:
				control.press('r')
				control.release('r')
			if note == 56:
				control.press('5')
				control.release('5')
			if note == 57:
				control.press('t')
				control.release('t')
			if note == 58:
				control.press('6')
				control.release('6')
			if note == 59:
				control.press('y')
				control.release('y')
			if note == 60:
				control.press('u')
				control.release('u')
			if note == 61:
				control.press('8')
				control.release('8')
			if note == 62:
				control.press('i')
				control.release('i')
			if note == 63:
				control.press('9')
				control.release('9')
			if note == 64:
				control.press('o')
				control.release('o')
			if note == 65:
				control.press('p')
				control.release('p')
			if note == 66:
				control.press('-')
				control.release('-')
			if note == 67:
				control.press('[')
				control.release('[')
			if note == 68:
				control.press('=')
				control.release('=')
			if note == 69:
				control.press(']')
				control.release(']')
			if note == 70:
				control.press(Key.backspace)
				control.release(Key.backspace)
			if note == 71:
				control.press('\\')
				control.release('\\')
			if note == 72:
				control.press(Key.delete)
				control.release(Key.delete)
			if note == 73:
				control.press(Key.insert)
				control.release(Key.insert)
			if note == 74:
				control.press(Key.end)
				control.release(Key.end)
			if note == 75:
				control.press(Key.home)
				control.release(Key.home)
			if note == 76:
				control.press(Key.page_down)
				control.release(Key.page_down)
			if note == 77:
				control.press(KeyCode.from_vk(103))
				control.release(KeyCode.from_vk(103))
			if note == 78:
				control.press(KeyCode.from_vk(111))
				control.release(KeyCode.from_vk(111))
			if note == 79:
				control.press(KeyCode.from_vk(104))
				control.release(KeyCode.from_vk(104))
			if note == 80:
				control.press(KeyCode.from_vk(106))
				control.release(KeyCode.from_vk(106))
			if note == 81:
				control.press(KeyCode.from_vk(105))
				control.release(KeyCode.from_vk(105))
			if note == 82:
				control.press(KeyCode.from_vk(109))
				control.release(KeyCode.from_vk(109))
			if note == 83:
				control.press(KeyCode.from_vk(107))
				control.release(KeyCode.from_vk(107))
			if note == 84:
				control.press(',')
				control.release(',')
			if note == 85:
				control.press('l')
				control.release('l')
			if note == 86:
				control.press('.')
				control.release('.')
			if note == 87:
				control.press(';')
				control.release(';')
			if note == 88:
				control.press('/')
				control.release('/')
			if note == 89: #Right Shift doesn't work
				control.press(KeyCode.from_vk(161))
				control.release(KeyCode.from_vk(161))
			if note == 90:
				control.press(KeyCode.from_vk(100))
				control.release(KeyCode.from_vk(100))
			if note == 91:
				control.press(KeyCode.from_vk(97))
				control.release(KeyCode.from_vk(97))
			if note == 92:
				control.press(KeyCode.from_vk(101))
				control.release(KeyCode.from_vk(101))
			if note == 93:
				control.press(KeyCode.from_vk(98))
				control.release(KeyCode.from_vk(98))
			if note == 94:
				control.press(KeyCode.from_vk(102))
				control.release(KeyCode.from_vk(102))
			if note == 95:
				control.press(KeyCode.from_vk(99))
				control.release(KeyCode.from_vk(99))
			# if note == 96: #Right enter doesn't work
			# 	control.press('')
