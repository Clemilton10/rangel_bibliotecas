import unidecode
import json
import re

def formatar(tx: str, j: 'dict {tirarLetras (str), maiusculo (str), minusculo (str), tirarNumeros (str), manterCaracteres}') -> str:
	'''Trata uma string

	Parameters:
		j (dict): {}
			j['tirarLetras'] (str): retira todas as letras
			j['maiusculo'] (str): converte a string para maiúsculo
			j['minusculo'] (str): converte a string para minúsculo
			j['tirarNumeros'] (str): retira todos os números
			j['manterCaracteres'] (str): todos os caracteres que não forem informados serão retirados com exceção de letras e números que devem ser informados como descrito acima

	Returns:
		resultado (str): retorna a string tratada/convertida
	'''
	st = str(tx);
	if not 'tirarLetras' in j or not j['tirarLetras']:
		if not 'manterAcentos' in j or not j['manterAcentos']:
			st = u'{}'.format(st)
			st = unidecode.unidecode(st)

		if 'maiusculo' in j and j['maiusculo']:
			st = st.upper()

		if 'minusculo' in j and j['minusculo']:
			st = st.lower()
	else:
		st = u'{}'.format(st)
		st = unidecode.unidecode(st)
		st = re.sub(r'([a-zA-Z])', r'', st)

	if 'tirarNumeros' in j and j['tirarNumeros']:
		st = re.sub(r'([0-9])', r'', st)

	kr = [
		"'",'-','=',']','"','!','@','#','$','%','¨','&',
		'*','(',')','_','+','}','¹','²','³','£','¢','¬',
		'§','º','`','{','?','^',':','>','<','|','´','[',
		'~','/',';','.',',','\\','°','ª',"\n","\t","\r"," "
	]

	if 'manterCaracteres' in j:
		for i in range(len(kr)):
			if not kr[i] in j['manterCaracteres']:
				st = st.replace(kr[i], '')
	else:
		for i in range(len(kr)):
			st = st.replace(kr[i], '')

	return st

def texNum(indice: str) -> int:
	'''Converte um número por extenso para um inteiro

	Parameters:
		indice (str): numero por extenso que vai se tornar um inteiro

	Returns:
		resultado (int): numero inteiro convertido
	'''
	try:
		indice = indice.strip()
		if indice.isalpha():
			nums = {
				'zero': 0,
				'um': 1,
				'dois': 2,
				'tres': 3,
				'quatro': 4,
				'cinco': 5,
				'seis': 6,
				'sete': 7,
				'oito': 8,
				'nove': 9,
				'dez': 10,
				'onze': 11,
				'doze': 12,
				'treze': 13,
				'catorze': 14,
				'quatorze': 14,
				'quinze': 15,
				'dezeseis': 16,
				'dezessete': 17,
				'dezoito': 18,
				'dezenove': 19,
				'vinte': 20
			}
			indice = nums[indice]
		else:
			indice = int( indice )
		return indice
	except Exception as er:
		print('texNum:')
		print(er)
		return 0

def limpar(t: str) -> str:
	'''Retira as conjuções para deixar o texto limpo para comparações

	Parameters:
		t (str): texto cru

	Returns:
		resultado (str): texto limpo sem (e, a, o, as, os, do, da, de, no, na, em)
	'''
	original = t
	try:
		t = formatar(t, {'minusculo': True, 'manterCaracteres': '|:; '})
		t = t.strip()
		t = t.replace(' e ', ' ')
		t = t.replace(' a ', ' ')
		t = t.replace(' o ', ' ')
		t = t.replace(' as ', ' ')
		t = t.replace(' os ', ' ')
		t = t.replace(' do ', ' ')
		t = t.replace(' da ', ' ')
		t = t.replace(' de ', ' ')
		t = t.replace(' no ', ' ')
		t = t.replace(' na ', ' ')
		t = t.replace(' em ', ' ')

		if \
		t.find('e ') == 0 or \
		t.find('a ') == 0 or \
		t.find('o ') == 0 or \
		t.find('as ') == 0 or \
		t.find('os ') == 0 or \
		t.find('do ') == 0 or \
		t.find('da ') == 0 or \
		t.find('de ') == 0 or \
		t.find('no ') == 0 or \
		t.find('na ') == 0 or \
		t.find('em ') == 0:
			l = len(t)
			p = t.find(' ')
			t = t[ p + 1 : l - (p + 1) ]

		if \
		t.rfind(' e') >- 1 or \
		t.rfind(' a') >- 1 or \
		t.rfind(' o') >- 1 or \
		t.rfind(' as') >- 1 or \
		t.rfind(' os') >- 1 or \
		t.rfind(' do') >- 1 or \
		t.rfind(' da') >- 1 or \
		t.rfind(' de') >- 1 or \
		t.rfind(' no') >- 1 or \
		t.rfind(' na') >- 1 or \
		t.rfind(' em') >- 1:
			p = t.rfind(' ')
			t = t[ 0 : p ]

		return t
	except Exception as er:
		print('limpar:')
		print(er)
		return original

def comparar(a: str, b: str) -> float:
	'''Percorre o texto, palavra por palavra verificando se são iguais, retorna o percentual de similaridade

	Parameters:
		a (str): primeiro texto a ser comparado
		b (str): segundo texto a ser comparado

	Returns:
		percentual (float): percentual de similaridade de uma string com a outra
	'''
	try:
		a  = limpar(a)
		b  = limpar(b)
		sa = a.split(' ')
		sb = b.split(' ')
		lb = len(sb)
		la = 0
		for va in sa:
			if va in sb:
				la += 1
		# lb = 100
		# la = ?
		pc = (la * 100) / lb
		return pc
	except Exception as er:
		print('comparar:')
		print(er)
		return 0
