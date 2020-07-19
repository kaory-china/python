
'it checks if the int inputs are in crescent order'

valor = int(input("Valor: "))
i = 10
anterior = -1

#found = False

while valor // i > 0:
  current = (valor % i) // (i/10)
  if current == anterior:
    print("sim")
    exit(0)
  else:
    anterior = current
  i *= 10

print("não")
