print('*****************')
print('***Calculadora***')
print('*****************')
ope = ''
print('Escola uma das opções para inciar as operações')
while(ope != 'A'  and ope != 'a' and ope != 'S' and ope != 's' and ope != 'D'  and ope != 'd' and ope != 'M' and ope != 'm'):
	ope = str(input('Digite A = Adição, S = Subtração, D = Divisão, M = Multiplicação: '))
	if ope == 'A' or ope == 'a':
		n1 = float(input('Digite um numero: '))
		n2 = float(input('Digite outro numero: '))
		print (n1 ,'+', n2, '=', n1 + n2)
	elif ope == 'S' or ope == 's':
		n1 = float(input('Digite um numero: '))
		n2 = float(input('Digite outro numero: '))
		print(n1 ,'-', n2, '=', n1 - n2)
	elif ope == 'D' or ope == 'd':
		n1 = float(input('Digite um numero: '))
		n2 = float(input('Digite outro numerlo: '))
		print(n1 ,'/', n2, '=', n1 / n2)
	elif ope == 'M' or ope == 'm':
		n1 = float(input('Digite um numero: '))
		n2 = float(input('Digite outro numero: '))
		print(n1 ,'*', n2, '=', n1 * n2)
	else:
		print('Essa não e uma opção valida')