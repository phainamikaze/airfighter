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
playerX_change = 0
playerY_change = 0
player_change_speed = 3
def player(x,y):
    screen.blit(playerImg,(x,y))


running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = player_change_speed*-1
            if event.key == pygame.K_RIGHT:
                playerX_change = player_change_speed
            if event.key == pygame.K_UP:
                playerY_change = player_change_speed*-1
            if event.key == pygame.K_DOWN:
                playerY_change = player_change_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:    
                playerY_change = 0
    playerX += playerX_change
    playerY += playerY_change
    if playerX<=0 :
        playerX = 0
    elif playerX>=736:
        playerX = 736
    if playerY<=0 :
        playerY = 0
    elif playerY>=536:
        playerY = 536
    player(playerX,playerY)


    pygame.display.update()
    