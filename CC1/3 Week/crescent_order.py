'it checks if 3 int inputs were done in crescent order'

NumInt1 = int(input("Primeiro Numero: "))
NumInt2 = int(input("Segundo Numero: "))
NumInt3 = int(input("Terceiro Numero: "))
if NumInt1 < NumInt2 and NumInt2 < NumInt3:
  print("crescente")
else:
  print("não está em ordem crescente")
