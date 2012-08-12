import CoreApp
import Ship
import random
import pygame

#TODO: Instead of manually creating a polygon fixture and all that it should be handy functions
#TODO: There needs to be a handy function to apply an impulse to all the bodies in a Entity

class Entity():
    def __init__(self, pos):
        self.bodyList = []
        self.setUp(pos)
    
    def setUp(self):
        pass
    
    def tearDown(self):
        for body in self.bodyList:
            CoreApp.world.DestroyBody(body)
            
    def update(self, dt):
        pass
    
    #TODO: Tom argues to put this outside of the Entity - He's prolly right. CP
    #         This will do for now for testing purps
    def applyImpulse(self, shipVelocity):
        for body in self.bodyList:
            impulse = list(shipVelocity)
            impulse[0] = impulse[0] * Ship.IMPULSE_FACTOR * body.mass
            impulse[1] = impulse[1] * Ship.IMPULSE_FACTOR * body.mass
            body.ApplyLinearImpulse(impulse, body.worldCenter)
 
#Below will be hack ass shit for First Playable - CP      
class DragonBall(Entity):
    def setUp(self, pos):
        self.image = pygame.image.load("../res/entity/dragonball.png").convert_alpha()
        ball = CoreApp.world.CreateDynamicBody(position=pos)
        self.bodyList.append(ball)
        ball.CreateCircleFixture(radius=.25, density=0.8, friction=0.5, restitution=0.45 )
        
class Hat(Entity):
    def setUp(self, pos):
        self.image = pygame.image.load("../res/entity/hat.png").convert_alpha()
        box1 = CoreApp.world.CreateDynamicBody(position=pos)
        self.bodyList.append(box1)
        box1.CreatePolygonFixture(box=(0.12,0.2), density=2, friction=1, restitution=0.1)
        
        
class Pyramid(Entity):
    def setUp(self, pos):
        self.image = pygame.image.load("../res/entity/pyramid.png").convert_alpha()
        box1 = CoreApp.world.CreateDynamicBody(position=pos)
        self.bodyList.append(box1)
        box1.CreatePolygonFixture(vertices=[(-1.8,-4.0), (1.8,-4.0), (0,-1.1)], density=10, friction=1, restitution=0.1)
        
                
class Shuriken(Entity):
    def setUp(self, pos):
        self.image = pygame.image.load("../res/entity/shuriken.png").convert_alpha()
        ball = CoreApp.world.CreateDynamicBody(position=pos)
        self.bodyList.append(ball)
        ball.CreateCircleFixture(radius=.2, density=0.5, friction=0.5, restitution=0.5)
                
class Eyeball(Entity):
    def setUp(self, pos):
        self.image = pygame.image.load("../res/entity/eyeball.png").convert_alpha()
        ball = CoreApp.world.CreateDynamicBody(position=pos)
        self.bodyList.append(ball)
        ball.CreateCircleFixture(radius=.2, density=0.5, friction=0.5, restitution=0.5)
        
class Horse(Entity):
    def setUp(self, pos):
        self.image = pygame.image.load("../res/entity/horse.png").convert_alpha()
        box1 = CoreApp.world.CreateDynamicBody(position=pos)
        self.bodyList.append(box1)
        box1.CreatePolygonFixture(box=(0.43,0.35), density=2, friction=1, restitution=0.1)        
        
class Human(Entity):
    def setUp(self, pos):
        self.image = pygame.image.load("../res/entity/human.png").convert_alpha()
        box1 = CoreApp.world.CreateDynamicBody(position=pos)
        box1.userData = "Human"
        self.bodyList.append(box1)
        box1.CreatePolygonFixture(box=(0.2,0.4), density=2, friction=1, restitution=0.1)

class Boulder(Entity):
    def setUp(self, pos):
        self.image = pygame.image.load("../res/entity/boulder.png").convert_alpha()
        ball = CoreApp.world.CreateDynamicBody(position=pos)
        self.bodyList.append(ball)
        ball.CreateCircleFixture(radius=1, density=5, friction=0.5, restitution=0.5)
        
class FireTruck(Entity):
    def setUp(self, pos):
        self.image = pygame.image.load("../res/entity/firetruck.png").convert_alpha()
        box1 = CoreApp.world.CreateDynamicBody(position=pos)
        self.bodyList.append(box1)
        box1.CreatePolygonFixture(box=(2.0,0.7), density=5, friction=1, restitution=0.1)

class Cow(Entity):
    def setUp(self, pos):
        self.image = pygame.image.load("../res/entity/cow.png").convert_alpha()
        box1 = CoreApp.world.CreateDynamicBody(position=pos)
        self.bodyList.append(box1)
        box1.CreatePolygonFixture(box=(0.5,0.42), density=2, friction=1, restitution=0.1)        
 
class Tire(Entity):
    def setUp(self, pos):
        self.image = pygame.image.load("../res/entity/tire.png").convert_alpha()
        ball = CoreApp.world.CreateDynamicBody(position=pos)
        self.bodyList.append(ball)
        ball.CreateCircleFixture(radius=.4, density=1, friction=0.5, restitution=0.7 )
 
class Football(Entity):
    def setUp(self, pos):
        self.image = pygame.image.load("../res/entity/football.png").convert_alpha()
        box1 = CoreApp.world.CreateDynamicBody(position=pos, angle=random.uniform(-0.2,0.2))
        self.bodyList.append(box1)
        box1.CreatePolygonFixture(box=(0.28,0.18), density=1, friction=0.01, restitution=0.7)
 
class UVicGameDev(Entity):
    def setUp(self, pos):
        self.image = pygame.image.load("../res/entity/uvicgamedev.png").convert_alpha()
        box1 = CoreApp.world.CreateDynamicBody(position=pos, angle=random.uniform(-0.2,0.2))
        self.bodyList.append(box1)
        box1.CreatePolygonFixture(box=(2.4,0.8), density=40, friction=0.5, restitution=0.5)
           

EntityList = [Tire, Eyeball, Shuriken, Hat, Horse, DragonBall, Boulder, FireTruck, Cow, Football, UVicGameDev]
        