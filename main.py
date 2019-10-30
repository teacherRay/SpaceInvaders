import pygame

#setup pygame
pygame.init()

#init screen and add title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('./images/ufo.png')
pygame.display.set_icon(icon)

#screen size
screen = pygame.display.set_mode((800,640))

playerImg = pygame.image.load('./images/spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y))

#game loop
running = True

while running:
    #screen background color
    screen.fill((0,0,0))
    #playerX-=.25
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print('hello')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
              if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                  playerX_change = 0 

    playerX += playerX_change 

    if playerX < 0:
        playerX = 0
    if playerX > 740:
        playerX = 740

    player(playerX,playerY)

    #update screen
    pygame.display.update()

