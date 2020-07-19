# criar uma funcao para calculo de fatorial e depois fazer um programa para calcular o coeficiente binomial

# ALGORITMO
# definir uma função que calcula o fatorial de parametro 'numero'
# coeficiente binomial tem dois parametros 'n' e 'k'
	# fatorial(n) / fatorial(k)*fatorial(n-k)

def fatorial(numero):
	referencia = 1  
	fatorial = numero

	if numero == 0:
		fatorial = 1
	else:
		while referencia < numero:
			fatorial = fatorial * (numero - referencia)
			referencia += 1
	return(fatorial)

def coefbinomial(n, k):
	return(fatorial(n)/(fatorial(k)*fatorial(n-k)))
