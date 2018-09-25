import pyautogui as p
import time

# Program to open Paint application, draw something and close it.
#NOTE, the program is DEVICE and OS dependent!
p.moveTo(32, 110, duration = 1)
p.click()
time.sleep(3)

p.hotkey('ctrl', 'winleft', 'up')
xmax, ymax = p.size()
xmid = xmax/2
ymid = ymax/2
p.moveTo(xmid, ymid-100, duration=1 )

distance = 200
while distance > 0:
	p.dragRel(distance, 0, duration=0.1)  # move right
	distance = distance - 5
	p.dragRel(0, distance, duration=0.1)   # move down
	p.dragRel(-distance, 0, duration=0.1) # move left
	distance = distance - 5
	p.dragRel(0, -distance, duration=0.1)

p.moveTo(13, 13, duration=1)
p.click()
time.sleep(1)
p.hotkey('left')
time.sleep(1)
p.hotkey('enter')