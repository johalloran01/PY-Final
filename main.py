import pygame
import herosprite
import math
pygame.init()
#initialize pygame lib (must have)
clock = pygame.time.Clock()
screen_width = 800
screen_height = 600
screen_scroll = [0,0]

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = self 
        #self.rect = pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
    def main(self, screen):
        pygame.square(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))
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
player_ranged= []
player = Player(400, 300, 32, 32)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Spritesheets')

sprite_sheet_walkingr = pygame.image.load('walking.png').convert_alpha()
sprite_sheet0 = herosprite.SpriteSheet2(sprite_sheet_walkingr)

sprite_sheet_standing = pygame.image.load('player.png').convert_alpha()
sprite_sheet1 = herosprite.SpriteSheet(sprite_sheet_standing)

sprite_sheet_walkingl = pygame.image.load('Walking_Left.png').convert_alpha()
sprite_sheet2 = herosprite.SpriteSheet3(sprite_sheet_walkingl)

sprite_sheet_attackr = pygame.image.load('Attack_Right.png').convert_alpha()
sprite_sheet3 = herosprite.SpriteSheet4(sprite_sheet_walkingl)
BG = (255,255,255)

#animation list
hero_standing = []
hero_stands = 6
last_update = pygame.time.get_ticks()
animation_cooldown = 50
frame = 0

for x in range(hero_stands):
    hero_standing.append(sprite_sheet1.get_image(x, 48, 48, 2))
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

hero_walkingr = []
hero_walks = 6

hero_walkingl = []
hero_walk = 6

for x in range(hero_walks):
    hero_walkingr.append(sprite_sheet0.get_image2(x, 48, 48, 2))

for x in range(hero_walk):
    hero_walkingl.append(sprite_sheet2.get_image3(x, 48, 48, 2))

hero_attackr = []
hero_attack = 4

for x in range(hero_attack):
    hero_attackr.append(sprite_sheet3.get_image4(x, 48, 48, 2))

run = True
while run:

    #update background
    screen.fill(BG)

    #update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(hero_standing):
            frame = 0

    #show frame image
    
    mouse_x, mouse_y = pygame.mouse.get_pos()

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player_ranged.append(PlayerRanged(player.x, player.y, mouse_x, mouse_y))

    
    keys = pygame.key.get_pressed()
        
    pygame.draw.rect(screen, (0, 0, 0), (100-screen_scroll[0], 100-screen_scroll[1], 16, 16))
        
    if keys[pygame.K_a]:
        screen_scroll[0] -= 5
        screen.blit(hero_walkingl[frame], (350, 265))

    if keys[pygame.K_d]:
        screen_scroll[0] += 5
        screen.blit(hero_walkingr[frame], (350, 265))
    
    if keys[pygame.K_w]:
        screen_scroll[1] -= 5
        screen.blit(hero_walkingr[frame], (350, 265))
    
    if keys[pygame.K_s]:
        screen_scroll[1] += 5
        screen.blit(hero_walkingl[frame], (350, 265))
    
    if not keys[pygame.K_s] and not keys[pygame.K_w] and not keys[pygame.K_d] and not keys[pygame.K_a]:
        screen.blit(hero_standing[frame], (350, 250))
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time   
        if frame >= len(hero_standing):
                frame = 0

    for arrows in player_ranged:
        arrows.main(screen)
    

    pygame.display.update()