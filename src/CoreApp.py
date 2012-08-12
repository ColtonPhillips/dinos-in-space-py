import pygame
from Box2D import b2World

# --- constants ---
# Box2D deals with meters, but we want to display pixels, 
# so define a conversion factor:
PPM=40.0
FPS=60
TIME_STEP=1.0/FPS
SCREEN_WIDTH, SCREEN_HEIGHT=640 ,480

# Box2D Iterations
VELOCITY_ITERATION = 10
POSITION_ITERATION = 10

# --- pygame setup ---
pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),0, 32)
pygame.display.set_caption('Dinosaurs In Space!')

# --- pybox2d world setup ---
# Create the world
GRAVITY = -10
world=b2World(gravity=(0,GRAVITY),doSleep=False)

# --- pygame.mixer setup ---
pygame.mixer.init()
#TODO: Tweak for latency vs channels and verify this works - CP
pygame.mixer.set_num_channels(10)

# TODO: These function have, by far, the shittiest, most fucking confusing names - CP
def pixelsToWorld(pixels):
    worldPosition = (pixels[0] / PPM, (SCREEN_HEIGHT - pixels[1]) / PPM)
    return worldPosition

def pixelsToVelocity(pixels):
    worldPosition = (pixels[0] / PPM, pixels[1] / PPM)
    return worldPosition

def worldToPixels(world):
    pixelPosition = ((world[0] * PPM, SCREEN_HEIGHT - (world[1] * PPM)))
    return pixelPosition