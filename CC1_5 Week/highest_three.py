# Reescreva a função 'maximo' do outro exercício, que devolve o maior valor dentre dois inteiros recebidos, 
# para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.

# ALGORITMO
# recebo dois numeros inteiros 'n1' e 'n2'
# 'n1' é maior que 'n2'? 
# se sim, retorna 'n1'
# senao, retorna 'n2'

# CODIGO

def maximo(n1, n2, n3):
	if n1 >= n2 and n1>=n3:
		return(n1)
	if n2 >= n1 and n2 >= n3:
		return(n2)
	if n3 >= n1 and n3 >= n2:
		return(n3)

