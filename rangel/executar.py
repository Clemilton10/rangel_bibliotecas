from threading import Thread
from os import system

def executar_rp(exe: str):
	'''Função que executa um aplicativo externo

	Parameters:
		exe (str): String com aplicativo e parâmetros
	'''
	try:
		system(exe)
	except Exception as er:
		print('executar_rp:')
		print(er)

def outraRota(funcao, *args: tuple):
	'''Função que executa um aplicativo em paralelo (Thread)

	Parameters:
		args (tuple): Múltiplos parâmetros
			(arg1, arg2, arg3...)
	'''
	try:
		t = Thread(target = funcao, args = args)
		t.daemon = True
		t.start()
	except Exception as er:
		print('outraRota:')
		print(er)

def executar(exe: str):
	'''Função que executa um aplicativo externo em paralelo

	Parameters:
		exe (str): String com aplicativo e parâmetros
	'''
	try:
		outraRota(executar_rp, exe)
	except Exception as er:
		print('executar:')
		print(er)
