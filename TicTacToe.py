import pygame
import sys
import time
from pygame.locals import *
import os


#variáveis globais
SIMBOLO_XO = 'x'

VENCEDOR = None

EMPATE = None

TELA_LARGURA = 500
TELA_ALTURA = 500

FUNDO = (255, 255, 255) #cor padrão da janela

COR_LINHA = (0, 0, 0) #cor das linhas divisórias

TABULEIRO = [[None*3], [None*3], [None*3]]

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