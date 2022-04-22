import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0,0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        
        return image
    
class SpriteSheet2():
    def __init__(self, image):
        self.sheet = image

    def get_image2(self, frame, width, height, scale):
        image2 = pygame.Surface((width, height)).convert_alpha()
        image2.blit(self.sheet, (0,0), (frame * width, 0, width, height))
        image2 = pygame.transform.scale(image2, (width * scale, height * scale))

        return image2

class SpriteSheet3():
    def __init__(self, image):
        self.sheet = image

    def get_image3(self, frame, width, height, scale):
        image3 = pygame.Surface((width, height)).convert_alpha()
        image3.blit(self.sheet, (0,0), (frame * width, 0, width, height))
        image3 = pygame.transform.scale(image3, (width * scale, height * scale))

        return image3

class SpriteSheet4():
    def __init__(self, image):
        self.sheet = image

    def get_image4(self, frame, width, height, scale):
        image4 = pygame.Surface((width, height)).convert_alpha()
        image4.blit(self.sheet, (0,0), (frame * width, 0, width, height))
        image4 = pygame.transform.scale(image4, (width * scale, height * scale))

        return image4