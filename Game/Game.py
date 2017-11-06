import pygame, sys, os, math
from pygame.locals import *
from random import randint

from SpriteHelper import SpriteSheet, Animation
from pkg_resources import compatible_platforms



WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
GAMENAME = "Platformer"
FRAMERATE = 60
BGCOLOR = (255,255,255)

        
class Drawable:
    x = 0
    y = 0
    collider = None
    animations = {}
    state = None
    vX = 0
    vY = 0
    def __init__(self):
        pass
    def draw(self):
        pass  
    def getCollider(self):
        return self.animations[self.state].get_rect()
    
class Player(Drawable):
    lives = 2
    def __init__(self,images,x,y):
        pass
    def jump(self):
        pass
    def move(self,direction):  #1 is right, -1 is left
        pass
    def die(self):
        pass

class Enemy(Drawable):
    def __init__(self):
        pass
    def move(self,delta):
        pass
    
class Platform(Drawable):
    def __init__(self):
        pass
            
class Level:
    platforms = []
    enemies = []
    def __init__(self):
        pass
    def draw(self,delta):
        for platform in self.platforms:
            platform.draw(delta)
        for enemy in self.enemies:
            enemy.draw(delta)


class Game:
    ##########CLASS VARIABLES##########
    player = None
    levels = []
    score = 0
    playing = False
    bg = None
    clock = None
    
    ##########CONSTRUCTOR##########
    def __init__(self):
        pygame.init()
        clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
        pygame.display.set_caption(GAMENAME)
        player = self.buildPlayer()
        
        
    
    def process(self,delta):
        pass
    
    def main(self):
        playing = True
        
    
    def checkInput(self):
        pass
    
    def gameOver(self):
        pass
    
    def buildPlayer(self):
        return Player()
    
    ##########MAIN FUNCTION##########
    def main(self):
        playing = True
        pygame.init()
        clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
        pygame.display.set_caption(GAMENAME)
        playerSpriteSheet = SpriteSheet("p2_spritesheet.png")
        playerStanding = playerSpriteSheet.get_image(355,0,70,90)
        playerStandingRight = Animation(
            "standingRight",[playerStanding],1,False,False)
        playerStandingLeft = playerStandingRight.getFlippedOverY("standingLeft")
        w2 = playerSpriteSheet.get_image(70,0,70,90)
        w3 = playerSpriteSheet.get_image(140,0,70,90)
        w4 = playerSpriteSheet.get_image(210,0,70,90)
        w5 = playerSpriteSheet.get_image(280,0,70,90)
        w1 = playerSpriteSheet.get_image(0,0,70,90)
        playerWalking = [w1,w2,w3,w4,w5]
        playerWalkingRight = Animation("walkingRight",playerWalking,10,True,False)
        playerWalkingLeft = playerWalkingRight.getFlippedOverY()
        jumpingRight = playerSpriteSheet.get_image(70*7,90*2,70,90)
        playerJumpingRight = Animation([jumpingRight],1,False,False)
        playerJumpingLeft = playerJumpingRight.getFlippedOverY()
        
        playerImageRect = playerStanding.get_rect()
        centerX = WINDOWWIDTH/2-(playerImageRect.width/2)
        centerY = WINDOWHEIGHT/2
        self.player = Player(playerImages,centerX,centerY)
        ##########GAME LOOP##########
        while playing:
            delta = clock.tick(FRAMERATE)
            
            ##########EVENT HANDLING##########
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit()
                if event.type == KEYDOWN:
                    if event.key==K_LEFT:
                        self.player.startWalking(2)
                    elif event.key==K_RIGHT:
                        self.player.startWalking(1)
                    elif event.key==K_SPACE:
                        self.player.jump()
                else:
                    self.player.stopWalking()
            ##################################
                    
            self.processLogic(delta)
            self.drawScreen(delta)
            pygame.display.flip()
    
    ##########MAKES CHANGES FROM LAST FRAME##########
    def processLogic(self,delta):
        self.player.process(delta)
    
    ##########DRAWS THE FRAME##########
    def drawScreen(self,delta):
        self.surface.fill(BGCOLOR)
        self.player.draw(self.surface,delta)
    def quit(self):
        pygame.quit()
        sys.exit()
        
##########STARTS EVERYTHING##########
if __name__=='__main__':
    game = Game()
    game.main()