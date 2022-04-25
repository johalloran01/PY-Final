import pygame 
from settings import *
from support import import_folder

screen = pygame.display.set_mode((WIDTH, HEIGTH))

'''def draw_speech_bubble(screen, text, text_colour, bg_colour, pos, size):

    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, text_colour)
    text_rect = text_surface.get_rect(midbottom=pos)

    # background
    bg_rect = text_rect.copy()
    bg_rect.inflate_ip(10, 10)

    # Frame
    frame_rect = bg_rect.copy()
    frame_rect.inflate_ip(4, 4)

    pygame.draw.rect(screen, text_colour, frame_rect)
    pygame.draw.rect(screen, bg_colour, bg_rect)
    screen.blit(text_surface, text_rect)'''




class Player(pygame.sprite.Sprite):

	def __init__(self,pos,groups,obstacle_sprites):
		super().__init__(groups)
		self.image = pygame.image.load('../graphics/playertest/left/left 1.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-10)

		# graphics setup
		self.import_player_assets()
		self.status = 'left'
		self.frame_index = 0
		self.animation_speed = 0.10

		# movement
		self.direction = pygame.math.Vector2()
		self.speed = 2
		self.attacking = False
		self.attack_cooldown = 500
		self.attack_time = None
		self.obstacle_sprites = obstacle_sprites

	def import_player_assets(self):
		character_path = '../graphics/playertest/'
		self.animations = {
			'left':[],'right':[],'left_idle':[],'right_idle':[],'left_attack':[],'right_attack':[]
		}
		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_folder(full_path)

	def input(self):
		keys = pygame.key.get_pressed()
		# movement input
		if not self.attacking:
			if keys[pygame.K_UP] or keys[pygame.K_w]:
				self.direction.y = -1
			# self.status = 'up'
			elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
				self.direction.y = 1
			# self.status = 'down'
			else:
				self.direction.y = 0

			if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
				self.direction.x = 1
				self.status = 'right'
			elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
				self.direction.x = -1
				self.status = 'left'
			else:
				self.direction.x = 0
			# attack input
			if keys[pygame.K_SPACE]:
				self.attacking = True
				self.attack_time = pygame.time.get_ticks()
				print('attacking')

	def get_status(self):
		# idle status
		if self.direction.x == 0 and self.direction.y == 0:
			if not 'idle' in self.status and not 'attack' in self.status:
				self.status = self.status + '_idle'
		if self.attacking:
			self.direction.x = 0
			self.direction.y = 0
			if not 'attack' in self.status:
				if 'idle' in self.status:
					# ovewrite idle
					self.status = self.status.replace('_idle', '_attack')
				else:
					self.status = self.status + '_attack'
		else:
			if 'attack' in self.status:
				self.status = self.status.replace('_attack', '')

	def move(self, speed):
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.hitbox.x += self.direction.x * speed
		self.collision('horizontal')
		self.hitbox.y += self.direction.y * speed
		self.collision('vertical')
		self.rect.center = self.hitbox.center

	def collision(self, direction):
		if direction == 'horizontal':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.x > 0:  # moving right
						self.hitbox.right = sprite.hitbox.left
					if self.direction.x < 0:  # moving left
						self.hitbox.left = sprite.hitbox.right

		if direction == 'vertical':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.y > 0:  # moving down
						self.hitbox.bottom = sprite.hitbox.top
					if self.direction.y < 0:  # moving up
						self.hitbox.top = sprite.hitbox.bottom

	def cooldowns(self):
		current_time = pygame.time.get_ticks()
		if self.attacking:
			if current_time - self.attack_time >= self.attack_cooldown:
				self.attacking = False

	def animate(self):
		animation = self.animations[self.status]

		# loop over frame index
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0

		# set the image
		self.image = animation[int(self.frame_index)]
		self.rect = self.image.get_rect(center=self.hitbox.center)

	def update(self):
		self.input()
		self.cooldowns()
		self.get_status()
		self.animate()
		self.move(self.speed)










