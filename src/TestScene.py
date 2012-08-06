import CoreApp
import PhysicsDebug
import InputWatcher 
import pygame
import Ship
import Box2D
import Entity
import math
import random
import PiTweener

class TestScene():
    def __init__(self):
        self.debugRenderer = PhysicsDebug.DebugRenderer()
        
        self.ship = Ship.Ship()
        self.entityList = []
        
        self.face_image = pygame.image.load("../res/face.png").convert_alpha()
        
        # TODO: Test shit. Remove Later
        
        pygame.mixer.music.load("../res/Slowkemon.mp3")
        pygame.mixer.music.play(-1)
        
        
        self.poop_font = pygame.font.Font(None,100)
        
        width = 16
        height = 2
        for i in range(3):
            ground_body=CoreApp.world.CreateKinematicBody(
                position=(-i * width + 10,0),
                shapes=Box2D.b2PolygonShape(box=(width/2, height/2), density=1000000, friction=1), #TODO: What should my actual floor values be? - CP
                )
            ground_body.linearVelocity= (1,0)   
                
        self.tweener = PiTweener.Tweener()
            
    def update(self, dt):
        InputWatcher.update()
        self.ship.update(dt)
        for entity in self.entityList:
            entity.update(dt)
        
        self.tweener.update(dt)
            
        #if (InputWatcher.wasPressed(pygame.K_SPACE)):
            #self.tweener.add_tween(self.ship,self.ship.position[1]=30,tweenTime=5.0,tweenType=ship.tweener.OUT_QUAD )    
           # self.tweener.add_tween(self.ship, magic_num =random.uniform(100,500), tween_time=1000.0, tween_type=self.tweener.OUT_ELASTIC)
            
        if InputWatcher.wasPressed(pygame.K_a):
            entity = Entity.Circle(self.ship.getWorldDropPosition())
            entity.applyImpulse(self.ship.getWorldVelocity())
            
        if InputWatcher.wasPressed(pygame.K_q):
            new_sound = pygame.mixer.Sound("../res/Costanza.wav")
            new_sound.play()
            print pygame.mixer.get_num_channels()
            
            ##TEST TEST
        #Draw the five item boxes
        
        print len(CoreApp.world.bodies)
        for body in CoreApp.world:
            self.fart_image = pygame.transform.rotate(self.face_image, math.degrees(body.angle))
            pos = CoreApp.worldToPixels(body.worldCenter)
            CoreApp.screen.blit(self.fart_image, (pos[0] - self.fart_image.get_width()/2 , pos[1] - self.fart_image.get_height()/2) )
        
        #print CoreApp.world.bodies[-1].worldCenter

    def draw(self):
        self.debugRenderer.draw()
        self.ship.draw()
        
        text = self.poop_font.render(str(len(CoreApp.world.bodies)), True, pygame.Color(255,255,255))
        
        self.poop_loc = text.get_rect(centerx=CoreApp.screen.get_width() - 80)
        CoreApp.screen.blit(text, self.poop_loc)
        
        pass