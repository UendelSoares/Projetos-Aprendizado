import time
pont = int(0)
p1 = ''
p2 = ''

print('Olá, seja bem vindo ao nosso jogo de verdadeiro ou falso.')
nome = str(input('Qual seu nome? '))
time.sleep(0.5)
print('Então vamos começar', nome,', lembrando que so pode escolher entre v ou f.')

while (p1 != 'v' and p1 != 'f'):
	p1 = str(input('\nO Brasil faz fronteira com um membro da União Europeia. v ou f? '))
	p1 = p1.lower()
	if(p1 == 'v'):
		pont = 1
		print('voce acertou.')
		time.sleep(0.5)
		print('\nO Brasil faz fronteira com a Guiana Francesa, que faz parte da União Europeia.')
		print('Voce esta com' , pont, 'ponto')
	elif (p1 == 'f'):
		print('voce errou, por isso continua com', pont, 'ponto')
	else:
		print('Essa não e uma resposta valida')	
time.sleep(0.5)

while (p2 != 'v' and p2 != 'f'):
	p2 = str(input('\nPor causa do tamanho, as girafas ficam o tempo todo em pé e só se deitam quando vão dar à luz. v ou f? '))
	p2 = p2.lower()
	if(p2 == 'f'):
		pont = pont + 1
		print('voce acertou')
		time.sleep(0.5)
		print('\nAs girafas tiram pequenas sonecas ao longo do dia, e para isso elas se deitam')
		print('voce esta com', pont, 'pontos')
	elif(p2 == 'v'):
		print('voce errou, por isso continua com', pont, 'ponto')
	else:
		print('Essa nao e uma resposta valida')