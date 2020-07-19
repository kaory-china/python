def busca(lista, elemento):
    first = 0
    last = len(lista)-1

    while first <= last:
        middle = (first + last)//2
        if lista[middle] == elemento:
            print (middle)
            return middle
        if elemento < lista[middle]:
            last = middle - 1
        else:
            first = middle + 1
        print (middle)
    return False


def bubble_sort(lista):
    end = len(lista) - 1
    
    for i in range(end, 0, -1):
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print (lista)
    return lista

def insertion_sort(lista):
    end = len(lista) - 1

    for i in range(0, end):
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista
                
