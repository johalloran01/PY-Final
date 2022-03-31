import pygame
pygame.init()
#initialize pygame lib (must have)


def screensetting():
    #screen window setting pixel x pixel
    screen = pygame.display.set_mode((800,600))
    #application NAME and ICON
    pygame.display.set_caption('DEMO')
    icon = pygame.image.load('sword.png')
    pygame.display.set_icon(icon)


def loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False

screensetting()
loop()

