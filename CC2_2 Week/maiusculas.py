'''Escreva a função maiusculas(frase) que recebe uma frase (uma string) como
parâmetro e devolve uma string com as letras maiúsculas que existem nesta frase,
na ordem em que elas aparecem.'''

def maiusculas(frase):
    i = 0
    maiuscula = ''
    while i < len(frase):
        if ord(frase[i]) >= 65 and ord(frase[i]) <= 90:
            maiuscula += frase[i]
        i += 1
    return maiuscula
        
        
    
