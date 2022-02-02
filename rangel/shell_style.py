from sys import platform
if 'win' in platform:
	import ctypes;
	kernel32 = ctypes.WinDLL('kernel32');
	hStdOut = kernel32.GetStdHandle(-11);
	mode = ctypes.c_ulong();
	kernel32.GetConsoleMode(hStdOut, ctypes.byref(mode));
	mode.value |= 4;
	kernel32.SetConsoleMode(hStdOut, mode)

class shell_style:

	# Cor da Fonte (Foreground)
	CF_PRETA    = f'\033[30m'
	CF_VERMELHA = f'\033[31m'
	CF_VERDE    = f'\033[32m'
	CF_AMARELA  = f'\033[33m'
	CF_AZUL     = f'\033[34m'
	CF_MAGENTA  = f'\033[35m'
	CF_CIANO    = f'\033[36m'
	CF_BRANCA   = f'\033[37m'

	CFB_PRETA    = f'\033[90m'
	CFB_VERMELHA = f'\033[91m'
	CFB_VERDE    = f'\033[92m'
	CFB_AMARELA  = f'\033[93m'
	CFB_AZUL     = f'\033[94m'
	CFB_MAGENTA  = f'\033[95m'
	CFB_CIANO    = f'\033[96m'
	CFB_BRANCA   = f'\033[97m'

	# Fundos (Background)
	FD_PRETA    = f'\033[40m'
	FD_VERMELHA = f'\033[41m'
	FD_VERDE    = f'\033[42m'
	FD_AMARELA  = f'\033[43m'
	FD_AZUL     = f'\033[44m'
	FD_MAGENTA  = f'\033[45m'
	FD_CIANO    = f'\033[46m'
	FD_BRANCA   = f'\033[47m'

	FDB_PRETA    = f'\033[100m'
	FDB_VERMELHA = f'\033[101m'
	FDB_VERDE    = f'\033[102m'
	FDB_AMARELA  = f'\033[103m'
	FDB_AZUL     = f'\033[104m'
	FDB_MAGENTA  = f'\033[105m'
	FDB_CIANO    = f'\033[106m'
	FDB_BRANCA   = f'\033[107m'

	# Efeitos
	UNDERLINE   = f'\033[4m'
	ITALICO     = f'\033[3m'
	NEGRITO     = f'\033[1m'
	SLOW_BLINK  = f'\033[5m'
	RAPID_BLINK = f'\033[6m'

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
	NONE = f'\033[0m'

	def __init__(self):
		'''Classe para tratar de cores e estilos para o Shell

		Variables (str):

			# Cor da Fonte (Foreground)
			CF_PRETA
			CF_VERMELHA
			CF_VERDE
			CF_AMARELA
			CF_AZUL
			CF_MAGENTA
			CF_CIANO
			CF_BRANCA

			CFB_PRETA
			CFB_VERMELHA
			CFB_VERDE
			CFB_AMARELA
			CFB_AZUL
			CFB_MAGENTA
			CFB_CIANO
			CFB_BRANCA

			# Fundos (Background)
			FD_PRETA
			FD_VERMELHA
			FD_VERDE
			FD_AMARELA
			FD_AZUL
			FD_MAGENTA
			FD_CIANO
			FD_BRANCA

			FDB_PRETA
			FDB_VERMELHA
			FDB_VERDE
			FDB_AMARELA
			FDB_AZUL
			FDB_MAGENTA
			FDB_CIANO
			FDB_BRANCA

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
		except KeyboardInterrupt as ki:
			pass
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
			self.print(f'{self.FD_VERMELHA}{self.CF_BRANCA} {funcao} {self.NONE}')
			self.print(tx_erro, cor=self.CF_VERMELHA)
		except Exception as er:
			print('shell_style.erro:')
			print(er)
