def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == 'vertical':
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    if orientacao == 'horizontal':
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    
    return posicoes

def preenche_frota(frota,navio, linha, coluna, orientacao, tamanho):
    posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    if navio not in frota:
        frota[navio] = []
    frota[navio].append(posicao)
    
    return frota


def faz_jogada(tab, linha, coluna):
    if tab[linha][coluna] == 0:
        tab[linha][coluna] = '-'
    elif tab[linha][coluna] == 1:
        tab[linha][coluna] = 'X'
    return tab

def posiciona_frota(frota):
    tab = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tab.append(linha)
    for posicoes in frota.values():
        for posicao in posicoes:
            for linha, coluna in posicao:
                tab[linha][coluna] = 1
    return tab

def afundados(frota, tabuleiro):
    navios_afundados = 0

    for posicoes in frota.values():
        for posicao in posicoes:
            afundado = True
            for linha, coluna in posicao:
                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
            if afundado:
                navios_afundados += 1

    return navios_afundados


def criar_matriz():
    tab = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tab.append(linha)
    return tab 

#def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    #posicoes_novas = define_posicoes(linha, coluna, orientacao, tamanho)
    #tab = []
    #for i in range(10):
        #linha = []
        #for j in range(10):
            #linha.append(0)
        #tab.append(linha)
    #if posicoes_novas > len(tab):
        #return False
    #for tipo_navio, navios in frota.items():
        #for navio in navios:
            #for pos in navio:
                #if pos in posicoes_novas:
                    #return False
    #return True

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes_novas = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao_nova in posicoes_novas:
        if posicao_nova[0] < 0:
            return False
        elif posicao_nova[0] >= 10:
            return False
        elif posicao_nova[1] < 0:
            return False
        elif posicao_nova[1] >= 10:
            return False
    for tipos_navios in frota.values():
        for navio in tipos_navios:
            for posicao_nova in navio:
                if posicao_nova in posicoes_novas:
                    return False
    return True
