# Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. 
# O programa deve imprimir uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.

# Exemplo
# digite a largura: 10
# digite a altura: 3
# ##########
# ##########
# ##########

# ALGORITMO
# receber input (numero inteiro) de largura ('largura') de um retangulo
# receber input (numero inteiro) de altura ('altura') de um retangulo
# i = altura 
# enquanto 'altura' for maior ou igual a i:
	# i -= 1
	# print (largura*'#')

# CODIGO

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

i = 1
while i <= altura:
	i += 1
	print(largura*'#')
