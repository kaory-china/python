# ALGORITMO
# definiar variavel linha = 1
# definiar variavel coluna = 1
# enquanto linha for menor ou igual a 10:
    # enquanto coluna for menor ou igual a 10:
        # multiplico linha (tabuada do 2, por exemplo) por coluna (referencia)
        # adiciono 1 a coluna para fazer a proxima multiplicacao
    # adiciono 1 a linha para ir para a proxima tabuada
    # "reseto" coluna para 1

# CODIGO 

linha = 1
coluna = 1
while linha <= 10:
    while coluna <= 10:
        # o end ='\t' vai fazer com que tenha um espacamento padrao entre os prints
        print(linha * coluna, end ='\t')
        coluna += 1
    linha += 1
    # esse print vai fazer com que cada tabuada saia em uma linha diferente
    print()
    coluna = 1
  
