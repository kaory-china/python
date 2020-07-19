# Escreva a função remove_repetidos que recebe como parâmetro uma lista com
# números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos.
# A lista devolvida deve estar ordenada.

# ALGORITMO

# escrever uma funcao que
# receber uma lista de numeros inteiros

# verificar se ha numeros repetidos
    # como verificar se ha numeros repetidos
    # fazer um loop comparando cada item com todos os itens restantes, fazer isso
    # para todos os itens

# remover os repetidos
    # se for igual, deletar esse item

# qdo acabar, ordenar

# retornar uma e lista sem repeticoes e ordenada

# CODIGO

def remove_repetidos(lista):
    lista_limpa = []
    comprimento = len(lista) - 1

    for i in lista:
        if i in lista_limpa:
            continue
        else:
            lista_limpa.append(i)
    return sorted(lista_limpa)
