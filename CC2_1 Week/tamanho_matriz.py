'''Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e imprime
as dimensões da matriz recebida, no formato Linhas X Colunas.'''

# ALGORITMO

# recebo uma matriz
# quantidade de linhas é o len da matriz
# quantidade de colunas é o len de cada linha, usei a linha 0

def dimensoes(minha_matriz):
    linhas = len(minha_matriz)
    colunas = len(minha_matriz[0])
    return print(str(linhas) + 'X' + str(colunas))
