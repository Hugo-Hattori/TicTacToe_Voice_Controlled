import pygame
import sys
import time
from pygame.locals import *


#variáveis globais
SIMBOLO_XO = 'x'

VENCEDOR = None

EMPATE = None

TELA_LARGURA = 500
TELA_ALTURA = 500

FUNDO = (255, 255, 255) #cor padrão da janela

COR_LINHA = (0, 0, 0) #cor das linhas divisórias

TABULEIRO = [[None*3], [None*3], [None*3]]