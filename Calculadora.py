print('*****************')
print('***Calculadora***')
print('*****************')
ope = ''
print('Escola uma das opções para inciar as operações')
while(ope != 'a' and ope != 's' and ope != 'd' and ope != 'm'):
	ope = str(input('Digite A = Adição, S = Subtração, D = Divisão, M = Multiplicação: '))
	ope = ope.lower()
	if ope == 'a':
		n1 = float(input('Digite um numero: '))
		n2 = float(input('Digite outro numero: '))
		total = n1 + n2
		if total % 1 == 0:
			print (int(total))
		else: 
			print (total)

	elif ope == 's':
		n1 = float(input('Digite um numero: '))
		n2 = float(input('Digite outro numero: '))
		total = n1 - n2
		if total % 1 == 0:
			print (int(total))
		else:
			print (total) 

	elif ope == 'd':
		n1 = float(input('Digite um numero: '))
		n2 = float(input('Digite outro numerlo: '))
		total = n1 / n2
		if total % 1 == 0:
			print (int(total))
		else:
			print (total)

	elif ope == 'm':
		n1 = float(input('Digite um numero: '))
		n2 = float(input('Digite outro numero: '))
		total = n1 * n2
		if total % 1 == 0:
			print (int(total))
		else:
			print (total)

	else:
		print('Essa não e uma opção valida')
