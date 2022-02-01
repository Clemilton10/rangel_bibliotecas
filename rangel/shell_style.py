import ctypes;
kernel32 = ctypes.WinDLL('kernel32');
hStdOut = kernel32.GetStdHandle(-11);
mode = ctypes.c_ulong();
kernel32.GetConsoleMode(hStdOut, ctypes.byref(mode));
mode.value |= 4;
kernel32.SetConsoleMode(hStdOut, mode)

class shell_style:
	ESC = '\x1b['

	# Cor da Fonte (Foreground)
	CF_PRETA    = f'{ESC}30m'
	CF_BRANCA   = f'{ESC}37m'
	CF_AMARELA  = f'{ESC}93m'
	CF_MAGENTA  = f'{ESC}95m'
	CF_AZUL     = f'{ESC}94m'
	CF_VERDE    = f'{ESC}92m'
	CF_VERMELHA = f'{ESC}91m'
	CF_CIANO    = f'{ESC}96m'

	# Fundos (Background)
	FD_PRETA    = f'{ESC}100m'
	FD_BRANCA   = f'{ESC}107m'
	FD_AMARELA  = f'{ESC}103m'
	FD_MAGENTA  = f'{ESC}105m'
	FD_AZUL     = f'{ESC}104m'
	FD_VERDE    = f'{ESC}102m'
	FD_VERMELHA = f'{ESC}101m'
	FD_CIANO    = f'{ESC}106m'

	# Efeitos
	UNDERLINE   = f'{ESC}4m'
	ITALICO     = f'{ESC}3m'
	NEGRITO     = f'{ESC}1m'
	SLOW_BLINK  = f'{ESC}5m'
	RAPID_BLINK = f'{ESC}6m'

	# Ícones
	PLACA         = '⚠'
	TRIANGULO1    = '▲'
	TRIANGULO2    = '∆'
	XIS           = '✖'
	LAPIS         = '✎'
	CHECADO       = '✔'
	RAIZ_QUADRADA = '√'
	MENOR_MENOR   = '«'
	MAIOR_MAIOR   = '»'
	AO_QUADRADO   = '²'
	ALFA          = 'α'
	BETA          = 'β'
	OMEGA         = 'Ω'
	TIL           = '∼'
	ENTER         = '↳'
	TAB           = '⇄'
	SETA1         = '➝'
	SETA2         = '➜'
	SETA3         = '➞'
	SETA4         = '⇒'
	SETA5         = '➼'
	SETA6         = '➤'
	TECLADO       = '⌨'
	RELOGIO       = '⌚'
	AMPULIETA     = '⌛'
	TELEFONE      = '☎'
	FERRAMENTAS   = '⚒'
	CAMINHAO      = '⛟'
	AVIAO         = '✈'
	CARTA         = '✉'
	DIAMENTE      = '❖'
	LOZANGULO     = '⬧'
	MAO           = '☛'
	SUSTENIDO     = '♯'

	# Status
	ALERTA     = f'{CF_AMARELA}{PLACA} '
	ERRO       = f'{CF_VERMELHA}{XIS} '
	PERGUNTA   = f'{CF_CIANO}{LAPIS} '
	FINALIZADO = f'{CF_VERDE}{CHECADO} '

	# Reset
	NONE = f'{ESC}0m'

	def __init__(self):
		'''Classe para tratar de cores e estilos para o Shell

		Variables (str):
			ESC

			# Cor da Fonte (Foreground)
			CF_PRETA
			CF_BRANCA
			CF_AMARELA
			CF_MAGENTA
			CF_AZUL
			CF_VERDE
			CF_VERMELHA
			CF_CIANO

			# Fundos (Background)
			FD_PRETA
			FD_BRANCA
			FD_AMARELA
			FD_MAGENTA
			FD_AZUL
			FD_VERDE
			FD_VERMELHA
			FD_CIANO

			# Efeitos
			UNDERLINE
			ITALICO
			NEGRITO
			SLOW_BLINK
			RAPID_BLINK

			# Ícones
			PLACA         ⚠
			TRIANGULO1    ▲
			TRIANGULO2    ∆
			XIS           ✖
			LAPIS         ✎
			CHECADO       ✔
			RAIZ_QUADRADA √
			MENOR_MENOR   «
			MAIOR_MAIOR   »
			AO_QUADRADO   ²
			ALFA          α
			BETA          β
			OMEGA         Ω
			TIL           ∼
			ENTER         ↳
			TAB           ⇄
			SETA1         ➝
			SETA2         ➜
			SETA3         ➞
			SETA4         ⇒
			SETA5         ➼
			SETA6         ➤
			TECLADO       ⌨
			RELOGIO       ⌚
			AMPULIETA     ⌛
			TELEFONE      ☎
			FERRAMENTAS   ⚒
			CAMINHAO      ⛟
			AVIAO         ✈
			CARTA         ✉
			DIAMENTE      ❖
			LOZANGULO     ⬧
			MAO           ☛
			SUSTENIDO     ♯

			# Status
			ALERTA
			ERRO
			PERGUNTA
			FINALIZADO

			# Reset
			NONE
		'''
		pass

	def extrair_tupla(self, t: tuple, s: str)->str:
		'''Converte uma Tupla para String concatenando um separador

		Parameters:
			t (tuple): Tupla que vai ser convertida
			s (str): Separador que vai entre cada item da tupla

		Returns:
			resposta (str): String gerada a partir da Tupla
		'''
		try:
			lst = []
			for i in range( len( t ) ):
				lst.append( t[i] )
			return s.join( map( str, lst ) )
		except Exception as er:
			print('shell_style.extrair_tupla:')
			print(er)
			return ''

	def print(self, *args, cor='', efeito='', sep=' ', end='\n', file=None, flush=False):
		'''Função que substirui a função print nativa

		Parameters:
			args (args): Múltiplos argumentos indiduais
			cor (str): Cor da letra
			efeito (str): Efeito para o texto (negrito, italico, etc)
			Sep (str): Separador
			end (str): Texto para o final
			file (str): Arquivo para escrever texto
			flush (bool): Força o print em tempo real

		Returns:
			print (function): Nova função print
		'''
		try:
			texto = self.extrair_tupla( args, sep )
			return print(f'{cor}{efeito}{texto}{self.NONE}', sep=sep, end=end, file=file, flush=flush)
		except Exception as er:
			print('shell_style.print:')
			print(er)

	def input(self, texto, cor='', efeito='', br='\n➤ '):
		'''Função que substitui a função input nativa

		Parameters:
			texto (str): Texto que fará a descrição do input
			cor (str): Cor da letra
			efeito (str): Efeito para o texto (negrito, italico, etc)
			br (str): texto que vai antes da digitação do input
		Returns:
			input (function): Nova função input
		'''
		try:
			return input(f'{cor}{efeito}{texto}{br}{self.NONE}')
		except Exception as er:
			print('shell_style.input:')
			print(er)

	def erro(self, funcao: str, tx_erro: str):
		'''Função que trata os erros colorindo

		Parameters:
			funcao (str): Nome da função que deu erro
			tx_erro (str): Texto do erro
		'''
		try:
			self.print(f'{ss.FD_VERMELHA}{ss.CF_BRANCA} {funcao} {ss.NONE}')
			self.print(tx_erro, cor=ss.CF_VERMELHA)
		except Exception as er:
			print('shell_style.erro:')
			print(er)
