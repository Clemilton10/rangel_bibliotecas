# -*- coding: utf-8 -*-
from rangel.shell_style import shell_style
ss = shell_style()

def tabela_colorida(colunas=(), alinhamento=(), dados=[]):
	'''Função que cria uma tabela extraida de uma lista

	Parameters:
		colunas (tuple): Nome das colunas (opcional)
		alinhamento (tuple): Alinhamento de cada coluna (opicional)
		dados (list): Lista com dados para tabela
	'''
	try:
		# juntando as colunas pra ver qual o texto maior
		if colunas != ():
			tmp_dados = []
			tmp_dados.append(colunas)
			tmp_dados = tmp_dados + dados.copy()
		else:
			tmp_dados = dados.copy()

		# enfileirando cada coluna em uma lista pra saber quem é maior
		lista_reordenada = []
		for j, d in enumerate(tmp_dados[0]):
			lista_reordenada.append([])

		for j, d in enumerate(tmp_dados[0]):
			for i, l in enumerate(tmp_dados):
				lista_reordenada[j].append(l[j])

		# convertendo tudo para string
		for j, d in enumerate(tmp_dados[0]):
			lista_reordenada[j] = list( map( str, lista_reordenada[j]) )

		# gerando lista com o maior número de caracteres de cada coluna
		lista_max = []
		for j, d in enumerate(tmp_dados[0]):
			maior_nome = max( lista_reordenada[j], key=len )
			nmax = len( maior_nome )
			lista_max.append(nmax)

		# printando as colunas
		if colunas != ():

			# o nome das colunas
			linha = f'{ss.CF_AMARELA}| '
			for j, d in enumerate(tmp_dados[0]):
				if alinhamento != ():
					if alinhamento[j] == 'd':
						linha += f'{ss.CF_AMARELA}{ss.NEGRITO}{colunas[j]: >{lista_max[j]+1}}{ss.NONE} {ss.CF_AMARELA}| '
					elif alinhamento[j] == 'c':
						linha += f'{ss.CF_AMARELA}{ss.NEGRITO}{colunas[j]: ^{lista_max[j]+1}}{ss.NONE} {ss.CF_AMARELA}| '
					else:
						linha += f'{ss.CF_AMARELA}{ss.NEGRITO}{colunas[j]: <{lista_max[j]+1}}{ss.NONE} {ss.CF_AMARELA}| '
				else:
					linha += f'{ss.CF_AMARELA}{ss.NEGRITO}{colunas[j]: <{lista_max[j]+1}} {ss.CF_AMARELA}| '
			linha = linha[ 0: len(linha) - 1 ]
			print(linha)

			# a linha de baixo
			linha = '|-'
			for j, d in enumerate(tmp_dados[0]):
				nada = ''
				linha += f'{nada:-<{lista_max[j]+1}}-|-'
			linha = ss.CF_AMARELA + linha[ 0: len(linha) - 1 ] + ss.NONE
			print(linha)

		# printando os dados da coluna
		for l in dados:
			linha = f'{ss.CF_AMARELA}| '
			for j, d in enumerate(tmp_dados[0]):
				rw = str(l[j]).replace('\t', '').replace('\r', '').replace('➜', '>').replace('\n', '$')
				if alinhamento != ():
					if alinhamento[j] == 'd':
						linha += f'{ss.CFB_BRANCA}{rw: >{lista_max[j]+1}} {ss.CF_AMARELA}| '
					elif alinhamento[j] == 'c':
						linha += f'{ss.CFB_BRANCA}{rw: ^{lista_max[j]+1}} {ss.CF_AMARELA}| '
					else:
						linha += f'{ss.CFB_BRANCA}{rw: <{lista_max[j]+1}} {ss.CF_AMARELA}| '
				else:
					linha += f'{ss.CFB_BRANCA}{rw: <{lista_max[j]+1}} {ss.CF_AMARELA}| '
			linha = linha[ 0: len(linha) - 1 ]
			print(linha)

		print(ss.NONE)

	except Exception as er:
		print('tabela:')
		print(er)

