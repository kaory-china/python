# Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro 
# e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).

# EXEMPLO
# >>>n_primos(2)
# 1
# >>>n_primos(4)
# 2
# >>>n_primos(121)
# 30

# ALGORITMO




# CODIGO

def n_primos(n)
	fator = 2
	soma = 0
	while n % fator != 0 and fator <= n:
		fator = fator +1
	if n % fator == 0:
		soma += 0
	else:
		soma += 1
	return soma

n_primos(2)