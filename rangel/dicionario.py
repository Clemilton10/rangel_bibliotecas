from rangel.arquivo import *
from json import loads, dumps

def ordem(js, coluna) -> dict:
	original = js
	try:
		js.sort(key=lambda x: x[coluna])
		return js
	except Exception as er:
		print('ordem:')
		print(er)
		return original

def ler_json(arquivo) -> dict:
	try:
		tx = ler_arquivo(arquivo)
		js = loads(tx)
		return js
	except Exception as er:
		print('ler_json:')
		print(er)
		return []

def salvar_json(arquivo, js):
	try:
		tx = dumps(js, indent=4)
		salvar_arquivo(arquivo, tx)
	except Exception as er:
		print('salvar_json:')
		print(er)
