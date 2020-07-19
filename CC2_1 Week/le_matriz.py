'receives from user number of lines and columns of a list and each of its element, then prints the final list'

def cria_matriz(linhas, colunas):
    '''(int, int, valor) - > matriz (lista de listas)
        Cria e retornar uma matriz com num_linhas linhas e
        num_colunas colunas em que cada elemento é igual ao valor dado.'''
    # inicializo a lista matriz, vazia
    matriz = []
    # para cada linha em 'num_linhas'
    for lin in range(linhas):
        # cria uma 'lista linha', inicialmente vazias (comando abaixo)
        linha = []
        # para cada coluna em 'num_colunas'
        for coluna in range(colunas):
            # ele adiciona na lista 'linha' o valor dado na qtdd de num_colunas
            linha.append(int(input('Digite o valor do elemento [' + str(lin) + '] [' + str(coluna) + ']:')))
        # adiciona a linha ja com os valores, na matriz (lista de listas)
        matriz.append(linha)
    return matriz

def le_matriz():
    linhas = int(input('Digite o número de linhas da matriz: '))
    colunas = int(input('Digite o número de colunas da matriz: '))
    return cria_matriz(linhas, colunas)
