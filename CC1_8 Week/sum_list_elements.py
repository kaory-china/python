# Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um
# número inteiro correspondente à soma dos elementos da lista recebida.

lista = [10, 10, 10, 10, 10, 10]


def soma_elementos(lista):
    # inicio a variavel soma
    soma = 0
    # verifico o len da lista
    comprimento = len(lista) - 1
    # enquanto o len for maior ou igual a zero
    while comprimento >= 0:
        # adiciono os valores de cada item a variavel soma
        soma += lista[comprimento]
        comprimento -= 1
    # ao final do loop retorno a soma
    return soma

