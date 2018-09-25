import pyautogui as p
import time

try:
	while True:
		x,y = p.position()
		positionStr = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
		print(positionStr, end='')
		print('\b'* len(positionStr), end='', flush=True)
except KeyboardInterrupt:
	print("\n Done!")