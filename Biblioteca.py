# Biblioteca de funções
import random

import pygame, sys
from pygame.locals import *
from random import randint

#Lista de cores
FloralWhite=(255,250,240)#branco
DarkSlateGray=(047,079,079)#verde/cinza
SlateGray=(112,128,144)#azul/cinza
DeepSkyBlue=(000,191,255)#azul suave, céu
SteelBlue=(070,130,180)#azul, escuro
SeaGreen=(046,139,087)#verde
Firebrick=(178,34,034)#vermelho

#Tamanho da tela
comprimento=500
altura=500

#Direccoes
CIMA = 8
BAIXO = 2
ESQUERDA=4
DIREITA=6

#Quadrado
#funcao rect(X, Y, largura, altura)
#Snake
snake = [[30,120],[10,120]]

cabeca = [30,120] 

x=randint(0,20)
y=randint(0,19)

comida = 0
while True:
    x1=randint(0,20)
    y1=randint(0,17)
    comidaXY=[int(x1*20)+10,int(y1*20)+120]
    if snake.count(comidaXY)==0:
        comida=1
        break
