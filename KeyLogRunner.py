import pyautogui as p
import pickle
import time



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

def decode(eventList, inTime):
	if (eventList[0] == 'kp' or eventList[0] == 'kr'):
		time.sleep(inTime)
	if (eventList[0] == "mr"):
		p.moveTo(eventList[1], eventList[2],duration=(inTime))
		p.click(eventList[1], eventList[2])
	elif (eventList[0] == "kp" and eventList[1]=='Key.ctrl'):
		p.keyDown('ctrlleft')
	elif (eventList[0] == "kr" and eventList[1]=='Key.ctrl'):
		p.keyUp('ctrlleft')
	elif (eventList[0] == "kp" and eventList[1]=='Key.shift'):
		p.keyDown('shift')
	elif (eventList[0] == "kr" and eventList[1]=='Key.shift'):
		p.keyUp('shift')
	elif (eventList[0] == "kp" and eventList[1]=='Key.alt'):
		p.keyDown('altleft')
	elif (eventList[0] == "kr" and eventList[1]=='Key.alt'):
		p.keyUp('altleft')
	elif (eventList[0] == 'kr' and eventList[1]=='Key.tab'):
		p.hotkey('tab')
	elif (eventList[0] == 'kp' and eventList[1]=='Key.cmd'):
		p.hotkey('winleft')		
	elif (eventList[0] != "kp") :
		p.hotkey(eventList[1])
	elif (eventList[0] == 'kp' and eventList[1]=='Key.space'):
		p.hotkey(' ')		
	elif (eventList[0] == 'kp' and eventList[1]=='Key.backspace'):
		p.hotkey('backspace')		
	elif (eventList[0] == 'kp' and eventList[1]=='Key.enter'):
		p.hotkey('enter')		
		


Fname=input("Enter the name of your task ->  ")
Fname = Fname + ".task"
print(Fname)
logDict = pickle.load( open( Fname, "rb" ) )
#file = open(Fname, "rb")
#logDict = load(logDict, file)
print('Loaded!')
#printplus(logDict)

keyList = logDict.keys()
	
prevTime = 0	
i = 1
for key in sorted(logDict):
	if (i==0 or i==len(logDict)-1 or i==len(logDict)-2):
		continue
	currentTime = key
	event = logDict[key]
	if event[0] == 'mp':
		continue
	deltaTime = currentTime - prevTime
	print(deltaTime)
	print(i, end='   ')
	print(key, end='   ')
	print(logDict[key])
	# time.sleep(deltaTime)
	decode(event,deltaTime)
	prevTime = currentTime
	i+=1

exit()	

