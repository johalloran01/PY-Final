import pygame
from settings import *
from support import import_folder


screen = pygame.display.set_mode((100, 100))


class RosenSheet():
	def __init__(self, image):
		self.sheet = image

	def get_image(self, frame, width, height, scale):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))

		return image

'''def draw_speech_bubble(screen, text, text_colour, bg_colour, pos, size):

    font = pygame.font.SysFont('comicsansms', size)
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

class NPCOne(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image_left = pygame.image.load('../graphics/monsters/rosen/idle/0.png').convert_alpha()
		self.image_right = pygame.transform.flip(self.image_left, True, False)
		self.image = pygame.Surface(self.image_left.get_size(), pygame.SRCALPHA)

		self.image.blit(self.image_left, (0, 0))
		self.rect = self.image.get_rect(topleft = pos)
		self.status = 'left'




	def draw(self, screen):
		screen.blit(self.image, self.rect.topleft)
		draw_speech_bubble(screen, "Hello Player", (255, 255, 0), (175, 175, 0), self.rect.midtop, 25)