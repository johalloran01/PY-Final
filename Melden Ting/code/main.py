import pygame, sys
from settings import *
from level import Level
from npc import *

class Game:
	def __init__(self):
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Melden Ting')
		self.clock = pygame.time.Clock()
		self.level = Level()
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('black')
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)


if __name__ == '__main__':
	game = Game()
	game.run()

rosen_sprite = pygame.image.load('rosen.png').convert_alpha()
rosen_sprite_sheet = npcsprite.RosenSheet(rosen_sprite)

rosen_standing = []
rosen_stands = 6
last_update = pygame.time.get_ticks()
animation_cooldown = 50
frame = 0

for x in range(rosen_stands):
	rosen_standing.append(rosen_sprite_sheet.get_image(x, 20, 23, 2))