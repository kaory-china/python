'this function receives number of lines, numer of columns and a value, creating and returning the list'

def cria_matriz(num_linhas, num_colunas, valor):
    '''(int, int, valor) - > matriz (lista de listas)
        Cria e retornar uma matriz com num_linhas linhas e
        num_colunas colunas em que cada elemento é igual ao valor dado.'''
    # inicializo a lista matriz, vazia
    matriz = []
    # para cada linha em 'num_linhas'
    for linha in range(num_linhas):
        # cria uma 'lista linha', inicialmente vazias (comando abaixo)
        linha = []
        # para cada coluna em 'num_colunas'
        for coluna in range(num_colunas):
            # ele adiciona na lista 'linha' o valor dado na qtdd de num_colunas
            linha.append(valor)
    
        # adiciona a linha ja com os valores, na matriz (lista de listas)
        matriz.append(linha)

        

    return print (matriz)
