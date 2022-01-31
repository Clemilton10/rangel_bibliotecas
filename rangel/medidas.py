class medidas:
	π = 3.14159265359

	def coordenadas_hipotenusa(self, x1: float, y1: float, x2: float, y2: float)->float:
		'''Função que calcula os catetos e retorna a hipotenusa

		Parameters:
			x1 (float): Primeira posição X
			y1 (float): Primeira posição Y
			x2 (float): Segunda posição X
			y2 (float): Segunda posição Y

		Returns:
			hipotenusa (float): Distância da Hipotenuza calculada
		'''
		try:
			cateto_adjacente = x2 - x1
			cateto_oposto = y2 - y1
			d = ( cateto_adjacente ** 2 ) + ( cateto_oposto ** 2 )
			d = d ** .5
			return d
		except Exception as er:
			print('medidas.coordenadas_hipotenusa:')
			print(er)
			return 0

	def catetos_hipotenusa(self, cateto_adjacente: float, cateto_oposto: float)->float:
		'''Função que calcula a hipotenusa

		Parameters:
			cateto_adjacente (float): Cateto para cálculo
			cateto_oposto (float): Cateto para cálculo

		Returns:
			hipotenusa (float): Distância da Hipotenuza calculada
		'''
		try:
			d = ( cateto_adjacente ** 2 ) + ( cateto_oposto ** 2 )
			d = d ** .5
			return d
		except Exception as er:
			print('medidas.catetos_hipotenusa:')
			print(er)
			return 0

	def coordenadas_area(self, x1: float, y1: float, x2: float, y2: float)->float:
		'''Função que calcula os catetos e retorna a área

		Parameters:
			x1 (float): Primeira posição X
			y1 (float): Primeira posição Y
			x2 (float): Segunda posição X
			y2 (float): Segunda posição Y

		Returns:
			área (float): Área calculada
		'''
		try:
			cateto_adjacente = x2 - x1
			cateto_oposto = y2 - y1
			a = ( cateto_adjacente * cateto_oposto ) / 2
			return a
		except Exception as er:
			print('medidas.coordenadas_area:')
			print(er)
			return 0

	def catetos_area(self, cateto_adjacente: float, cateto_oposto: float)->float:
		'''Função que calcula a área

		Parameters:
			cateto_adjacente (float): Cateto para cálculo
			cateto_oposto (float): Cateto para cálculo

		Returns:
			área (float): Área calculada
		'''
		try:
			a = ( cateto_adjacente * cateto_oposto ) / 2
			return a
		except Exception as er:
			print('medidas.catetos_area:')
			print(er)
			return 0

	def raio_area(self, raio: float)->float:
		'''Função que calcula a área baseada em um raio

		Parameters:
			raio (float): Raio para cálculo

		Returns:
			area (float): Área calculada
		'''
		try:
			a = ( self.π * ( raio ** 2 ) )
			return a
		except Exception as er:
			print('medidas.raio_area:')
			print(er)
			return 0

	def raio_circunferencia(self, raio: float)->float:
		'''Função que calcula a circunferência baseada em um raio

		Parameters:
			raio (float): Raio para cálculo

		Returns:
			circunferencia (float): Circunferência calculada
		'''
		try:
			c = 2 * self.π * raio
			return c
		except Exception as er:
			print('medidas.raio_circunferencia:')
			print(er)
			return 0

	def area_raio(self, area: float)->float:
		'''Função que calcula o raio baseado na área

		Parameters:
			area (float): Área para cálculo

		Returns:
			raio (float): Raio calculado
		'''
		try:
			r = area / self.π ** .5
			return r
		except Exception as er:
			print('medidas.area_raio:')
			print(er)
			return 0

	def circunferencia_raio(self, circunferencia: float)->float:
		'''Função que calcula o raio baseado em uma circunferência

		Parameters:
			circunferencia (float): Circunferência para cálculo

		Returns:
			raio (float): Raio calculado
		'''
		try:
			r = circunferencia / ( 2 * self.π )
			return r
		except Exception as er:
			print('medidas.circunferencia_raio:')
			print(er)
			return 0
