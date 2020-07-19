# Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. 
# O programa deve imprimir uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.
# Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

# Exemplo
# digite a largura: 10
# digite a altura: 3
# ##########
# #        #
# ##########

# ALGORITMO
# receber input (numero inteiro) de largura ('largura') de um retangulo
# receber input (numero inteiro) de altura ('altura') de um retangulo
# i = 1
# enquanto 'i' for menor ou igual a 'altura':
	# i += 1
	# print (largura*'#')

# CODIGO

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

i = 1
linha = 1
while i <= altura:
	i += 1
	if linha == 1 or linha == altura:
		print(largura*'#')
	else:
		print('#' + ' '*(largura-2) + "#")
	linha += 1

	
