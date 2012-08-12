import PhysicsDebug
import Entity
import Ship
import InputWatcher
import CoreApp
import pygame
import EntityDrawComponent
import random

class DinoScene():
    def __init__(self):
        self.debugRenderer = PhysicsDebug.DebugRenderer()
        self.ship = Ship.Ship()
        self.entityList = []
        self.background = pygame.image.load("../res/bg/background.png").convert_alpha()
        
    def update(self, dt):
        InputWatcher.update()
        self.ship.update(dt)
        self.debugRenderer.update()
        
        if InputWatcher.wasPressed(pygame.K_SPACE):
            # HACK  CP
            entity = Entity.EntityList[random.randint(1,4)](self.ship.getWorldDropPosition())
            entity.applyImpulse(self.ship.getWorldVelocity())
            self.entityList.append(entity)

    def draw(self):
        CoreApp.screen.blit(self.background, (0,0))
        EntityDrawComponent.draw(self.entityList)
        self.ship.draw()
        self.debugRenderer.draw()