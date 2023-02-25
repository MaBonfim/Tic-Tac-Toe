import os
#constantes para as cores
VERMELHO = '\033[31m'
AZUL = '\033[34m'
ORIGINAL = '\033[0;0m'

#A função não recebe parâmetros
#Exibe o menu inicial do jogo mostrando as opções de começar ou sair e pede a seleção para o usuário
#Retorna o respectivo valor(1 ou 0) da seleção
def menu_inicial():
    print('=' * 19)
    print('Super - Jogo da Velha')
    print('Press 1 - Começar')
    print('Press 0 - Sair')
    print('=' * 19)
    try:
        select = int(input('selection: '))
    except:
        limpa_tela()
        return menu_inicial()
    if (select == 1) or (select == 0):
        return select
    else:
        limpa_tela()
        return menu_inicial()

#Função não recebe parâmetros
#Função para limpar a tela do terminal
#Função não retorna valor
def limpa_tela():
    os.system('cls')

#Função recebe como parâmetro uma lista que representa o tabuleiro do jogo
#Reinicia o tabuleiro, inicializando todos os espaços da matriz que representa o tabuleiro com 0
#Função não retorna valor
def inicializa_tabuleiro(tabuleiro):
    for i in range(0, 3):
        tabuleiro.append([])

    for i in range(0, 3):
        for j in range(0, 3):
            tabuleiro[i].append(0)

#Função recebe como parâmetros uma lista que representa o tabuleiro
#e uma variavel que representa a vez de qual jogador
#Exibe o estado atual do tabuleiro e quais casas foram marcadas
#a lista é uma matriz em que o valor representa cada estado da casa
#0 é vazio
#1 é X do jogador 1
#2 é O do jogador 2
#Função não retorna valor
def exibe_tabuleiro(tabuleiro,jogador):
    print('='*15)
    print(f'Jogador {jogador}')
    print('   1   2   3  X')
    for i in range(0, 3):
        print(f'{i + 1} ', end='')
        for j in range(0, 3):
            if tabuleiro[i][j] == 0:
                print('___', end='')
            elif tabuleiro[i][j] == 1:
                print(f'_{VERMELHO}X{ORIGINAL}_', end='')
            elif tabuleiro[i][j] == 2:
                print(f'_{AZUL}O{ORIGINAL}_', end='')
            if j != 2:
                print('|', end='')
        print()
    print('\nY')
    print('='*15)

#Função não recebe parametros
#Função para adquirir a coordenada que representa a jogada do respectivo jogador
#recebe do usuário uma string da coordenada
#Função retorna a própria string caso ela seja adequada como uma coordenada
def pega_coordenada():
    while 1:
        coord = str(input('Insira a coordenada no formato "x y" ou "x,y"\n-> '))
        if (len(coord) == 3):
            if (int(coord[0]) >= 1) and (int(coord[0]) <= 3) and ((coord[1] == ' ') or (coord[1] == ',')):
                return coord
            else:
                return pega_coordenada()
        else:
            return pega_coordenada()

#Função recebe como parâmetro a variável que representa o jogador
#Muda o estado da variavel "jogador" mudando a vez de cada um
#Função retorna o valor referente ao novo jogador(1 ou 2)
def muda_jogador(jogador):
    if jogador == 1:
        return 2
    elif jogador == 2:
        return 1

#Função recebe como parâmetros a variavel que representa o jogador, uma string para a coordenada da jogada que o jogador fez
#e a lista que representa o tabuleiro
#Adiciona a jogada no tabuleiro de acordo com a coordenada, e determinando se é X ou O referente ao jogador
#Função não retorna valor
def inseri_jogada(jogador,coordenada,tabuleiro):
    x = int(coordenada[0]) - 1
    y = int(coordenada[2]) - 1

    if jogador == 1:
        tabuleiro[y][x] = 1
    else:
        tabuleiro[y][x] = 2

#Função recebe como parâmetros uma string que é uma coordenada de jogada, e uma lista que representa o tabuleiro do jogo
#Verifica a coordenada de acordo com o estado atual do tabuleiro para ver se é uma jogada válida, ou seja, se a coordenada
#representa um espaço livre no jogo
#Função retorna 1 caso deu certo a jogada
#e 0 caso deu errado a jogada
def verifica_coordenada(coordenada, tabuleiro):
    x = int(coordenada[0]) - 1
    y = int(coordenada[2]) - 1

    if tabuleiro[y][x] == 0:
        return 1
    else:
        return 0

#Função recebe como parâmetro uma lista que representa o tabuleiro do jogo
#Verifica todas as condições de vitória do jogo
#Função retorna 0 caso não tenha condição vitória
#, 1 caso tenha terminado a partida e um jogador ganhou
#e 2 caso tenha dado velha
def verifica_status_tabuleiro(tabuleiro):
    parar = 0
    conta_0 = 0

    #verifica se deu velha
    for i in range(0, 3):
        for j in range(0, 3):
            if tabuleiro[i][j] == 0:
                conta_0 = 1
    if conta_0 == 0:
        parar = 10

    #verifica as linhas
    for i in range(0, 3):
        if (tabuleiro[i][0] == tabuleiro[i][1]) and ((tabuleiro[i][0] == tabuleiro[i][2]) and (tabuleiro[i][0] != 0)):
            parar = 1

    #verifica as colunas
    for j in range(0, 3):
        if (tabuleiro[0][j] == tabuleiro[1][j]) and ((tabuleiro[0][j] == tabuleiro[2][j]) and (tabuleiro[0][j] != 0)):
            parar = 1

    #verifica as diagonais
    if (tabuleiro[0][0] == tabuleiro[1][1]) and ((tabuleiro[0][0] == tabuleiro[2][2]) and (tabuleiro[0][0] != 0)):
        parar = 1

    if (tabuleiro[2][0] == tabuleiro[1][1]) and ((tabuleiro[2][0] == tabuleiro[0][2]) and (tabuleiro[2][0] != 0)):
        parar = 1

    if parar == 0:
        return 0
    elif parar == 10:
        return 2
    else:
        return 1





