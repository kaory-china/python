'''Exercício 2: Ordem lexicográfica
Como pedido no segundo vídeo da semana, escreva a função primeiro_lex(lista) que recebe
uma lista de strings como parâmetro e devolve o primeiro string na ordem lexicográfica.
Neste exercício, considere letras maiúsculas e minúsculas.'''

def primeiro_lex(lista):
    menor = lista[0]

    for palavra in lista:
      if palavra <= menor:
        menor = palavra
    
    return menor
