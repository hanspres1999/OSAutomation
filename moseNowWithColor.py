import pyautogui as p
import time
#NOTE, the program is DEVICE and OS dependent!
try:
	while True:
		x,y = p.position()
		positionStr = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
		pixelColor = p.screenshot().getpixel((x, y))
		positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
		positionStr += ', ' + str(pixelColor[1]).rjust(3)
		positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
		print(positionStr, end='')
		print('\b'* len(positionStr), end='', flush=True)
except KeyboardInterrupt:
	print("\n Done!")