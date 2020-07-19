def n_primos(x):
    fator = 2
    soma = 1
    while x >= 2:
        while  x % fator != 0 and fator <= x/2:
            fator += 1
        if x % fator == 0:
            soma += 0
        else:
            soma += 1
        x -= 1
        fator = 2
    return soma



# ALGORITMO
# funcao vai receber um numero inteiro maior ou igual a 2
# fator comeca com 2 porque todo numero e divisel por 1
# variavel de controle de soma dos numeros primos, comeca com 1

# primero loop, enquanto o numero for menor ou igual a 2:
    # entro em outro loop pra verificar se numero e primo, enquanto modulo de x por fator for diferente de zero
    # e fator for menor ou igual que metadre de x
        # executo fator += 1, senao cai fora e faco a soma 
    # se modulo de x por fator for igual a zero, quer dizer que x nao e primo
        # soma += 0 (ver como nao precisar colocar isso)
    # senao, e primo
        # soma += 1
    # vou para o proximo numero da sequencia x -= 1
    # reseto o fator para 2

# qdo numero for igual a 2, returno soma
