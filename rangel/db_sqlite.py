import sqlite3
class db_sqlite():
	cx = None
	cursor = None
	colunas = [];

	def __init__(self):
		'''Classe que conversa com banco de dados SQLite

		Variables:
			cx (connection): Objeto de conexão com o banco de dados
			cursor (cursor): Objeto que interage com o banco de dados
			colunas (list): Nome das colunas quando é feita uma consulta (select)
		'''
		pass

	def conectar(self, arquivo: str):
		'''Função que conecta a um banco de dados (arquivo.db)

		Parameters:
			arquivo (str): Nome do arquivo (banco de dados)
		'''
		try:
			#con = sqlite3.connect(":memory:")
			self.cx = sqlite3.connect(arquivo)
			self.cursor = self.cx.cursor()
		except Exception as er:
			print('db.conectar:')
			print(er)

	def query(self, sql: str):
		'''Função que consulta ou executa uma ação no banco de dados

		Parameters:
			sql (str): SQL consulta ou executa uma ação no banco de dados

		Returns:
			lista (list): Em caso de ação (insert, update, delete) retorna [] caso contrário, retorna uma lista com os registros encontrados e armazena o nome das colunas na variável self.colunas
		'''
		try:
			if sql.lower().find('select') > -1 and sql.lower().find('select') <= 1:
				rs = self.cursor.execute(sql)
				self.colunas = [description[0] for description in self.cursor.description]
				tmp = []
				for i, r in enumerate(rs):
					tmp.append({})
					for j, n in enumerate(self.colunas):
						tmp[i][j] = r[j]
						tmp[i][n] = r[j]
				rs = tmp
				return rs
			else:
				rs = self.cursor.execute(sql)
				self.cx.commit()
				return []
		except Exception as er:
			print('db.query:')
			print(er)
			return []