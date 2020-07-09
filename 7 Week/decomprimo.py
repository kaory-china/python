# dado um numero n, n > 1, imprimir sua decomposicao em fatores primos, 
# indicando tambem a multiplicidade de cada fator.

# 8 = 2 * 2 * 2
# 20 = 2 * 2 * 5
# 1000 = 2^3 * 5^3

n = int(input("Digite um número inteiro > 1: "))
# descobrir fatores:
fator = 2
multiplicidade = 0

while n > 1:
	while n%fator == 0:
		multiplicidade += 1
		n = n / fator
	if multiplicidade > 0:
		print ("fator ", fator, "multiplicidade =", multiplicidade)
	fator += 1
	multiplicidade = 0


