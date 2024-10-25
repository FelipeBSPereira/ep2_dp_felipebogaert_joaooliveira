
def faz_jogada(tab, linha, coluna):
    if tab[linha][coluna] == 0:
        tab[linha][coluna] = '-'
    elif tab[linha][coluna] == 1:
        tab[linha][coluna] = 'X'
    return tab