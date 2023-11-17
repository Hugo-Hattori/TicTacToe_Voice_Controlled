import pygame
import os


TELA_LARGURA = 500
TELA_ALTURA = 500

IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load((os.path.join('imgs', 'malha3x3.png'))))
IMAGEM_X = pygame.transform.scale2x(pygame.image.load((os.path.join('imgs', 'simbolo-x.png'))))
IMAGEM_O = pygame.transform.scale2x(pygame.image.load((os.path.join('imgs', 'simbolo-o.png'))))

pygame.font.init()
FONTE_TEXTO = pygame.font.SysFont('arial', 30)


class Simbolo_X:
    IMAGEM = IMAGEM_X

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x, self.y))


class Simbolo_O:
    IMAGEM = IMAGEM_O

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x, self.y))


def desenhar_tela(tela, simbolos_o, simbolos_x):
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    #desenhar X ou O de acordo com o comando
    pygame.display.update()


tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))