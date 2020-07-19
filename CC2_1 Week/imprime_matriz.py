'''function that receives a list of lists and prints each list in a different line'''

def imprime_matriz(matriz):
  linha = 0
  
  while linha < len(matriz):
    for i in matriz[linha]:
      print (i, end=' ')
    print()
    linha += 1
