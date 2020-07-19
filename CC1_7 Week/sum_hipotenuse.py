# primeiro faca uma funcao é_hipotenusa que diz se um número
# inteiro é o comprimento da hipotenusa de um triângulo com lados de comprimento inteiro ou não.

# um número é uma hipotenusa de um triângulo inteiro se existe um triângulo retângulo
# com lados inteiros cuja hipotenusa é igual a esse número.
# em outras palavras, n é uma hipotenusa se existem números inteiros i e j tais que: nˆ2 = iˆ2 + jˆ2

# ALGORITMO PARTE 1

# primeiro como saber se um numero e hipotenusa de algum triangulo

# ate que i seja menor que n, fazer um sequencia dos seguintes calculos:
# nˆ2 (constante pare esse loop) = iˆ2 + (n-i)ˆ2, se for verdareiro, n é uma hipotenusa
    # retorna verdadeiro
# senao
    # diminui 1 de i


def e_hipotenusa(x):
    c2 = 1
    c1 = 1
    hipotenusa = False
    while c1 < x:
        while c2 < x and hipotenusa == False:
            if x**2 == c1**2 + c2**2:
                hipotenusa = True
            else:
                c2 += 1
        c1 += 1
        c2 = 1
            
    if hipotenusa == True:
        return True
    else:
        return False

# ALGORITMO PARTE 2

    # inicio variavel de controle i com valor de 1
    #inicia variavel soma com valor de zero
    # enquanto i for menor que numero
        # verifico se o numero e uma hipotenusa com a funcao acima
        # se for, adiciono o numero a soma
        # adiciono 1 a i
    # retorno soma

def soma_hipotenusas(x):
    i = 1
    soma = 0
    while x > i:
        if e_hipotenusa(x) == True:
            soma += x
        x -= 1
    return soma

    
