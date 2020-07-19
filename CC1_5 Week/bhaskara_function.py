# otimizar programa que calcular bhasara com funcoes

import math

def delta(a, b, c):
	return (b**2 - 4*a*c)

def bhaskara (a, b, c):
	d = delta(a, b, c)
	if d > 0:
		Raíz1 = (-b + math.sqrt(d)) / 2*a
		Raíz2 = (-b - math.sqrt(d)) / 2*a
		print("as raízes da equação são", Raíz1, "e", Raíz2)
	else:
		if d == 0:
			Raíz1 = (-b + math.sqrt(d)) / 2*a
			print("a raíz desta equação é", Raíz1)
		else:
			print("esta equação não possui raízes reais")


