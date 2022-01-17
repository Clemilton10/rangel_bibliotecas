class arquivos:

	def ajuda():
		print()
		print('a = arquivos()')
		print('a.ler_arquivo(\'arquivo.txt\')')
		print('a.salvar_arquivo(\'arquivo.txt\', \'texto a ser salvo\')')
		print()

	def ler_arquivo(self, arquivo) -> str:
		try:
			f = open(arquivo, 'r', encoding='utf8')
			t = f.read()
			f.close()
			return t
		except Exception as er:
			print('arquivos.ler_arquivo:')
			print(er)
			return ''

	def salvar_arquivo(self, arquivo, texto):
		try:
			f = open(arquivo, 'w', encoding='utf8')
			f.writelines(texto)
			f.close()
		except Exception as er:
			print('arquivos.salvar_arquivo:')
			print(er)