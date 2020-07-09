# Escreva um programa que receba um número inteiro positivo na entrada e 
# verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

# número primo é aquele maior do que um que é dividido apenas por um e ele mesmo

# ALGORITMO TENTATIVA 1
# receber input de número inteiro 'numInt'
# inicio variavel 'primo' = False
# enquanto 'primo' for False
# se modulo de numInt por 2 for difeferente de zero ou se quociente da divisao de numInt por 2 for menor que 2, primo
# 'primo' passa a ser True
# senao, 
	# se modulo de numInt por 3 for difeferente de zero ou se quociente da divisao de numInt por 3 for menor que 3, primo
	# 'primo' passa a ser True
# senao, 
	# se modulo de numInt por 5 for difeferente de zero ou se quociente da divisao de numInt por 5 for menor que 5, primo
	# 'primo' passa a ser True
# senao, 
	# se modulo de numInt por 7 for difeferente de zero ou se quociente da divisao de numInt por 7 for menor que 7, primo
	# 'primo' passa a ser True
# printar 'primo'

# ALGORITMO TENTATIVA 2
# recebo input de um numero 'n'
# varival divisor = 'n'
# variavel total = 0
# enquanto variavel divisor for maior que 1 ou variavel total for diferente de 2
	# se modulo de 'n' por divisor == 0
	# atualiza variavel divisor 'n' - 1
	# atualiza variavel total + 1
# senao
	# atualiza variavel divisor 'n' - 1
# finaliza com 'não primo'

# ALGORITMO TENTATIVA 3


# CÓDIGO

numInt = int(input('Digite um número inteiro: '))
num = numInt - 1
primo = True
while num > 1:
	if numInt % num !=0: 
		num -= 1
	else:
		primo = False
		num -= 1
	
if primo == True:
	print('primo')
else:
	print('não primo')

	