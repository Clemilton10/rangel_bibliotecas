import json
import pandas as pd

def visualizar(arquivo, separador, tx):
	try:
		# dataframe
		df = pd.read_csv(arquivo, sep=separador)

		if tx:
			jstmp = []
			js = json.loads(tx)
			colunas = list(df.keys())
			if 'indice' in js and js['indice']:
				for i, d in enumerate(df.iterrows()):
					if i == int( js['indice'] ):
						jstmp = [{}]
						for col in colunas:
							try:
								jstmp[0][col] = df.at[i, col]
							except:
								pass
			else:
				x = 0
				campos = js.keys()
				for i, d in enumerate(df.iterrows()):
					adicionar = False
					for c in campos:
						busca = js[c].replace('=','').replace('%','').strip().lower()
						pi = js[c].find('=')
						pp = js[c].find('%')
						if \
						c != 'indice' and \
						(pi == 0 or pp == 0) and \
						busca:
							if pi == 0 and busca == df.at[i, c].lower():
								adicionar = True
							elif pp == 0 and busca in df.at[i, c].lower():
								adicionar = True
							else:
								pass
					if adicionar:
						jstmp.append({})
						for col in colunas:
							try:
								jstmp[x][col] = df.at[i, col]
							except:
								pass
						x += 1
			df = pd.json_normalize(jstmp)

		# string
		st = df.to_json(orient='records')

		# dicionario
		js = json.loads(st)
		for i, j in enumerate(js):
			j['indice'] = i

		return js
	except Exception as er:
		print('visualizar:')
		print(er)
		return []

def adicionar(arquivo, separador, tx):
	try:
		js  = json.loads(tx)
		df2 = pd.json_normalize(js)
		df1 = pd.read_csv(arquivo, sep=separador)
		df1 = pd.concat([df1, df2])
		df1.to_csv(arquivo, index=None, header=True, sep=separador)
		return {'sucesso': 1}
	except Exception as er:
		print('adicionar:')
		print(er)
		return {'sucesso': 0, 'erro': er}

def editar(arquivo, separador, tx):
	try:
		js  = json.loads(tx)
		df = pd.read_csv(arquivo, sep=separador)
		colunas = list(df.keys())
		for i, d in enumerate(df.iterrows()):
			if i == int( js['indice'] ):
				for col in colunas:
					try:
						df.at[i, col] = js[col]
					except:
						pass
		df.to_csv(arquivo, index=None, header=True, sep=separador)
		return {'sucesso': 1}
	except Exception as er:
		print('editar:')
		print(er)
		return {'sucesso': 0, 'erro': er}

def excluir(arquivo, separador, tx):
	try:
		js  = json.loads(tx)
		df = pd.read_csv(arquivo, sep=separador)
		df = df.drop( int( js['indice'] ) )
		df.to_csv(arquivo, index=None, header=True, sep=separador)
		return {'sucesso': 1}
	except Exception as er:
		print('excluir:')
		print(er)
		return {'sucesso': 0, 'erro': er}
