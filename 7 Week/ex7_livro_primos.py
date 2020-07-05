#Dada uma sequência de números inteiros maiores que um,
# terminada por um zero, determinar quantos números primos há na sequência.

def primo(x):
    num = x - 1
    primo = True
    while num > 1 and primo == True:
        if x % num == 0:
            primo = False
        num -= 1

    if primo == True:
        return True
    else:
        return False

def soma_primos(x):
    soma = 0
    i = 2
    while x > 1:
        if primo(x) == True:
            soma += 1
        x -= 1
    return soma
