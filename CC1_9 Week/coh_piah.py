import re

def le_assinatura():
    # A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))
    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    # A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    return textos

def separa_sentencas(texto):
    # A funcao recebe um texto e devolve uma lista das sentencas dentro do texto
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    # A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    #A funcao recebe uma frase e devolve uma lista das palavras dentro da frase
    return frase.split()

def n_palavras_unicas(lista_palavras):
    #Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas

def n_palavras_diferentes(lista_palavras):
    # Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)

# 1 traco linguistico: tamanho medio de palavra, soma dos tamanhos
# das palavras dividida pelo num total de palavras

def tamanho_medio_palavras(texto):
    sentencas = separa_sentencas(texto)
    lista_frases = []
    lista_palavras = []
    soma = 0

    # recebo 'texto' e pego a lista de sentencas desse texto
    for sentenca in sentencas:
        lista_frases.extend(separa_frases(sentenca))
    # recebo a lista de sentencas e faco outra lista com todas as frases
    for frase in lista_frases:
        lista_palavras.extend(separa_palavras(frase))
    # com a lista de palavras, faco a soma do len de todas elas
    for palavra in lista_palavras:
        soma += len(palavra)
    # devolvo a divisao da soma pelo total de palavras
    return (soma / len(lista_palavras))

# 2 traco linguistico: relacao type token, é o número de palavras diferentes dividido pelo número total de palavras.
def type_token(texto):
    sentencas = separa_sentencas(texto)
    lista_frases = []
    lista_palavras = []

# recebo 'texto' e pego a lista de sentencas desse texto
    for sentenca in sentencas:
        lista_frases.extend(separa_frases(sentenca))
# recebo a lista de sentencas e faco outra lista com todas as frases
    for frase in lista_frases:
        lista_palavras.extend(separa_palavras(frase))
# com a lista de palavras, verifico a quantidade de palavras diferentes
    palavras_diferentes = n_palavras_diferentes(lista_palavras)
# com o num de palavras diferentes, retorno sua divisao pelo total de palavras
    return (palavras_diferentes/(len(lista_palavras)))

# 3 traco linguistico: razao hapax legomana
def hapax_legomana(texto):
    sentencas = separa_sentencas(texto)
    lista_frases = []
    lista_palavras = []

# recebo 'texto' e pego a lista de sentencas desse texto
    for sentenca in sentencas:
        lista_frases.extend(separa_frases(sentenca))
    # recebo a lista de sentencas e faco outra lista com todas as frases
    for frase in lista_frases:
        lista_palavras.extend(separa_palavras(frase))
    # com a lista de palavras, verifico a quantidade de palavras unicas
    palavras_unicas = n_palavras_unicas(lista_palavras)
    # com o num de palavras unicas, retorno sua divisao pelo total de palavras
    return (palavras_unicas/(len(lista_palavras)))

# 4 traco linguistico: tamanho medio sentenca
def tamanho_medio_sentenca(texto):
  soma = 0
  # separo o texto em sentencas
  sentencas = separa_sentencas(texto)
  # para cada sentenca, quero somar o total de caracteres
  for sentenca in sentencas:
    soma += len(sentenca)
  # faco a divisao da soma pelo total de separa_sentencas
  return (soma / len(sentencas))

# 5 traco linguistico: complexidade de sentenca
def complexidade_sentenca(texto):
    sentencas = separa_sentencas(texto)
    lista_frases = []
    # separo o texto em sentencas
    for sentenca in sentencas:
        lista_frases.extend(separa_frases(sentenca))
    # faco a divisao do total de frases pelo total de sentencas
    return (len(lista_frases)/len(sentencas))

# 6 traco linguistico: tamanho medio de frase
def tamanho_medio_frase(texto):
  sentencas = separa_sentencas(texto)
  lista_frases = []
  soma = 0
    
  for sentenca in sentencas:
    lista_frases.extend(separa_frases(sentenca))
  for frase in lista_frases:
    soma += len(frase)
  return (soma/len(lista_frases))

def compara_assinatura(as_a, as_b):
    # IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.
    soma = 0
    i = 0

    while i <= (len(as_a) - 1):
        soma += abs(as_a[i] - as_b[i])
        i += 1

    return soma/6

def calcula_assinatura(texto):
    # IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.
    assinatura = []
    assinatura.append(tamanho_medio_palavras(texto))
    assinatura.append(type_token(texto))
    assinatura.append(hapax_legomana(texto))
    assinatura.append(tamanho_medio_sentenca(texto))
    assinatura.append(complexidade_sentenca(texto))
    assinatura.append(tamanho_medio_frase(texto))
    return assinatura

def avalia_textos(textos, ass_cp):
    # IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    grau_similaridades = []
    
    for texto in textos:
        as_a = calcula_assinatura(texto)
        grau_similaridades.append(compara_assinatura(as_a, ass_cp))

    i = 0
    infectado = grau_similaridades[i]
    while i < len(grau_similaridades) - 1:
        if grau_similaridades[i] <= infectado:
            infectado = grau_similaridades[i]
            index = i
        i += 1

    return (index + 1)
    



















