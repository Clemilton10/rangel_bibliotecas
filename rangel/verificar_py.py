# pip install psutil

import psutil
from os import getpid

def verificar(script: str)->bool:
	'''Verifica se um script python (py) está rodando

	Parameters:
		script (string): nome do arquivo py que vai ser verificado

	Returns:
		resposta (boolean): Se encontrar True, caso contrário False
	'''
	for q in psutil.process_iter():
		if q.name().startswith('python'):
			if len( q.cmdline() ) > 1 and script in q.cmdline()[1] and q.pid != getpid():
				return True

	return False
