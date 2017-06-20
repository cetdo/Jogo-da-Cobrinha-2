# Biblioteca de funções
import random

import pygame, sys
from pygame.locals import *
from random import randint

#Lista de cores
FloralWhite=(255,250,240)#branco
DarkSlateGray=(47,79,79)#verde/cinza
SlateGray=(112,128,144)#azul/cinza
DeepSkyBlue=(000,191,255)#azul suave, céu
SteelBlue=(70,130,180)#azul, escuro
SeaGreen=(46,139,87)#verde
Firebrick=(178,34,34)#vermelho

#Tamanho da tela
screen_length = 500
screen_high = 500

#Direccoes
up = 8
down = 2
left = 4
right = 6

#Quadrado
#funcao rect(X, Y, largura, altura)
#Snake
snake = [[30,120],[10,120]]

head = [30,120]

x = randint(0,20)
y = randint(0,19)

apple = 0

while True:
    x1 =randint(0,20)
    y1 =randint(0,17)
    comidaXY =[int(x1*20)+10,int(y1*20)+120]
    if snake.count(comidaXY)==0:
        apple = 1
        break
