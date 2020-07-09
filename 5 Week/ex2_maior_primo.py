# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro 
# e devolve o maior número primo menor ou igual ao número passado à função.

# ALGORITMO
# ****OBJETIVO: OBTER O MAIOR NUMERO PRIMO IGUAL OU MENOR A 'N'**** 

# COMO SABER SE UM NUMERO E PRIMO
	# UM NUMERO PRIMO SO E DIVISIVEL POR 1 E POR ELE MESMO, OU SEJA 
	# O RESTO DA DIVISAO DE N POR N, RESULTADO TEM QUE SER ZERO
	# O RESTO DA DIVISAO DE N POR 1, RESULTADO TEM QUE SER ZERO
	# O RESTO DA DIVISAO DE N POR (N - 1) ATÉ 2, RESULTADO TEM QUE SER DIFERENTE DE ZERO
# ----------------------------------------------------------

# PARA DESCOBRIR SE 'NUM' E PRIMO:

	# INICIO VARIAVEL DE CONTROLE 'TOTAL' = 0
	# INICIO VARIAVEL DE CONTROLE 'I' = 'NUM'
	# ENQUANTO I FOR MAIOR OU IGUAL A 1:
		# MODULO DE N POR I
			# SE FOR IGUAL A ZERO
				# ADICIONO 1 A VARIAVEL 'TOTAL'
				# DIMINUO 1 A VARIAVEL 'I'
			# SENAO:
				# DIMINUO 1 A VARIAVEL 'I'
	# SE TOTAL FOR IGUAL A 2
		# 'NUM' E PRIMO
		# RETORNA 'NUM' E ACABOU
	# SENAO
		# 'NUM' = 'NUM' -1
		# 'TOTAL' = 0
# ----------------------------------------------------------

# MAS EU QUERO O MAIOR NUMERO PRIMO:

	# 'NUM' = NUM - 1

# CÓDIGO
def primo(n):
	num = n - 1
	primo = True
	while num > 1:
		if n % num ==0: 
			return False
		num -= 1
	
	return primo


def maior_primo(n):
	while n>=2:
		if primo(n):
			return n
		else:
			n -= 1
	return n







   


