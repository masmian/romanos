def numero_romano(numero_origen):
	unidades = ["","I", "II", "III", "IV", "V", "IV", "VII", "VIII", "IX"]
	decenas = ["","X", "XX", "XXX", "XL", "L","LX","LXX","LXXX","XC"]
	centenas = ("","C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM")
	millares = ("","M", "MM", "MMM")
	
	numero=str(numero_origen)

	largo = len(numero)
	numero_texto = ""
	if(largo == 1):
		unidad = int(numero)
		numero_texto += unidades[unidad]
	elif (largo ==2):
		decena = int(numero[0])
		numero_texto += decenas[decena]
		unidad = int(numero[1])
		numero_texto += unidades[unidad]
	elif (largo ==3):
		centena = int(numero[0])
		numero_texto += centenas[centena]
		decena = int(numero[1])
		numero_texto += decenas[decena]
		unidad = int(numero[2])
		numero_texto += unidades[unidad]
	elif (largo ==4):
		millar = int(numero [0])
		numero_texto += millares[millar]
		centena = int(numero[1])
		numero_texto += centenas[centena]
		decena = int(numero[2])
		numero_texto += decenas[decena]
		unidad = int(numero[3])
		numero_texto += unidades[unidad]

	return numero_texto

