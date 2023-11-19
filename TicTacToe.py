import pygame
import sys
import time
from pygame.locals import *
import os


#variáveis globais
JOGADOR_XO, VENCEDOR, EMPATE, TELA_LARGURA, TELA_ALTURA = 'x', None, False, 500, 500

COR_FUNDO = (255, 255, 255) #cor padrão da janela

COR_LINHA = (0, 0, 0) #cor das linhas divisórias

TABULEIRO = [[None]*3, [None]*3, [None]*3]

#inicializando janela
pygame.init()

#configurações
fps = 30
relogio = pygame.time.Clock()
tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA + 100), 0, 32)
pygame.display.set_caption('Tic Tac Toe')

#carregando imagens
IMAGEM_BACKGROUND = pygame.image.load((os.path.join('imgs', 'white_square.png')))
IMAGEM_X = pygame.image.load((os.path.join('imgs', 'simbolo-x.png')))
IMAGEM_O = pygame.image.load((os.path.join('imgs', 'simbolo-o.png')))

#redimensionando imagens
IMAGEM_BACKGROUND = pygame.transform.scale(IMAGEM_BACKGROUND, (TELA_LARGURA, TELA_ALTURA))
IMAGEM_X = pygame.transform.scale(IMAGEM_X, (80, 80))
IMAGEM_O = pygame.transform.scale(IMAGEM_O, (80, 80))


def desenhar_tela():
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    pygame.display.update()
    tela.fill(COR_FUNDO)

    #desenhando linhas verticais
    pygame.draw.line(tela, COR_LINHA, (TELA_LARGURA/3, 0), (TELA_LARGURA/3, TELA_ALTURA), 7)
    pygame.draw.line(tela, COR_LINHA, (TELA_LARGURA/3 * 2, 0), (TELA_LARGURA/3 * 2, TELA_ALTURA), 7)

    #desenhando linhas horizontais
    pygame.draw.line(tela, COR_LINHA, (0, TELA_ALTURA/3), (TELA_LARGURA, TELA_ALTURA/3), 7)
    pygame.draw.line(tela, COR_LINHA, (0, TELA_ALTURA/3 * 2), (TELA_LARGURA, TELA_ALTURA/3 * 2), 7)


def desenhar_status():
    global VENCEDOR, EMPATE

    if VENCEDOR == None:
        mensagem = f'Turno do jogador {JOGADOR_XO.upper()}'
    else:
        mensagem = f'Jogador {VENCEDOR} venceu!'
    if EMPATE:
        mensagem = 'O jogo empatou.'

    fonte = pygame.font.SysFont('arial', 30)
    texto = fonte.render(mensagem, 1, COR_FUNDO)
    retangulo = ((0, 500), (500, 100)) #((left, top), (width, height))
    tela.fill(COR_LINHA, retangulo)
    rect_texto = texto.get_rect(center=(TELA_LARGURA/2, 550))
    tela.blit(texto, rect_texto)
    pygame.display.update()


def checar_vitoria():
    global TABULEIRO, VENCEDOR, EMPATE

    #checar vitória pelas linhas
    for linha in range(len(TABULEIRO)):
        if (TABULEIRO[linha][0] == TABULEIRO[linha][1] == TABULEIRO[linha][2]) and (TABULEIRO[linha][0] is not None):
            VENCEDOR = TABULEIRO[linha][0] #vai pegar o X ou O e idenficar ele como vencedor
            pygame.draw.line(tela, (250, 0, 0),
                             (0, (linha + 1) * TELA_ALTURA / 3 - TELA_ALTURA / 6 - 3),
                             (TELA_LARGURA, (linha + 1) * TELA_ALTURA / 3 - TELA_ALTURA / 6 - 3),
                             4)

    #checar vitória pelas colunas
    for coluna in range(len(TABULEIRO)):
        if (TABULEIRO[0][coluna] == TABULEIRO[1][coluna] == TABULEIRO[2][coluna]) and (TABULEIRO[0][coluna] is not None):
            VENCEDOR = TABULEIRO[0][coluna]
            pygame.draw.line(tela, (250, 0, 0),
                             ((coluna + 1) * TELA_LARGURA / 3 - TELA_LARGURA / 6 - 3, 0),
                             ((coluna + 1) * TELA_LARGURA / 3 - TELA_LARGURA / 6 - 3, TELA_ALTURA), 4)


    #checar vitória pelas diagonais
    if (TABULEIRO[0][0] == TABULEIRO[1][1] == TABULEIRO[2][2]) and (TABULEIRO[0][0] is not None):
        VENCEDOR = TABULEIRO[0][0]
        pygame.draw.line(tela, (250, 0, 0), (50, 50), (450, 450), 5)

    if (TABULEIRO[0][2] == TABULEIRO[1][1] == TABULEIRO[2][0]) and (TABULEIRO[0][2] is not None):
        VENCEDOR = TABULEIRO[0][2]
        pygame.draw.line(tela, (250, 0, 0), (40, 450), (440, 50), 5)

    #checar por empate
    EMPATE = all(all(linha) for linha in TABULEIRO) if VENCEDOR is None else False
    # obs1: verifica se todas as linhas e todos os conteúdos dentro da linha estão preenchidos
    # obs2: EMPATE irá receber True ou False

    desenhar_status()


def desenhar_XO(linha, coluna):
    global TABULEIRO, JOGADOR_XO

    pos_y = 40 if linha == 1 else (TELA_ALTURA/3 + 40 if linha == 2 else TELA_ALTURA/3 * 2 + 40)
    pos_x = 40 if coluna == 1 else (TELA_LARGURA/3 + 40 if coluna == 2 else TELA_LARGURA/3 * 2 + 40)

    #substitui X ou O na matriz do TABULEIRO, de acordo com o jogador da vez e de acordo com a posição
    TABULEIRO[linha-1][coluna-1] = JOGADOR_XO

    if JOGADOR_XO == 'x':
        tela.blit(IMAGEM_X, (pos_x, pos_y))
        JOGADOR_XO = 'o' #troca de jogador
    else:
        tela.blit(IMAGEM_O, (pos_x, pos_y))
        JOGADOR_XO = 'x' #troca de jogador
    pygame.display.update()


def usuario_click():
    #pega coordenadas do click
    click_x, click_y = pygame.mouse.get_pos()

    #pega qual coluna foi clicado
    coluna = 1 if click_x < TELA_LARGURA/3 else (2 if click_x < TELA_LARGURA/3 * 2 else (3 if click_x < TELA_LARGURA else None))

    #pega qual linha foi clicado
    linha = 1 if click_y < TELA_ALTURA/3 else (2 if click_y < TELA_ALTURA/3 * 2 else (3 if click_y < TELA_ALTURA else None))

    #quando tivermos a linha e a coluna do clique e a posição onde foi clicado não for nula: desenha símbolo
    if linha and coluna and TABULEIRO[linha-1][coluna-1] is None:
        global JOGADOR_XO
        desenhar_XO(linha, coluna)
        checar_vitoria()


def resetar_jogo():
    global JOGADOR_XO, VENCEDOR, EMPATE, TABULEIRO

    time.sleep(3)
    JOGADOR_XO, EMPATE, VENCEDOR = 'x', False, None
    desenhar_tela()
    TABULEIRO = [[None]*3, [None]*3, [None]*3]


#Iniciando o jogo e Main Loop do jogo
desenhar_tela()
desenhar_status()

while(True):
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == MOUSEBUTTONDOWN:
            usuario_click()
            if (VENCEDOR or EMPATE):
                resetar_jogo()
        pygame.display.update()
        relogio.tick(fps)