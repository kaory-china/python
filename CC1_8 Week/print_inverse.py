# faca um programa que vai lendo do teclado uma sequencia de numeros e qdo o usuario digitar zero
# imprimi a lista em ordem inversa

n = int(input('Digite um numero:'))
lista = []

while n != 0:
    lista.append(n)
    n = int(input('Digite um numero:'))

comprimento = len(lista) - 1
while comprimento >= 0:
    print (lista [comprimento], end = ' ')
    comprimento -= 1
    
