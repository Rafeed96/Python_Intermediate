import pygame

square = 20


gameBoard = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 8, 0, 1, 0, 1, 0, 1, 0, 1, 0, 8, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], #Halfway
    [0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],   
    [0, 8, 0, 1, 0, 1, 0, 1, 0, 1, 0, 8, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

(width, height) = (len(gameBoard) * square , len(gameBoard[0]) * square)
screen = pygame.display.set_mode((width,height))
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
