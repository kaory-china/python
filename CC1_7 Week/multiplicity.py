# Dado um número inteiro n, n > 1,
# imprimir sua decomposição em fatores primos, indicando também a mutiplicidade de cada fator.

n = int(input('digite um numero > 1: '))
fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade += 1
        n = n / fator
    if multiplicidade > 0:
        print ("fator", fator, "multiplicidade = ", multiplicidade)
    fator += 1
    multiplicidade = 0
