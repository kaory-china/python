# ENUNCIADO
# Dados um número inteiro n, n > 0, e uma sequência com n números reais, verificar se a sequência está em ordem crescente.

quantidadeNumeros = int(input("Digite o total de números: "))
valor = -1
sequencia = 0
ordemcrescente = True

while sequencia <= quantidadeNumeros and ordemcrescente == True:
	numero = int(input("Digite o número: "))
	if numero > valor:
		valor = numero
		sequencia += 1
	else:
		ordemcrescente = False

if ordemcrescente == True:
	print("Está em ordem crescente.")
else:
	print("Não está em ordem crescente.")
