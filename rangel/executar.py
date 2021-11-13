from threading import Thread
from os import system

def executar_rp(exe):
	try:
		system(exe)
	except Exception as er:
		print('executar_rp:')
		print(er)

def outraRota(funcao, *args):
	try:
		t = Thread(target = funcao, args = args)
		t.daemon = True
		t.start()
	except Exception as er:
		print('outraRota:')
		print(er)

def executar(exe):
	try:
		self.outraRota(executar_rp, exe)
	except Exception as er:
		print('executar:')
		print(er)
