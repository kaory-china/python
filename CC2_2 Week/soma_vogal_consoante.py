'''Escreva a função conta_letras(frase, contar="vogais"), que recebe como
primeiro parâmetro uma string contendo uma frase e como segundo parâmetro uma outra string.
Este segundo parâmetro deve ser opcional.

Quando o segundo parâmetro for definido como "vogais", a função deve devolver
o numero de vogais presentes na frase. Quando ele for definido como "consoantes",
a função deve devolver o número de consoantes presentes na frase. Se este parâmetro não
for passado para a função, deve-se assumir o valor "vogais" para o parâmetro.'''

def conta_letras(frase, contar='vogais'):
    soma_vogais = 0
    soma_consoantes = 0
    
    for letra in frase:
        if letra == 'a' or letra == 'A' or letra == 'e' or letra == 'E' or letra == 'i' or letra == 'I' or letra == 'o' or letra == 'O' or letra == 'u' or letra == 'U':
            soma_vogais += 1
        else:
            if letra != ' ':
                soma_consoantes += 1

    if contar == 'vogais':
        return soma_vogais
    else:
        return soma_consoantes
