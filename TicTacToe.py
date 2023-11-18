import pygame
import sys
import time
from pygame.locals import *
import os


#variáveis globais
JOGADOR_XO = 'x'

VENCEDOR = None

EMPATE = None

TELA_LARGURA = 500
TELA_ALTURA = 500

COR_FUNDO = (255, 255, 255) #cor padrão da janela

COR_LINHA = (0, 0, 0) #cor das linhas divisórias

TABULEIRO = [[None]*3, [None]*3, [None]*3]

#inicializando janela
pygame.init()

#configurações
fps = 30
relogio = pygame.time.Clock()
tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA), 0, 32)
pygame.display.set_caption('Tic Tac Toe')

#carregando imagens
IMAGEM_BACKGROUND = pygame.image.load((os.path.join('imgs', 'malha3x3.png')))
IMAGEM_X = pygame.image.load((os.path.join('imgs', 'simbolo-x.png')))
IMAGEM_O = pygame.image.load((os.path.join('imgs', 'simbolo-o.png')))

#redimensionando imagens
IMAGEM_BACKGROUND = pygame.transform.scale(IMAGEM_BACKGROUND, (TELA_LARGURA, TELA_ALTURA))
IMAGEM_X = pygame.transform.scale(IMAGEM_X, (80, 80))
IMAGEM_O = pygame.transform.scale(IMAGEM_O, (80, 80))


def desenhar_tela():
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    pygame.display.update()
    time.sleep(3)
    tela.fill(COR_FUNDO)

    #desenhando linhas verticais
    pygame.draw.line(tela, COR_LINHA, (TELA_LARGURA/3, 0), (TELA_LARGURA/3, TELA_ALTURA), 7)
    pygame.draw.line(tela, COR_LINHA, (TELA_LARGURA/3 * 2, 0), (TELA_LARGURA/3 * 2, TELA_ALTURA), 7)

    #desenhando linhas horizontais
    pygame.draw.line(tela, COR_LINHA, (0, TELA_ALTURA/3), (TELA_LARGURA, TELA_ALTURA/3), 7)
    pygame.draw.line(tela, COR_LINHA, (0, TELA_ALTURA/3 * 2), (TELA_LARGURA, TELA_ALTURA/3 * 2), 7)


def desenhar_status():

    if VENCEDOR == None:
        mensagem = f'Turno do jogador {JOGADOR_XO.upper()}'
    else:
        mensagem = f'Jogador {VENCEDOR} venceu!'
    if EMPATE:
        mensagem = 'O jogo empatou.'

    fonte = pygame.font.SysFont('arial', 30)
    texto = fonte.render(mensagem, 1, COR_FUNDO)
    retangulo = ((0, 400), (500, 100)) #((left, top), (width, height))
    tela.fill(COR_LINHA, retangulo)
    rect_texto = texto.get_rect(center=(TELA_LARGURA/2, 450))
    tela.blit(texto, rect_texto)
    pygame.display.update()
