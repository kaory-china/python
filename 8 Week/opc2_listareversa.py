# Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência
# de números inteiros e imprima todos os valores em ordem inversa.
# A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.

lista = []
n = int(input('Digite um número: '))
while n != 0:
    lista.append(n)
    n = int(input('Digite um número: '))

comprimento = len(lista) - 1
while comprimento >= 0:
    print (lista[comprimento])
    comprimento -= 1


    
