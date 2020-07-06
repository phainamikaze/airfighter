import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Air Fighter")
icon = pygame.image.load("fighter-jet-icon.png")
pygame.display.set_icon(icon)

background = pygame.image.load('space.jpg')

playerImg = pygame.image.load('fighter-jet.png')
playerX = 375
playerY = 480

def player(x,y):
    screen.blit(playerImg,(x,y))


running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player(playerX,playerY)


    pygame.display.update()
    