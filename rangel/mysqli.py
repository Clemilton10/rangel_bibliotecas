# pip install mysql-connector-python

import mysql.connector
from mysql.connector import FieldType
from json import loads, dumps

class mysqli:
	host     = 'localhost'
	user     = 'root'
	passwd   = ''
	database = ''

	def __init__(self):
		'''Classe para conversar com banco de dados MySQL

		Variables:
			host (str): url do MySQL
			user (str): usuário do banco de dados
			passwd (str): senha do bando de dados
			database (str): nome do banco de dados
		'''
		pass

	def ler_arquivo(self, arquivo: str)->str:
		'''Função que lê um arquivo

		Parameters:
			arquivo (str): nome do arquivo a ser lido

		Returns:
			texto (str): texto do arquivo lido
		'''
		try:
			f = open(arquivo, 'r', encoding='utf8');
			t = f.read();
			f.close();
			return t
		except Exception as er:
			print('ler_arquivo:')
			print(er)
			return ''

	def ler_json(self, arquivo: str):
		'''Função que lê um arquivo e converte para um dicionario ou uma lista de dicionários

		Parameters:
			arquivo (str): nome do arquivo a ser lido

		Returns:
			lista (dict/list): Dicionário ou lista de dicionário
		'''
		try:
			tx = self.ler_arquivo(arquivo)
			js = loads(tx)
			return js
		except Exception as er:
			print('ler_json:')
			print(er)
			return []

	def carregar_configuracoes(self):
		'''Função que lê automaticamente o arquivo com as configurações do banco'''
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
		'''Função que conecta ao banco de dados'''
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

	def squery(self, sql: str)->dict:
		'''Função que executa uma consulta (select)

		Parameters:
			sql (str): SQL para consultar (select)

		Returns:
			dicionario (dict): {}
				sql (str): SQL para consultar (select)
				colunas (str): Nome das colunas obitidas
				linhas (list): Lista com registros encontrados
				sucesso (bool): Se a consulta ocorrer sem problema retorna True
		'''
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

	def equery(self, sql: str)->dict:
		'''Função que serve para executar ações no banco de dados (insert, update, delete)

		Parameters:
			sql (str): SQL para executar ações no banco de dados (insert, update, delete)

		Returns:
			dicionario (dict): {}
				sql: SQL para executar ações no banco de dados (insert, update, delete)
				sucesso (bool): Se a ação ocorrer sem problema retorna True
		'''
		try:
			self.cursor.execute(sql)
			self.db.commit()
			return {'sql': sql, 'sucesso': True}
		except Exception as er:
			print('squery:')
			print(er)
			return {'sql': sql, 'sucesso': False}

	def vquery(self, sql: str, val: tuple)->dict:
		'''Função que serve para executar ações no banco de dados (insert, update, delete) passando valores separados

		Parameters:
			sql (str): SQL para executar ações no banco de dados (insert, update, delete)
				"INSERT INTO usuario (nome, email) VALUES (%s, %s)"
			val (tuple): Tupla com valores para ação
				("clemas", "clemas.web@gmail.com")

		Returns:
			dicionario (dict): {}
				sql: SQL para executar ações no banco de dados (insert, update, delete)
				sucesso (bool): Se a ação ocorrer sem problema retorna True
		'''
		try:
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