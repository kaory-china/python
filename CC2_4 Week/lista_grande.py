import random

def lista_grande(n):
    lista = []
    for i in range(0,n):
        lista.append(random.randint(-99999, 99999))
    return lista
