from pynput import keyboard
from pynput import mouse
import os
import pyautogui
import time
import pickle
import sys

logDict = {}


Fname = input("Enter the name of this task -> ")
Fname = Fname + ".task"
t = time.time()


def saveToFile():
	file = open( Fname, "wb" )
	pickle.dump( logDict, file )
	file.close()
	print("File is Loaded, saved and closed! \n Task is now saved!")


def printplus(obj):
	"""
	Pretty-prints the object passed in.

	"""
	# Dict
	if isinstance(obj, dict):
	    for k, v in sorted(obj.items()):
	        print('{0}: {1}'.format(k, v))

	# List or tuple            
	elif isinstance(obj, list) or isinstance(obj, tuple):
	    for x in obj:
	        print(x)

	# Other
	else:
	    print(obj)




def get_key_name(key):	  #Gives the key name when a key is pressed.
	if isinstance(key, keyboard.KeyCode):
		return key.char
	else:
		return str(key)

def on_press(key):				#prints a key when it is pressed
	print("			A key was pressed:")
	tempTime= time.time()
	key_name = get_key_name(key)
	key = tempTime - t
	key = round(key, 4)
	value = ["kp", key_name]
	logDict.update({key : value})
	
	print('Key {} pressed.'.format(key_name))

def on_release(key):			#When a key is released
	
	key_name = get_key_name(key)
	tempTime= time.time()
	key_name = get_key_name(key)
	key = tempTime - t
	key = round(key, 4)
	value = ["kr", key_name]
	logDict.update({key : value})
	
	print('Key {} released.'.format(key_name))

	if key_name == 'Key.esc':  #The esc condition: Elegantly exits the program
		print('Exiting...')
		printplus(logDict)
		saveToFile()
		pyautogui.hotkey('ctrl', 'z')

def on_click(x, y, button, pressed): #for mouse clicks: When and where was the mouse clicked
	tempTime= time.time()
	print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))

	#storing to the keyLog:
	key = tempTime - t
	if pressed:
		value = ["mp", x, y]
	else:
		value = ["mr", x, y]
	key = round(key, 4)
	logDict.update({key : value})

	if not pressed:
	# Stop listener
		return True

def on_scroll(x, y, dx, dy):  #for mouse scrolls: when and where was the mouse scrolled.
	tempTime= time.time()
	key = tempTime - t
	key = round(key, 4)
	value = ["ms", x, y, dy]
	logDict.update({key : value})
	print('Scrolled {0}, steps downwards   '.format((x, y)), end='')
	print(dy)



#Heres where the execution starts.



	 

try	:
	with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
		with mouse.Listener(on_click=on_click, on_scroll=on_scroll) as listener:
			listener.join()
except SystemExit:
	print("\n\n\n\n")
	print(logDict)		
