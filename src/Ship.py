import pygame
import CoreApp
import InputWatcher

# TODO: This tuple bullshit, is flaky and gross - CP
# TODO: Ship should have aesthetic up and down movement.

# Magic Numbers
SHIP_START_X, SHIP_START_Y = 100, 20
DROP_OFFSET_X, DROP_OFFSET_Y = 50, 100
PLAYER_FORCE = 0.08
FRICTION_FORCE = 0.9
MAX_SPEED = 0.56
SHIP_SCREEN_RIGHT = CoreApp.SCREEN_WIDTH - 100
IMPULSE_FACTOR = 550

class Ship():
    def __init__(self):
        
        # TODO: Image loading needs to be abstracted. - CP
        self.image = pygame.image.load("./../res/ship/ship.png")
        
        # In screen units, not world, for the top left of the dinosaur
        self.position = [SHIP_START_X, SHIP_START_Y]
        self.velocity = [0,0]

    def update(self, dt):
        direction = 0
        if InputWatcher.isDown(pygame.K_LEFT) or InputWatcher.isDown(pygame.K_a):
            direction -= 1
        if InputWatcher.isDown(pygame.K_RIGHT) or InputWatcher.isDown(pygame.K_d):
            direction += 1
            
        # Apply player or friction force
        if direction == -1:
            self.velocity[0] -= PLAYER_FORCE
        elif direction == 1:
            self.velocity[0] += PLAYER_FORCE
        else:
            self.velocity[0] *= FRICTION_FORCE
            
        # Clamp velocity
        if (self.velocity[0] > MAX_SPEED):
            self.velocity[0] = MAX_SPEED
        if (self.velocity[0] < -MAX_SPEED):
            self.velocity[0] = -MAX_SPEED
        
        # Set position from velocity
        self.position = [self.position[0] + self.velocity[0] * dt, self.position[1] + self.velocity[1] * dt]
        
        # Clamp position in scene
        if (self.position[0] > SHIP_SCREEN_RIGHT):
            self.position[0] = SHIP_SCREEN_RIGHT
            self.velocity = [0,0]                  
        if (self.position[0] < 0):
            self.position[0] = 0
            self.velocity = [0,0]
        
    def draw(self):
        CoreApp.screen.blit(self.image, self.position)
        
    def getWorldDropPosition(self):
        return CoreApp.pixelsToWorld((self.position[0] + DROP_OFFSET_X, self.position[1] + DROP_OFFSET_Y))
    
    def getWorldVelocity(self):
        return CoreApp.pixelsToVelocity(self.velocity)