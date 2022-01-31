from rangel.arquivo import *
from json import loads, dumps

def ordem(js: list, coluna: str)->dict:
	'''Função que ordena uma lista

	Parameters:
		js (list): Lista de dicionários para ser ordenada
		coluna (str): Nome da coluna para ordenar por ela

	Returns:
		lista (list): Lista ordenada
	'''
	original = js
	try:
		js.sort(key=lambda x: x[coluna])
		return js
	except Exception as er:
		print('ordem:')
		print(er)
		return original

def ler_json(arquivo: str)->dict:
	'''Função que lê um arquivo e converte para um dicionario ou uma lista de dicionários

	Parameters:
		arquivo (str): nome do arquivo a ser lido

	Returns:
		lista (dict/list): Dicionário ou lista de dicionário
	'''
	try:
		tx = ler_arquivo(arquivo)
		js = loads(tx)
		return js
	except Exception as er:
		print('ler_json:')
		print(er)
		return []

def salvar_json(arquivo: str, js: list):
	'''Função que salva uma lista de dicionários em um arquivo

	Parameters:
		arquivo (str): Nome do arquivo para salvar
		js (list): Lista de dicionários para ser salvo
	'''
	try:
		tx = dumps(js, indent=4)
		salvar_arquivo(arquivo, tx)
	except Exception as er:
		print('salvar_json:')
		print(er)
