# Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.

# ALGORITMO

# recebo um input de um 'número'
# 
# fatorial igual a multiplicacao sequencial de n por todos numeros inteiros menores ou iguais a n 
# fatorial = n * (n - 1)
# fatorial = fatorial * (n - 2)
# fatorial = fatorial * (n - 3)
# fatorial = fatorial * (n - 4)
# até que 1/2/3/4/5/n seja igual a n
# quando deve sair o valor final de fatorial

# ALGORITMO TENTATIVA 2

# temos um numero de 10
# fatorial = 10*(10-1)*(10-2)*(10-3)*(10-4)*(10-5)*(10-6)*(10-7)*(10-8)*(10-9)
# referencia = 1/2/3/4/5/6/7/8/9 = referencia for menor que 10 
# 


# CÓDIGO

numero = int(input("Digite o valor de n: "))
referencia = 1  
fatorial = numero

if numero == 0:
	fatorial = 1
else:
	while referencia < numero:
		fatorial = fatorial * (numero - referencia)
		referencia += 1
print(fatorial)


# TESTE
# input de 6
# primeira variavel = fatorial = numero (relacionados aos numeros 6/30/120/360/720 abaixo)
# segunda variavel = referencia (relacionados aos numeros 1/2/3/4/5)
# condição enquanto referencia for menor que numero
# enquanto verdadeira, calcula fatorial e incrementa referencia em 1
# 6 * (6 - 1) = 30
# 30 * (6 - 2) = 120
# 120 * (6 - 3) = 360
# 360 * (6 - 4) = 720
# 720 * (6 - 5) = 720

# PRIMEIRA SEQUENCIA
# 1 < 6 = True
# 6*(6-1) = 30
# referencia = 2
# fatorial = 30

# SEGUNDA SEQUENCIA
# 2 < 6 = True
# 30*(6-2) = 120
