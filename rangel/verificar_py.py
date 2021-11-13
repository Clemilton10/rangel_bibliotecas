# pip install psutil

import psutil
from os import getpid

def verificar(script):
	for q in psutil.process_iter():
		if q.name().startswith('python'):
			if len( q.cmdline() ) > 1 and script in q.cmdline()[1] and q.pid != getpid():
				return True

	return False
