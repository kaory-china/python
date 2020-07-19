# Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída.

# ALGORITMO

# receber input de um número inteiro = 'valor'
# CONDIÇÃO? 
# isolar o digito da unidade do 'valor' performando o modulo do 'valor' por 10, variavel 'digito'  
# somar o resultado acima com a variavel 'soma' (iniciada com valor zero)
# atualizar o 'i' multiplicando por 10 (para que na proxima iteração, isolarmos o digito da dezena)
# isolar o digito da dezena do 'valor' performando o modulo do 'valor' por 100
	# divisao inteira por 100/10 (que resulta no i anterior) e isola somente o valor da dezena
# somar o resultado com a 'soma'
# atualizar o 'i' multiplicando por 10 (para que na proxima iteração, isolarmos o digito da centena)
# repetir o loop while até que a condição retorne False
# ao final printar 'soma'

numInt = int(input("Digite um número inteiro: "))

soma = 0
i = 10

while numInt / i > 0.1:
	digito = (numInt % i) // (i // 10)
	soma += digito
	i *= 10
print(soma)

# PRIMEIRA SEQUENCIA
# 123
# while 123 // 10 > 0					: True 
# digito = (123 % 10) // (10 // 10)		: 3
# soma = 0 + 3.0 = 3
# i = 10*10 = 100

# SEGUNDA SEQUENCIA
# 123
# while 123 // 100 > 0					: True 
# digito = (123 % 100) // (100 // 10)	: 2
# soma = 3.0 + 2.0 = 5.0
# i = 100*10 = 1000

# TERCEIRA SEQUENCIA
# 123
# while 123 // 1000 > 0					: False 


# PRIMEIRO PROBLEMA
# while 123 // 10 > 0		: True 
# while 123 // 100 > 0		: True
# while 123 // 1000 > 0		: False
# while 123 // 10000 > 0	: False

