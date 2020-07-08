import pygame
import random 

pygame.init()
width = 500
height = 800
palyerSize = 64
enemySize = 64
screen = pygame.display.set_mode((width,height))

pygame.display.set_caption("Air Fighter")
icon = pygame.image.load("fighter-jet-icon.png")
pygame.display.set_icon(icon)

background = pygame.image.load('space.jpg')

playerImg = pygame.image.load('fighter-jet.png')
playerX = (width/2)-(palyerSize/2)
playerY = height-100
playerX_change = 0
playerY_change = 0
player_change_speed = 3

enemyImg = []
enemyX = []
enemyY = []
enemyY_change = []
enemy_change_speed = 0.5
num_of_enemy = 1
max_enemy = 6

bulletImg = pygame.image.load('missile.png')
bulletX = 0
bulletY = 0
bulletY_change = 3
bullet_change_speed = 1
bullet_state = "ready"
def player(x,y):
    screen.blit(playerImg,(x,y))


def enemy(Img,x,y):
    screen.blit(Img,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    print(x,y)
    screen.blit(bulletImg,(x,y))

running = True
count = 1
while running:
    if count%500==0:
        count=1
        if num_of_enemy < max_enemy:
            num_of_enemy+=1
    for i in range(num_of_enemy):
        enemyImg.append(pygame.image.load('alien.png'))
        enemyX.append(random.randint(0,width-enemySize))
        enemyY.append(enemySize*-1)
        enemyY_change.append(enemy_change_speed)
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
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX+20
                    bulletY = playerY
                    fire_bullet(bulletX,bulletY)

                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:    
                playerY_change = 0
    playerX += playerX_change
    playerY += playerY_change
    if playerX<=0 :
        playerX = 0
    elif playerX>=(width-palyerSize):
        playerX = width-palyerSize
    if playerY<=0 :
        playerY = 0
    elif playerY>=(height-palyerSize):
        playerY = height-palyerSize
    player(playerX,playerY)
    for i in range(num_of_enemy):
        enemyY[i]+=enemyY_change[i]
        if enemyY[i]>=height:
            enemyY[i]=enemySize*-1
        enemy(enemyImg[i],enemyX[i],enemyY[i])
    if bullet_state == "fire":
        bulletY -= bulletY_change
        fire_bullet(bulletX,bulletY)
        if bulletY <=0 :
            bullet_state = "ready"
        
        

    count+=1
    pygame.display.update()
    