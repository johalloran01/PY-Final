from cmath import rect
import pygame
from sys import exit
import math
import sprites

pygame.init()
#initialize pygame lib (must have)
clock = pygame.time.Clock()
hero = pygame.image.load('images\images\characters\player.png')

def screensetting():
    #screen window setting pixel x pixel
    #application NAME and ICON
    pygame.display.set_caption('Melden Ting')
    icon = pygame.image.load('dungeon-light.png')
    pygame.display.set_icon(icon)

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = hero 
        #self.rect = pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
    def main(self, screen):
        self.rect = pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
        screen.blit(self.image, self.rect)
        

class PlayerRanged:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 15
        self.angle = math.atan2(y - mouse_y, x - mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
    def main(self, screen):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        pygame.draw.circle(screen, "Black", (self.x, self.y), 5)


player = Player(400, 300, 32, 32)

screen_scroll = [0,0]

player_ranged= []

def loop():
    
    screen = pygame.display.set_mode((800,600))
    screensetting()
    running = True
    while running:
        screen.fill((0,150,0))
        player.main(screen)
        
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player_ranged.append(PlayerRanged(player.x, player.y, mouse_x, mouse_y))
 
        
        keys = pygame.key.get_pressed()
        
        pygame.draw.rect(screen, (255, 255, 255), (100-screen_scroll[0], 100-screen_scroll[1], 16, 16))
        
        if keys[pygame.K_a]:
            screen_scroll[0] -= 5
        
        if keys[pygame.K_d]:
            screen_scroll[0] += 5
        
        if keys[pygame.K_w]:
            screen_scroll[1] -= 5
        
        if keys[pygame.K_s]:
            screen_scroll[1] += 5

        for arrows in player_ranged:
            arrows.main(screen)


        clock.tick(60)
        pygame.display.update()



loop()
