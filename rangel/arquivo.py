def ler_arquivo(arquivo: str)->str:
	'''Função que lê um arquivo

	Parameters:
		arquivo (str): nome do arquivo a ser lido

	Returns:
		texto (str): texto do arquivo lido
	'''
	try:
		f = open(arquivo, 'r', encoding='utf8')
		t = f.read()
		f.close()
		return t
	except Exception as er:
		print('ler_arquivo:')
		print(er)
		return ''

def salvar_arquivo(arquivo: str, texto: str):
	'''Função que salva texto em arquivo

	Parameters:
		arquivo (str): Nome do arquivo
		texto (str): Texto a ser salvo
	'''
	try:
		f = open(arquivo, 'w', encoding='utf8')
		f.writelines(texto)
		f.close()
	except Exception as er:
		print('salvar_arquivo:')
		print(er)