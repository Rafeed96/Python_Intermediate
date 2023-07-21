# import packages
import pygame
import math

pygame.init()

WIDTH = 900
HEIGHT = 950
screen = pygame.display.set_mode([WIDTH,HEIGHT])
timer = pygame.font.Font('freesanbold.ttf', 20)
level = boards
color = 'blue'
PI = math.pi



def draw_board():
    num1 = ((HEIGHT -50) // 32)
    num2 = (WIDTH // 30)

    for i in range(len(level)):
        for j in range(len(level[i])):
            