# Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve
#'Fizz' se o número for divisível por 3 e não for divisível por 5;
#'Buzz' se o número for divisível por 5 e não for divisível por 3;
#'FizzBuzz' se o número for divisível por 3 e por 5;
#Caso o número não seja divisível 3 e também não seja divisível por 5, ela deve devolver o número recebido como parâmetro.

# ALGORITMO
# receber um parametro 'n'

# variavel div3 = modulo de 'n' por 3 e IGUAL e ZERO
# variavel div5 = modulo de 'n' por 5 e IGUAL e ZERO

# if div3 == True and div5 == False
	# 'Fizz'
# if div3 == False and div5 == True
	# 'Buzz'
# if div3 == True and div5 == True
	# 'FizzBuzz'
# if div3 == False and div5 == False
	# 'n'

def fizzbuzz(n):
	div3 = n%3 == 0
	div5 = n%5 == 0

	if div3 == True and div5 == False:
		return "Fizz"
	if div3 == False and div5 == True:
		return "Buzz"
	if div3 == True and div5 == True:
		return "FizzBuzz"
	if div3 == False and div5 == False:
		return n

