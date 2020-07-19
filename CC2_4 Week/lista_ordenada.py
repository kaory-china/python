def ordenada(lista):
    while len(lista) > 1:
        if lista[0] < lista[1]:
            return True
        else:
            return False
    return True


def busca(lista, elemento):
    for i in range(len(lista)):
        if  lista[i] == elemento:
            return i
    return False
