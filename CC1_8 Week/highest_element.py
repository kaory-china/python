# Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteirose devolve um número
# inteiro correspondente ao maior valor presente na lista recebida.

lista = [-90, -12]
def maior_elemento(lista):
    comprimento = len(lista) - 1
    # inicial variavel do objetivo da funcao
    maior_elemento = lista[comprimento]
    # para cada item da lista, verificar se o item e maior que maior_elemento
    for i in lista:
        if i > maior_elemento:
            maior_elemento = i
    return maior_elemento
    
