class db_sqlite():
	cx = None
	cursor = None
	colunas = [];

	def conectar(self, arquivo):
		try:
			#con = sqlite3.connect(":memory:")
			self.cx = sqlite3.connect(arquivo)
			self.cursor = self.cx.cursor()
		except Exception as er:
			print('db.conectar:')
			print(er)

	def query(self, sql):
		try:
			if sql.lower().find('select') <= 1:
				rs = c.execute(sql)
				self.colunas = [description[0] for description in c.description]
				tmp = []
				for i, r in enumerate(rs):
					tmp.append({})
					for j, n in enumerate(self.colunas):
						tmp[i][j] = r[j]
						tmp[i][n] = r[j]
				rs = tmp
				return rs
			else:
				rs = c.execute(sql)
				return True
		except Exception as er:
			print('db.conectar:')
			print(er)
			return False