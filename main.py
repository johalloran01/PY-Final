import pygame
#initialize the pygame lib
pygame.init()

def template(): #game window
    #set the window of game pixel x pixel can be change depends on the map
    screen = pygame.display.set_mode((800,600))
    #icon and title setting for application
    icon = pygame.image.load('put your file name here')
    pygame.display.set_icon(icon)
    pygame.display.set_caption("NAME OF THE GAME")

#GAME LOOP
def looper():   #creating a function for future use
    running = True #putting the game in infinite loop
    while running:
        for event in pygame.event.get():   #running all event in game
            if event.type == pygame.quit(): #clicking cross on application window will close the app
                running = False #break out of loop and close the program

template()
looper()




