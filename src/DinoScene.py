# The Scene for the core #DinosaursInSpace game. 
# TODO: Is this just for 1 player? AKA, are modes part of this scene, or new scene?


import PhysicsDebug
import Entity
import Ship
import InputWatcher
import CoreApp
import PiTweener
import pygame
import EntityDrawComponent
import Box2D
import random
import sys

class DinoScene():
    def __init__(self):
        self.debugRenderer = PhysicsDebug.DebugRenderer()
        self.ship = Ship.Ship()
        self.entityList = []
        self.debugFlag = False
        
        # TODO: A class to load all this shit up right. - Bey gimme a handskie on this one. 
        pygame.mixer.music.load("../res/Egypt Theme 1.mp3")
        pygame.mixer.music.play(-1)
        self.score_font = pygame.font.Font(None,100)
        # Not a sexual handskie
        
        self.background = pygame.image.load("../res/background.png").convert_alpha()
        width = 16
        height = 3.7
        for i in range(30):
            ground_body=CoreApp.world.CreateKinematicBody(
                position=(-i * width + 10,0),
                shapes=Box2D.b2PolygonShape(box=(width/2, height/2), density=1000000, friction=1), #TODO: What should my actual floor values be? - CP
                )
            ground_body.linearVelocity= (4,0)  
            
            entity = Entity.Pyramid((-i * width + 10,10))
            self.entityList.append(entity)
            
            mentity = Entity.Human((-i * width + 20 ,3))
            self.entityList.append(mentity)
            
            horsity = Entity.Horse((-i * width + 29.5 ,4))
            self.entityList.append(horsity)
            mentity = Entity.Human((-i * width + 30 ,5))
            self.entityList.append(mentity)
        
        
    # Yield drops - mostly just learning yields - CP
        self.dropper = yieldThatShit(self.entityList)


        
    def update(self, dt):
        InputWatcher.update()
        self.ship.update(dt)
        
        if InputWatcher.wasPressed(pygame.K_SPACE):
            entity = Entity.EntityList[self.dropper.next()](self.ship.getWorldDropPosition())
            entity.applyImpulse(self.ship.getWorldVelocity())
            self.entityList.append(entity)
            
        if InputWatcher.wasPressed(pygame.K_d):
            self.debugFlag = not self.debugFlag
            
        if InputWatcher.wasPressed(pygame.K_ESCAPE):
            sys.exit()
        
    def draw(self):
        CoreApp.screen.blit(self.background, (0,0))
        
        EntityDrawComponent.draw(self.entityList)
        
        # TODO: Score of game
        text = self.score_font.render(str(len(CoreApp.world.bodies)), True, pygame.Color(255,255,255))
        self.score_loc = text.get_rect(centerx=CoreApp.screen.get_width()/2)
        CoreApp.screen.blit(text, self.score_loc)
        #
        
        self.ship.draw()
        
        if self.debugFlag:
            self.debugRenderer.draw()
            
def yieldThatShit(entityList):
    count = 0
    while True:
        count = count + 1
        if count == len(Entity.EntityList):
            count = 0
        yield count