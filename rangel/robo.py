# python -m pip install Pillow
# python -m pip install opencv-python

import pyautogui as pa
import pyperclip as pc
from time import sleep
import pyttsx3
#from os.path import dirname, realpath #, abspath
#from sys import platform
from pynput import mouse

class robo:
	pa = None
	pc = None
	teclar = None
	pressionar = None
	clicar = None
	boca = None
	xy = [0, 0]

	def __init__(self):
		'''Classe que automatiza tarefas assumindo o teclado e mouse

		Variables:
			pa (pyautogui): Biblioteca que assume o teclado e mouse
			pc (pyperclip): Biblioteca que em casos de caracteres especiais que o pyautogui não consegue digitar, substitui copiando e colando
			teclar (function): Função que serve para presionar e soltar uma ou mais teclas combinadas
			pressionar (function): Função que serve para pressionar uma tecla
			clicar (function): Função que serve para clicar em uma coordenada
			boca (pyttsx3): Driver para reproduzir a fala humana
			xy (list): Lista de coordenadas (x e y)
		'''
		try:
			self.pa = pa
			self.pc = pc

			#self.pwd = dirname( abspath(__file__) )
			#self.pwd = dirname( realpath(__file__) )
			#if platform == 'win32':
			#	self.pwd = self.pwd + '\\'
			#else:
			#	self.pwd = self.pwd + '/'

			self.teclar = self.pa.hotkey
			self.pressionar = self.pa.press
			self.clicar = self.pa.click

			self.boca = pyttsx3.init(driverName='sapi5')
			#boca = pyttsx3.init('dummy')
			vozes = self.boca.getProperty('voices')

			voz_id = 0
			for i, voz in enumerate(vozes):
				'''
				print(i)
				print(voz.name)
				print(voz.id)
				print()
				'''
				if 'maria' in voz.name.lower():
					voz_id = voz.id

			self.boca.setProperty('voice', voz_id)
			self.boca.setProperty('rate', 200 )
			self.boca.setProperty('volume', 1. )

		except Exception as er:
			print('robo.init:')
			print(er)

	def ajuda(self):
		print()
		print('--- Bibliotecas obrigatórias ---')
		print('python -m pip install Pillow')
		print('python -m pip install opencv-python')
		print()
		print('--- Funções disponíveis ---')
		print('r = robo()')
		print('r.tempo(5)')
		print('r.tempo_voz(5)')
		print('r.falar(\'texto para falar\')')
		print('r.teclar(\'win\', \'2\')')
		print('r.pressionar(\'enter\')')
		print('r.digitar(\'http://www.google.com.br\')')
		print('r.posicao_imagem(\'imagem.png\')')
		print('r.mover(500, 300)')
		print('r.mover_clicar(500, 300)')
		print('r.clicar(500, 300)')
		print('r.clicar_direito(500, 300)')
		print('p = r.posicao(12)')
		print('r.ap_bt_esquerdo()')
		print('r.st_bt_esquerdo()')
		print('r.ap_bt_direito()')
		print('r.st_bt_direito()')
		print()
		print('r.capturar_click()')
		print('p = r.xy')
		print()

	def clicar_direito(self, x: float, y: float):
		'''Função que assume o mouse e clica com botão direito nas coordenadas

		Parameters:
			x (float): Posição X para o clique
			y (float): Posição Y para o clique
		'''
		try:
			self.pa.click(x=x, y=y, button='right')
		except Exception as er:
			print('robo.clicar_direito:')
			print(er)

	def falar(self, fala: str):
		'''Função que simula a fala humana

		Parameters:
			fala (str): Texto para ser narrado
		'''
		try:
			self.boca.say(fala)
			self.boca.runAndWait()
		except Exception as er:
			print('robo.falar:')
			print(er)

	def tempo_voz(self, qtd_vezes: int):
		'''Função que narra e espera alguns segundos antes da próxima tarefa

		Parameters:
			qtd_vezes (int): Quantidade de segundos que o programa vai esperar e narrar
		'''
		try:
			for i in range(1, qtd_vezes + 1):
				print(i)
				self.falar(str( i ))
		except Exception as er:
			print('robo.tempo:')
			print(er)

	def tempo(self, qtd_vezes: int):
		'''Função que espera alguns segundos antes da próxima tarefa

		Parameters:
			qtd_vezes (int): Quantidade de segundos que o programa vai esperar e narrar
		'''
		try:
			for i in range(1, qtd_vezes + 1):
				print(i)
				sleep(1)
		except Exception as er:
			print('robo.tempo:')
			print(er)

	def digitar(self, texto: str):
		'''Função que assume o teclado e digita o texto

		Parameters:
			texto (str): Texto a ser digitado
		'''
		try:
			antes = 'x'
			lista = []
			x = 0
			letras_problematicas = 'àèìòùÀÈÌÒÙáéíóúýÁÉÍÓÚÝâêîôûÂÊÎÔÛãñõÃÑÕäëïöüÿÄËÏÖÜŸçÇ'
			for i in range( len( texto ) ):
				if \
				(texto[i].isalnum() or \
				texto[i] == ' ' or \
				texto[i] == '.') and \
				not texto[i] in letras_problematicas:
					agora = 't'
				else:
					agora = 'e'

				if agora == 'e':
					lista.append({'t': agora, 'v': texto[i]})
					x += 1
				else:
					if antes == 'e' or antes == 'x':
						lista.append({'t': agora, 'v': texto[i]})
						x += 1
					else:
						lista[x - 1]['v'] += texto[i]
						pass
				antes = agora
			for tx in lista:
				if tx['t'] == 't':
					self.pa.typewrite(tx['v'], interval=0.02)
				else:
					self.pc.copy(tx['v'])
					self.pa.hotkey('ctrl', 'v')
		except Exception as er:
			print('digitar:')
			print(er)

	def posicao_imagem(self, im: str, q_vezes: int)->list:
		'''Função que busca a posição central de uma imagem na tela

		Parameters:
			im (str): Caminho da imagem a ser procurada
			q_vezes (int): Quantidade de tentativas

		Returns:
			posicao (list): Coordenadas [X, Y]
		'''
		try:
			procurar_imagem = True
			i = [-1 , -1]
			x = 0
			while procurar_imagem and x < q_vezes:
				try:
					print(f'procurando... tentativa {x + 1}')
					i = self.pa.locateCenterOnScreen(
						image = im,
						#region = (0, 0, 1920, 1080),
						grayscale = True,
						confidence = 0.8
					)
					if i:
						procurar_imagem = False
						i = list(i)
						x = 1000
						break
					else:
						i = [-1, -1]
				except Exception as er:
					print('robo.posicao_imagem.while:')
					print(er)
					x += 1
					sleep( 1 )
				finally:
					x += 1
					sleep( 1 )
			return i
		except Exception as er:
			print('robo.posicao_imagem:')
			print(er)
			return [-1, -1]

	def mover(self, x: float, y: float):
		'''Função que assume o mouse e reposiciona nas coordenadas

		Parameters:
			x (float): Posição X
			y (float): Posição Y
		'''
		try:
			self.pa.moveTo(x=x, y=y, duration=0.2)
		except Exception as er:
			print('robo.mover:')
			print(er)

	def mover_clicar(self, x: float, y: float):
		'''Função que assume o mouse, reposiciona nas coordenadas e clica

		Parameters:
			x (float): Posição X
			y (float): Posição Y
		'''
		try:
			self.pa.moveTo(x=x, y=y, duration=0.2)
			self.pa.click(x=x, y=y)
		except Exception as er:
			print('robo.mover:')
			print(er)

	def posicao(self, q_vezes: int)->list:
		'''Função que espera um certo tempo e pega a posição em que o mouse estiver

		Parameters:
			q_vezes (int): Quantidade de segundos que deve narrar e esperar antes de pegar a posição

		Returns:
			posicao (list): Posição do mouse [X, Y]
		'''
		try:
			self.tempo_voz(q_vezes)
			p = self.pa.position()
			p = list(p)
			return p
		except Exception as er:
			print('robo.posicao:')
			print(er)
			return [0, 0]

	def ap_bt_esquerdo(self):
		'''Função que assume o mouse, clica com botão esquerdo e o mantém pressionado'''
		try:
			self.pa.mouseDown()
		except Exception as er:
			print('robo.ap_bt_esquerdo:')
			print(er)

	def st_bt_esquerdo(self):
		'''Função que assume o mouse, e solta o botão esquerdo pressionado'''
		try:
			self.pa.mouseUp()
		except Exception as er:
			print('robo.st_bt_esquerdo:')
			print(er)

	def ap_bt_direito(self):
		'''Função que assume o mouse, clica com botão direito e o mantém pressionado'''
		try:
			self.pa.mouseDown(button='right')
		except Exception as er:
			print('robo.ap_bt_direito:')
			print(er)

	def st_bt_direito(self):
		'''Função que assume o mouse, e solta o botão direito pressionado'''
		try:
			self.pa.mouseUp(button='right')
		except Exception as er:
			print('robo.st_bt_direito:')
			print(er)

	def on_click(self, x, y, button, pressed):
		'''Função que pega o evento de clique do botão esquerdo do mouse e armazena em self.xy'''
		try:
			if button == mouse.Button.left:
				self.xy = [x, y]
			return False
		except Exception as er:
			print('robo.on_click:')
			print(er)
			return False

	def capturar_click(self):
		'''Função que inicia a escuta dos cliques com botão esquerdo do mouse para armazenar em self.xy'''
		try:
			self.falar('Clique na posição')
			self.xy = [0, 0]
			listener = mouse.Listener(on_click=self.on_click)
			listener.start()
			listener.join()
		except Exception as er:
			print('robo.capturar_click:')
			print(er)
			self.falar('Não consegui pegar')
		finally:
			self.falar('Capturei a posição')

