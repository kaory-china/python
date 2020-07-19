'''Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve
uma matriz que represente sua soma caso as matrizes tenham dimensões iguais.
Caso contrário, a função deve devolver False.'''

# ALGORITMO

# recebo duas matrizes
# verificar se num de linhas e colunas sao iguais
# se forem iguais, criar uma nova matriz com a soma dos elementos de mesma posicao
# senao retornar falso

def dimensoes(minha_matriz):
    linhas = len(minha_matriz)
    colunas = len(minha_matriz[0])
    return (str(linhas) + 'X' + str(colunas))

def soma_matrizes(m1, m2):
    soma_matrizes = []
    
    if dimensoes(m1) == dimensoes(m2):
        linha = []
        lin = 0
        col = 0
        while lin < len(m1) and col < len(m1[0]):
            for i in m1[lin]:
                linha.append(m1[lin][col] + m2[lin][col])
                col += 1
                print(lin)
                print(col)
            soma_matrizes.append(linha)
            lin += 1
            col = 0
            linha = []

        return soma_matrizes
    else:
        return False

'''
0 - supondo que as matrizes tem 3 linhas com 3 colunas

1 - criar uma linha vair receber a soma dos elementos, inicialmente vazia

2 - para cada lista (da lista)

cada elemento dessa linha vai ser a soma dos elementos (mesma posicao)
das duas matrizes:

para cada linha, temos que fazer:
    matriz1[0][0] + matriz2[0][0]
    matriz1[0][1] + matriz2[0][1]
    matriz1[0][2] + matriz2[0][2]

3 - faco o append desta linha na lista principal de soma_matrizes

4 - retorno a soma_matrizes'''