def tabela(colunas=(), alinhamento=(), dados=[]):
	'''Função que cria uma tabela extraida de uma lista

	Parameters:
		colunas (tuple): Nome das colunas (opcional)
		alinhamento (tuple): Alinhamento de cada coluna (opicional)
		dados (list): Lista com dados para tabela
	'''
	try:
		# juntando as colunas pra ver qual o texto maior
		if colunas != ():
			tmp_dados = []
			tmp_dados.append(colunas)
			tmp_dados = tmp_dados + dados.copy()
		else:
			tmp_dados = dados.copy()

		# enfileirando cada coluna em uma lista pra saber quem é maior
		lista_reordenada = []
		for j, d in enumerate(tmp_dados[0]):
			lista_reordenada.append([])

		for j, d in enumerate(tmp_dados[0]):
			for i, l in enumerate(tmp_dados):
				lista_reordenada[j].append(l[j])

		# convertendo tudo para string
		for j, d in enumerate(tmp_dados[0]):
			lista_reordenada[j] = list( map( str, lista_reordenada[j]) )

		# gerando lista com o maior número de caracteres de cada coluna
		lista_max = []
		for j, d in enumerate(tmp_dados[0]):
			maior_nome = max( lista_reordenada[j], key=len )
			nmax = len( maior_nome )
			lista_max.append(nmax)

		# printando as colunas
		if colunas != ():

			# o nome das colunas
			linha = f'| '
			for j, d in enumerate(tmp_dados[0]):
				if alinhamento != ():
					if alinhamento[j] == 'd':
						linha += f'{colunas[j]: >{lista_max[j]+1}} | '
					elif alinhamento[j] == 'c':
						linha += f'{colunas[j]: ^{lista_max[j]+1}} | '
					else:
						linha += f'{colunas[j]: <{lista_max[j]+1}} | '
				else:
					linha += f'{colunas[j]: <{lista_max[j]+1}} | '
			linha = linha[ 0: len(linha) - 1 ]
			print(linha)

			# a linha de baixo
			linha = '|-'
			for j, d in enumerate(tmp_dados[0]):
				nada = ''
				linha += f'{nada:-<{lista_max[j]+1}}-|-'
			linha = linha[ 0: len(linha) - 1 ]
			print(linha)

		# printando os dados da coluna
		for l in dados:
			linha = f'| '
			for j, d in enumerate(tmp_dados[0]):
				rw = str(l[j]).replace('\t', '').replace('\r', '').replace('➜', '>').replace('\n', '$')
				if alinhamento != ():
					if alinhamento[j] == 'd':
						linha += f'{rw: >{lista_max[j]+1}} | '
					elif alinhamento[j] == 'c':
						linha += f'{rw: ^{lista_max[j]+1}} | '
					else:
						linha += f'{rw: <{lista_max[j]+1}} | '
				else:
					linha += f'{rw: <{lista_max[j]+1}} | '
			linha = linha[ 0: len(linha) - 1 ]
			print(linha)

	except Exception as er:
		print('tabela:')
		print(er)

def tabela_texto(colunas=(), alinhamento=(), dados=[], html=False):
	'''Função que cria uma tabela extraida de uma lista e retorna em forma de texto

	Parameters:
		colunas (tuple): Nome das colunas (opcional)
		alinhamento (tuple): Alinhamento de cada coluna (opicional)
		dados (list): Lista com dados para tabela
		html (bool): Se o formato final vai ser HTML

	Returns:
		tabela (str): Tabela em forma de texto para salvar, exibir, etc
	'''
	try:
		txt = ''
		# juntando as colunas pra ver qual o texto maior
		if colunas != ():
			tmp_dados = []
			tmp_dados.append(colunas)
			tmp_dados = tmp_dados + dados.copy()
		else:
			tmp_dados = dados.copy()

		# enfileirando cada coluna em uma lista pra saber quem é maior
		lista_reordenada = []
		for j, d in enumerate(tmp_dados[0]):
			lista_reordenada.append([])

		for j, d in enumerate(tmp_dados[0]):
			for i, l in enumerate(tmp_dados):
				lista_reordenada[j].append(l[j])

		# convertendo tudo para string
		for j, d in enumerate(tmp_dados[0]):
			lista_reordenada[j] = list( map( str, lista_reordenada[j]) )

		# gerando lista com o maior número de caracteres de cada coluna
		lista_max = []
		for j, d in enumerate(tmp_dados[0]):
			maior_nome = max( lista_reordenada[j], key=len )
			nmax = len( maior_nome )
			lista_max.append(nmax)

		# printando as colunas
		if colunas != ():

			# o nome das colunas
			linha = f'| '
			for j, d in enumerate(tmp_dados[0]):
				if alinhamento != ():
					if alinhamento[j] == 'd':
						linha += f'{colunas[j]: >{lista_max[j]+1}} | '
					elif alinhamento[j] == 'c':
						linha += f'{colunas[j]: ^{lista_max[j]+1}} | '
					else:
						linha += f'{colunas[j]: <{lista_max[j]+1}} | '
				else:
					linha += f'{colunas[j]: <{lista_max[j]+1}} | '
			linha = linha[ 0: len(linha) - 1 ]
			txt += linha + '\n'

			# a linha de baixo
			linha = '|-'
			for j, d in enumerate(tmp_dados[0]):
				nada = ''
				linha += f'{nada:-<{lista_max[j]+1}}-|-'
			linha = linha[ 0: len(linha) - 1 ]
			txt += linha + '\n'

		# printando os dados da coluna
		for l in dados:
			linha = f'| '
			for j, d in enumerate(tmp_dados[0]):
				rw = str(l[j]).replace('\t', '').replace('\r', '').replace('➜', '>').replace('\n', '$')
				if alinhamento != ():
					if alinhamento[j] == 'd':
						linha += f'{rw: >{lista_max[j]+1}} | '
					elif alinhamento[j] == 'c':
						linha += f'{rw: ^{lista_max[j]+1}} | '
					else:
						linha += f'{rw: <{lista_max[j]+1}} | '
				else:
					linha += f'{rw: <{lista_max[j]+1}} | '
			linha = linha[ 0: len(linha) - 1 ]
			txt += linha + '\n'

		if html:
			txt = '<style>.py_tabela{border:0px;margin:0px;padding:0px;font-family: courier; font-size:14px;white-space: nowrap;}</style><div class=py_tabela>' + txt.replace(' ', '&nbsp;').replace('\n', '<br>') + '</div>'

		return txt

	except Exception as er:
		print('tabela:')
		print(er)
