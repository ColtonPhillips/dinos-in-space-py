# ARE YOU FUCKING READY!? ARE YOU FUCKING READY?! BECAUSE YOU SHOULD BE...
# THIS...
# IS... 
# DINOSAURS IN SPACE!!!

# THE BIG TODO!!!
# TODO: We need a class responsible for rendering the objects basically
#         This could be AnimationEngine or something similar
import CoreApp
import TestScene
import pygame
from pygame.locals import *

def gameLoop():
    # TODO: This should be more generic and easier to switch "FirstScene" 
    #        perhaps a SceneManager. for now, we'll use TestScene - CP
    testScene=TestScene.TestScene()
    
    # Game loop
    currentTime = pygame.time.get_ticks()
    IS_PLAYING = True
    while IS_PLAYING:
        previousTime = currentTime
        currentTime = pygame.time.get_ticks()
        deltaTime = currentTime - previousTime
        
        # Reset the screen
        CoreApp.screen.fill((0,0,0,0))
        
        # Step the world - times by 0.001 to convert to seconds
        CoreApp.world.Step((deltaTime) * 0.001, CoreApp.VELOCITY_ITERATION, CoreApp.POSITION_ITERATION)

        testScene.update(deltaTime)
        testScene.draw()
        
        # Swap to other screen buffer
        pygame.display.flip()  

        # One second / Target FPS is ideal frame time lapse
        timeLapse = pygame.time.get_ticks() - currentTime   
        if (timeLapse < 1000 / CoreApp.FPS):
            pygame.time.wait(1000 / CoreApp.FPS - timeLapse)
            
        # Must empty event queue or game stalls
        for event in pygame.event.get():
            if event.type == QUIT:
                IS_PLAYING = False
        
if __name__ == "__main__":
    gameLoop()