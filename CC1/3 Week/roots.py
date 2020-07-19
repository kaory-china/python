'it receives 3 float inputs and calculates roots'

import math
ParametroA = float(input("Digite o parâmetro A: "))
ParametroB = float(input("Digite o parâmetro B: "))
ParametroC = float(input("Digite o parâmetro C: "))
Delta = ParametroB**2 - 4*ParametroA*ParametroC
if Delta > 0:
  Raíz1 = (-ParametroB + math.sqrt(Delta)) / 2*ParametroA
  Raíz2 = (-ParametroB - math.sqrt(Delta)) / 2*ParametroA
  if Raíz1 < Raíz2:
    print("as raízes da equação são", Raíz1, "e", Raíz2)
  else:
    print("as raízes da equação são", Raíz2, "e", Raíz1)
else:
  if Delta == 0:
    Raíz1 = (-ParametroB + math.sqrt(Delta)) / 2*ParametroA
    print("a raíz desta equação é", Raíz1)
  else:
    print("esta equação não possui raízes reais")
