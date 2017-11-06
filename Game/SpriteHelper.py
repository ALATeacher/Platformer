import pygame

class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """
    # Colors
    BLACK    = (   0,   0,   0) 
    WHITE    = ( 255, 255, 255) 
    BLUE     = (   0,   0, 255)
 
    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """
 
        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()
 
 
    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
 
        # Create a new blank image
        image = pygame.Surface([width, height]).convert()
 
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
 
        # Assuming black works as the transparent color
        image.set_colorkey(self.BLACK)
 
        # Return the image
        return image

class UniformSpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """
 
    def __init__(self, file_name,width,height):
        """ Constructor. Pass in the file name of the sprite sheet. """
        
        # Colors
        BLACK    = (   0,   0,   0) 
        WHITE    = ( 255, 255, 255) 
        BLUE     = (   0,   0, 255)
         
        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()
        self.width = width
        self.height = height
 
 
    def get_image(self, x, y):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
        # Create a new blank image
        x = x*width
        y = y*width
        image = pygame.Surface([self.width, self.height]).convert()
 
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
 
        # Assuming black works as the transparent color
        image.set_colorkey(self.BLACK)
 
        # Return the image
        return image
    

class Animation:
    def __init__(self,name,images,fps,loop=True,reversible=False):
        self.images = images
        self.loop = loop
        self.reversible = reversible
        self.direction = 1
        self.fps = fps
        self.timer = 0
        self.index = 0
        self.name = name
    def tick(self,delta):
        self.timer+=delta
        if self.timer>=1/self.fps:
            self.timer = 0
            self.index+=self.direction
            if self.index>=len(self.images):
                if self.loop:
                    if self.reversible:
                        self.direction=-self.direction
                        self.index+=self.direction
                        return True
                    else:
                        self.index = 0
                        return True
                else:
                    return False
            elif self.index<0:
                if self.loop:
                    self.direction = -self.direction
                    self.index+=self.direction
                    return True
                else:
                    return False
    def getImage(self,delta):
        changing = self.tick(delta)
        if changing:
            return self.images[self.index]
        else:
            return self.images[0]
    def getFlippedOverY(self,newName):
        imagesLeft = []
        for x in self.images:
            imagesLeft.append(pygame.transform.flip(x, True, False))
        return Animation(newName,imagesLeft,self.fps,self.loop,self.reversible)
