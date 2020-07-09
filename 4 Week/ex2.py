# Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. 

# ALGORITMO/TESTE

# input de um número = quantidade
# obter a quantidade de '10' números ímpares de forma crescente, variável pode ser 'numero' com valor inicial de 1 
# enquanto a quantidade nao chegar a quantidade de  
# numeros ímpares são números onde o módulo do número por 2 é diferente de zero, iniciar por 1
# se o modulo de 'numero' por 2 for diferente de zero
	# printar o 'numero'
	# adicionar 1 a 'numero'
# senao, adicionar 1 a 'numero'

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
	

