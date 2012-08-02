import CoreApp
import Ship
import random

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
 
# TODO: This is a test Entity subclass    
class Box(Entity):
    def setUp(self, pos):
        box = CoreApp.world.CreateDynamicBody(position=pos)
        self.bodyList.append(box)
        box.CreatePolygonFixture(box=(random.uniform(0.4,0.5),random.uniform(0.0,0.5)), density=random.uniform(0.0,10), friction=random.uniform(0.0,0.1), restitution=random.uniform(0.0,1.0))

class Circle(Entity):
    def setUp(self, pos):
        box = CoreApp.world.CreateDynamicBody(position=pos)
        self.bodyList.append(box)
        box.CreateCircleFixture(radius=.5, density=0.5, friction=0.5, restitution=0.5)


# TODO: I'll need to think of the best way to solve the  (position=(pos[0] + 1, pos[1] + 1) ) 
#        problem below
class DoubleBox(Entity):
    def setUp(self, pos):
        box1 = CoreApp.world.CreateDynamicBody(position=pos)
        self.bodyList.append(box1)
        box1.CreatePolygonFixture(box=(0.4,0.5), density=2, friction=1, restitution=0.1)
        
        box2 = CoreApp.world.CreateDynamicBody (position=(pos[0] + 1, pos[1] + 1) )
        self.bodyList.append(box2)
        box2.CreatePolygonFixture(box=(0.6,0.2), density=992, friction=1, restitution=0.4)
        CoreApp.world.CreateRevoluteJoint(bodyA=box1, bodyB=box2, anchor=box1.worldCenter)
        #CoreApp.world.CreateWeldJoint(bodyA=box1,bodyB=box2, anchor= (box1.worldCenter + box2.worldCenter) / 2)