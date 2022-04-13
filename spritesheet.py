import pygame



class spritesheet (object): 
    def __init__(self, filename): 
        try:
            self.sheet = pygame.image.load(filename).convert()
        except(pygame.error, e):
            print("Unable to load spritesheet image: ", filename)
            raise(SystemExit, e) 
    
    #loading a specific image from a specific rectangle 
    def image_at(self, rectangle, colorKey = None): 
        #Loads image from x,y,x+offset,y+offset
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect, size).convert() 
        image.blit(self.sheet(0,0), rect)   
        if colorkey != None: 
            if colorkey is -1: 
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image 
    
    #load a bunch of images and return them as a list. 
    def images_at(self, rects, colorkey = None): 
        return [self.image_at(self, colorkey) for rect in rects]
    
    #load a strip of images
    def load_strip(self, rect, image_count, colorkey = None): 
        tups = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.image(tups, colorkey) 
    

        