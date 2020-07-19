# Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. 

quantidade = int(input('Digite o valor de n: '))
soma = 0
numero = 1

while soma < quantidade:
	if numero % 2 != 0:
		print(numero)
		numero += 1
		soma += 1
	else:
		numero += 1
	

