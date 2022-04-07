import pygame
pygame.init()
#initialize pygame lib (must have)
#used to setup frame rate
clock = pygame.time.Clock()

def screensetting():
    #screen window setting pixel x pixel
    screen = pygame.display.set_mode((800,600))
    #application NAME and ICON
    pygame.display.set_caption('Melden Ting')
    #creates icon for window based on png file
    icon = pygame.image.load('dungeon-light.png')
    pygame.display.set_icon(icon)


def loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        pygame.display.update()
        clock.tick(60)


screensetting()
loop()
