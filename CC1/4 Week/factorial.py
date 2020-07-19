# Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.

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
