x = int(input("numero:"))
fator = 2
while x % fator != 0 and fator <= x:
	fator = fator +1
if x % fator == 0:
	print(False)
else:
	print(True)

	# while x % fator != 0
	# verificar se o resto de divisao de x pelo fator é diferente de zero
		# se for diferente, o loop continua, com a soma de 1 a fator
		# se for igual ja sabemos que esse numero não é primo (por ele é divisivel por outro - que nao é 1 nem ele mesmo)

	# and fator <= x/2:
	# esse segunda teste do while é para definir ponto de parada, que poderia ser menor que x, uma vez que 
