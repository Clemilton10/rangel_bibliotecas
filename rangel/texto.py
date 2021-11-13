import unidecode
import json
import re

def formatar(tx, j) -> str:
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

def texNum(indice) -> int:
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

def limpar(t) -> str:
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
		return t
	except Exception as er:
		print('limpar:')
		print(er)
		return original

def comparar(a, b) -> float:
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
