# INSTRUÇÕES PARA USO DE WHILE LOOP
# inicializar as variáveis de controle antes do comando;
# criar uma condição que usa a variável de controle e se mantenha verdadeira pelo número correto de iterações;
# modificar a variável de controle para garantir a terminação; e
# realizar as computações sucessivas para se chegar a resposta correta.

# ENUNCIADO

# Dados um número inteiro n, n > 0, e uma sequência com n números reais, verificar se a sequência está em ordem crescente.
# EXERCICIO 5.2 - https://panda.ime.usp.br/aulasPython/static/aulasPython/aula05.html 

# ALGORITMO

# input de quantidade de numeros
# iniciar variavel de valores = valor
# iniciar contagem de sequencia de numeros 0
# enquanto sequencia de numeros for menor que a quantidade de numeros
# input de numero
# se o numero for maior que a variavel 'valor'
# valor passa a ser o numero
# contagem mais um
# senao
# esta sequencia nao esta em ordem crescente
# fora do bloco anterior
# esta sequencia esta em ordem crescente

# CÓDIGO

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
