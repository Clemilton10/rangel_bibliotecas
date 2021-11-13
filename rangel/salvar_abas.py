# extensao TabCopy

from sys import argv
from os.path import splitext
from os import system, remove
from rangel.arquivo import *
from rangel.dicionario import *

def txt_json(arquivo):
	try:
		nome, ext = splitext(arquivo)
		texto = ler_arquivo(arquivo)
		s = texto.split('\n')
		t = 'x'
		l = []
		x = 0
		for i in s:
			if t == 'x':
				l.append({'titulo': i, 'link': ''})
				t = 't'
				x += 1
			elif t == 't':
				l[x - 1]['link'] = i
				t = 'l'
			else:
				t = 'x'
		salvar_json(nome + '.json', l)
	except Exception as er:
		print('txt_json:')
		print(er)

def json_html(arquivo):
	try:
		nome, ext = splitext(arquivo)
		js = ler_json(nome + '.json')
		tx = ''
		for x, i in enumerate(js):
			tx += f'<div>{x} - {i["titulo"]}</div>\n'
			tx += f'<a name="lk{x}" href="{i["link"]}" style="display: block;">{i["link"]}</a>\n'
			tx += '<br>\n\n'
		remove(nome + '.json')
		salvar_arquivo(nome + '.html', tx)
		system(nome + '.html')
	except Exception as er:
		print('txt_json:')
		print(er)

# chama a função se executar este arquivo, não como biblioteca
if __name__ == "__main__":
	sa = salvar_abas(argv[1])