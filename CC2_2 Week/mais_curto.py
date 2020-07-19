'''Escrever uma funcao que recebe uma lista de stringscontendo nomes de
pessoas como parametro e devolve o nome mais curto. A funcao deve ignorar
espacos antes e depois do nome e deve devolver o nome capitalizado.'''

def menor_nome(lista_de_nomes):
    new_list = []
    for i in lista_de_nomes:
        n = i.strip().capitalize()
        new_list.append(n)
        
    mais_curto = new_list[0]
    it = 0
    while it < len(new_list):
        if len(new_list[it]) < len(mais_curto):
          mais_curto = new_list[it]
        it += 1
    return mais_curto.strip()
