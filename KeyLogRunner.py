import pyautogui as p
import pickle


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





Fname=input("Enter the name of your task ->  ")
Fname = Fname + ".task"
print(Fname)
logDict = pickle.load( open( Fname, "rb" ) )
#file = open(Fname, "rb")
#logDict = load(logDict, file)

printplus(logDict)

