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
                print("Left arrow key is pressed")
            if event.key == pygame.K_RIGHT:
                print("Right arrow key is pressed")
        if event.type == pygame.KEYUP:
              if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                  print("Key stroke has been released")      
    player(playerX,playerY)

    #update screen
    pygame.display.update()

