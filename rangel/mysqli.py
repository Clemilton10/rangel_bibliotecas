# pip install mysql-connector-python

import mysql.connector
from mysql.connector import FieldType
from json import loads, dumps

class mysqli:
	host     = 'localhost'
	user     = 'root'
	passwd   = ''
	database = ''

	def ler_arquivo(self, arquivo):
		try:
			f = open(arquivo, 'r', encoding='utf8');
			t = f.read();
			f.close();
			return t
		except Exception as er:
			print('ler_arquivo:')
			print(er)
			return ''

	def ler_json(self, arquivo):
		try:
			tx = self.ler_arquivo(arquivo)
			js = loads(tx)
			return js
		except Exception as er:
			print('ler_json:')
			print(er)
			return []

	def carregar_configuracoes(self):
		try:
			js = self.ler_json('mysqli_configuracoes.json')
			self.host     = js['host']
			self.user     = js['user']
			self.passwd   = js['passwd']
			self.database = js['database']
		except Exception as er:
			print('carregar_configuracoes:')
			print(er)
			return []

	def conectar(self):
		try:
			self.db  = mysql.connector.connect(
				host     = self.host,
				user     = self.user,
				passwd   = self.passwd,
				database = self.database
			)
			self.cursor = self.db.cursor(dictionary = True)
		except Exception as er:
			print('conectar:')
			print(er)

	def squery(self, sql):
		try:
			self.cursor.execute(sql)
			rs = self.cursor.fetchall()
			js = {'sql': sql, 'colunas': [],'linhas': [], 'sucesso': True}
			for i in range(len(self.cursor.description)):
				desc         = self.cursor.description[i]
				nome         = desc[0]
				q_caracteres = desc[1]
				tipo         = FieldType.get_info(desc[1])
				js['colunas'].append(
					{
						'nome:'       : nome,
						'q_caracteres': q_caracteres,
						'tipo:'       : tipo
					}
				)
			for i, r in enumerate(rs):
				js['linhas'].append({})
				for desc in self.cursor.description:
					nome = desc[0]
					js['linhas'][i][nome] = r[nome]
			return js
		except Exception as er:
			print('squery:')
			print(er)
			return {'sql': sql, 'colunas': [],'linhas': [], 'sucesso': False}

	def equery(self, sql):
		try:
			self.cursor.execute(sql)
			self.db.commit()
			return {'sql': sql, 'sucesso': True}
		except Exception as er:
			print('squery:')
			print(er)
			return {'sql': sql, 'sucesso': False}

	def vquery(self, sql, val):
		try:
			# sql = "INSERT INTO usuario (nome, email) VALUES (%s, %s)"
			# val = ("clemas", "clemas.web@gmail.com")
			self.cursor.execute(sql, val)
			self.db.commit()
			return {'sql': sql, 'valores': val, 'sucesso': True}
		except Exception as er:
			print('vquery:')
			print(er)
			return {'sql': sql, 'valores': val, 'sucesso': False}

	def fechar_cursor(self):
		self.cursor.close();

	def fechar_db(self):
		self.db.close();

'''
m = mysqli()
m.host     = 'localhost'
m.user     = 'root'
m.passwd   = '******'
m.database = 'db'
m.carregar_configuracoes()
m.conectar()
rs = m.squery('select * from acao')
print(rs)
m.equery('insert into acao(nome) values ("TESTE")')
rs = m.squery('select * from acao')
print(rs)
m.fechar_cursor()
m.fechar_db()
'''