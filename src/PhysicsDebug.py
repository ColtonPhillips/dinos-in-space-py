
from Box2D import b2_staticBody, b2_dynamicBody, b2_kinematicBody, b2Shape
import pygame
import CoreApp

bodyColors = {
    b2_staticBody    : (255,255,255,255),
    b2_dynamicBody   : (127,127,127,255),
    b2_kinematicBody : (50,127,127,255),
}

class DebugRenderer():
    def __init__(self):
        self.world = CoreApp.world

    def draw(self):
        for body in self.world.bodies:
            
            # Draw every body in the world
            for fixture in body.fixtures:
                shape=fixture.shape
                
                # Polygon
                if (shape.type == b2Shape.e_polygon):
                    vertices=[(body.transform*v)*CoreApp.PPM for v in shape.vertices]
                    
                    # Flipping vertices y axis to match pygame standard
                    vertices=[(v[0], CoreApp.SCREEN_HEIGHT-v[1]) for v in vertices]
        
                    # Draw Poly to the screen
                    pygame.draw.lines(CoreApp.screen, bodyColors[body.type], True, vertices)
                    
                # Circle
                else:
                    drawPointX = int(body.transform.position[0] * CoreApp.PPM)
                    drawPointY = int(CoreApp.SCREEN_HEIGHT - body.transform.position[1] * CoreApp.PPM)
                    
                    pygame.draw.circle(CoreApp.screen, bodyColors[body.type], (drawPointX, drawPointY), int(shape.radius * CoreApp.PPM), 1)
                    