def usuario_escolhe_jogada(n, m):
    retirar = int(input('Quantas peças você vai tirar?'))
    while retirar > m or retirar > n or retirar <= 0:
        print('Oops! Jogada inválida! Tente de novo')
        retirar = int(input('Quantas peças você vai tirar?'))
    return retirar

def computador_escolhe_jogada(n, m):
    i = m
    if m > n:
        return n
    else:
        while i <= m and i <= n: 
            if (n - i) % (m + 1) == 0:
                return i
            else:
                i -= 1
    return m

    #4
def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    if n % (m + 1) == 0:
        print('Você começa!')
        while n != 0:
            pecas = usuario_escolhe_jogada(n, m)
            n = n - pecas
            if pecas == 1:
                print('Você tirou ', pecas , 'peça.')
            if pecas > 1:
                print('Você tirou ', pecas , 'peças.')
            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            if n > 1:
                print('Agora resta restam ', n, 'peças no tabuleiro.')
            if n == 0:
                print('Fim do jogo! Você ganhou!')
                return 0
            pecas = computador_escolhe_jogada(n, m)
            n = n - pecas
            if pecas == 1:
                print('O computador tirou ', pecas , 'peça.')
            if pecas > 1:
                print('O computador tirou', pecas , 'peças.')
            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            if n > 1:
                print('Agora resta restam ', n, 'peças no tabuleiro.')
            if n == 0:
                print('Fim do jogo! O computador ganhou!')
                return 1
    else:
        while n != 0:
            print('Computador começa!')
            pecas = computador_escolhe_jogada(n, m)
            n = n - pecas
            if pecas == 1:
                print('O computador tirou ', pecas , 'peça.')
            if pecas > 1:
                print('O computador tirou', pecas , 'peças.')
            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            if n > 1:
                print('Agora resta restam ', n, 'peças no tabuleiro.')
            if n == 0:
                print('Fim do jogo! O computador ganhou!')
                return 1
            pecas = usuario_escolhe_jogada(n, m)
            n = n - pecas
            if pecas == 1:
                print('Você tirou ', pecas , 'peça.')
            if pecas > 1:
                print('Você tirou ', pecas , 'peças.')
            if n == 1:
                print('Agora resta apenas uma peça no tabuleiro.')
            if n > 1:
                print('Agora resta restam ', n, 'peças no tabuleiro.')
            if n == 0:
                print('Fim do jogo! Você ganhou!')
                return 0

def campeonato():
    print('Voce escolheu um campeonato!')
    usuario = 0
    computador = 0      
    print('**** Rodada 1 ****')                  
    p1 = partida()
    if p1 == 0:
        usuario += 1
    else:
        computador += 1
    print('**** Rodada 2 ****')                  
    p2 = partida()
    if p2 == 0:
        usuario += 1
    else:
        computador += 1
    print('**** Rodada 3 ****')                  
    p3 = partida()
    if p3 == 0:
        usuario += 1
    else:
        computador += 1
    print('**** Final do campeonato! ****')
    print('Placar: Você ', usuario, 'x', computador, 'Computador')

print('Bem-vindo ao jogo do NIM! Escolha: ')
print('1 - para jogar uma partida isolada')
print('2 - para jogar um campeonato')
p = int(input('Escolha o modo: '))
if p == 2:
    campeonato()
else:
    partida()


    
