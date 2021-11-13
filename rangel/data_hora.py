def dia_semana(ds) -> str:
	dso = ds
	try:
		ds = ds.lower()
		en = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
		pt = ['domingo','segunda-feira','terça-feira','quarta-feira','quinta-feira','sexta-feira','sábado']
		i  = en.index(ds)
		return pt[i]
	except Exception as er:
		print('dia_semana:')
		print(er)
		return dso

def data_extenso(dt) -> str:
	dto = dt
	try:
		meses = [
			'',
			'Janeiro',
			'Fevereiro',
			'Março',
			'Abril',
			'Maio',
			'Junho',
			'Julho',
			'Agosto',
			'Setembro',
			'Outubro',
			'Novembro',
			'Dezembro'
		]
		spt = dt.split('/')
		dd  = int( spt[0] )
		mm  = spt[1]
		yy  = spt[2]
		mme = meses[ int( mm ) ]
		return f'{dd} de {mme} de {yy}'
	except Exception as er:
		print('data_extenso:')
		print(er)
		return dto
