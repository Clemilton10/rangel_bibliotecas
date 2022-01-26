class medidas:
	π = 3.14159265359

	def coordenadas_hipotenusa(self, x1, y1, x2, y2):
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

	def catetos_hipotenusa(self, cateto_adjacente, cateto_oposto):
		try:
			d = ( cateto_adjacente ** 2 ) + ( cateto_oposto ** 2 )
			d = d ** .5
			return d
		except Exception as er:
			print('medidas.catetos_hipotenusa:')
			print(er)
			return 0

	def coordenadas_area(self, x1, y1, x2, y2):
		try:
			cateto_adjacente = x2 - x1
			cateto_oposto = y2 - y1
			a = ( cateto_adjacente * cateto_oposto ) / 2
			return a
		except Exception as er:
			print('medidas.coordenadas_area:')
			print(er)
			return 0

	def catetos_area(self, cateto_adjacente, cateto_oposto):
		try:
			a = ( cateto_adjacente * cateto_oposto ) / 2
			return a
		except Exception as er:
			print('medidas.catetos_area:')
			print(er)
			return 0

	def raio_area(self, raio):
		try:
			a = ( self.π * ( raio ** 2 ) )
			return a
		except Exception as er:
			print('medidas.raio_area:')
			print(er)
			return 0

	def raio_circunferencia(self, raio):
		try:
			c = 2 * self.π * raio
			return c
		except Exception as er:
			print('medidas.raio_circunferencia:')
			print(er)
			return 0

	def area_raio(self, area):
		try:
			r = area / self.π ** .5
			return r
		except Exception as er:
			print('medidas.area_raio:')
			print(er)
			return 0

	def circunferencia_raio(self, circunferencia):
		try:
			r = circunferencia / ( 2 * self.π )
			return r
		except Exception as er:
			print('medidas.circunferencia_raio:')
			print(er)
			return 0
