import funcoes

# while para o funcionamento do programa todo
while 1:
    #começa o programa com um menu inicial
    funcoes.limpa_tela()
    comecar = funcoes.menu_inicial()
    #if and else para as duas opçoes do menu, começar o jogo ou sair o programa
    if comecar == 1:
        #inicialização de variáveis e do tabuleiro
        jogador = 2
        acabou = 0
        tabuleiro = []
        funcoes.inicializa_tabuleiro(tabuleiro)
        #while para rodar durante o funcionamento do jogo
        while acabou == 0:
            #funções para a operação do jogo, envolvendo pegar as jogadas de cada jogador e verificar se elas são validas
            jogador = funcoes.muda_jogador(jogador)
            funcoes.limpa_tela()
            funcoes.exibe_tabuleiro(tabuleiro, jogador)
            while 1:
                coordenada = funcoes.pega_coordenada()
                if funcoes.verifica_coordenada(coordenada, tabuleiro) == 1:
                    break
            funcoes.inseri_jogada(jogador,coordenada,tabuleiro)
            #a variavel "acabou" determina se o jogo acabou ou nao
            acabou = funcoes.verifica_status_tabuleiro(tabuleiro)
        funcoes.limpa_tela()
        funcoes.exibe_tabuleiro(tabuleiro, jogador)
        #diferentes mensagens no fim da partida para caso um jogador ganhou ou se deu velha
        if acabou == 1:
            print(f'\nVitória do Jogador {jogador}')
        elif acabou == 2:
            print('\nDeu Velha')
        a = input('Pressione enter para continuar...')
    elif comecar == 0:
        break
#mensagem de despedida após o fim do programa
funcoes.limpa_tela()
print('='*11)
print('!!! FLW !!!')
print('='*11)
