from pynput import keyboard
from pynput import mouse
import os
import pyautogui


def get_key_name(key):          #Gives the key name when a key is pressed.
    if isinstance(key, keyboard.KeyCode):
        return key.char
    else:
        return str(key)

def on_press(key):				#prints a key when it is pressed
	print("			A key was pressed:")
	key_name = get_key_name(key)
	print('Key {} pressed.'.format(key_name))

def on_release(key):			#When a key is released
    key_name = get_key_name(key)
    print('Key {} released.'.format(key_name))

    if key_name == 'Key.esc':  #The esc condition: Elegantly exits the program
        print('Exiting...')
        return False

def on_click(x, y, button, pressed): #for mouse clicks: When and where was the mouse clicked
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        # Stop listener
        return True

def on_scroll(x, y, dx, dy):  #for mouse scrolls: when and where was the mouse scrolled.
    print('Scrolled {0}, steps downwards   '.format((x, y)), end='')
    print(dy)



#Heres where the execution starts.
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
	with mouse.Listener(on_click=on_click, on_scroll=on_scroll) as listener:
		listener.join()