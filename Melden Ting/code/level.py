import pygame 
from settings import *
from tile import Tile
from player import Player
from npc import NPCOne
from debug import debug
from support import *

class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

	def create_map(self):
		layouts = {
			'boundary' : import_csv_layout('../Tile map/map test._FloorBlocks.csv'),

		}

		graphics = {
			'grass': import_folder('../graphics/Pixel Art Top Down - Basic/Texture')
		}

		for style, layout in layouts.items():
			for row_index,row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != '-1':
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if style =='boundary':
							Tile((x,y),[self.obstacle_sprites],'invisible')


		self.player = Player((310, 150), [self.visible_sprites], self.obstacle_sprites)
		self.npc = NPCOne((340,200),[self.visible_sprites])

	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)

		self.visible_sprites.update()
		debug(self.player.status)


class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		# general setup 
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

		# create the floor
		self.floor_surf = pygame.image.load('../graphics/map_test.png').convert()
		self.floor_rect = self.floor_surf.get_rect(topleft=(0,0))

	def custom_draw(self,player):

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# drawing the floor
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surf,floor_offset_pos)

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)


