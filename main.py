import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Air Fighter")
icon = pygame.image.load("aircraft.png")
pygame.display.set_icon(icon)

running = True
while running:
    screen.fill((255,255,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    