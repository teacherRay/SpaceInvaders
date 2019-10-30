import pygame

#setup pygame
pygame.init()

#init screen and add title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('./images/icon.png')
pygame.display.set_icon(icon)

#screen size
screen = pygame.display.set_mode((800,640))

#load player
playerImg = pygame.image.load('./images/spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

#load enemy
enemyImg = pygame.image.load('./images/enemy.png')
enemyX = 370
enemyY = 50
enemyX_change = 0
enemyY_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

#game loop
running = True

while running:
    #screen background color
    screen.fill((0,0,0))
    #playerX-=.25
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
              if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                  playerX_change = 0 

    playerX += playerX_change 

    #impose screen boundaries
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736
        
    if enemyX < 0:
        enemyX = 0
    elif enemyX > 736:
        enemyX = 736    
    

    #update player location
    player(playerX,playerY)

    #update player location
    enemy(enemyX,enemyY)

    #update screen
    pygame.display.update()

