# ARE YOU FUCKING READY!? ARE YOU FUCKING READY?! BECAUSE YOU SHOULD BE...
# THIS...
# IS... 
# DINOSAURS IN SPACE!!!

import CoreApp 
import DinoScene
import pygame
import InputWatcher
from pygame.locals import *

FIRST_SCENE = DinoScene

# HACK: First timestamp is a zero. is this a big deo la mon? - CP
def gameLoop():

    dinoScene=FIRST_SCENE.DinoScene()
    
    # Game loop
    currentTime = pygame.time.get_ticks()
    IS_PLAYING = True
    while IS_PLAYING:
        previousTime = currentTime
        currentTime = pygame.time.get_ticks()
        deltaTime = currentTime - previousTime
          
        # Reset the screen
        CoreApp.screen.fill((0,0,0,0))
        
        # HACK: If you drag screen in Windows, it locks main thread
        # This averts the bug, but may introduce new bugs. Look into this - CP
        if (deltaTime > 100):
            deltaTime = 0
        
        # Step the world - times by 0.001 to convert to seconds
        CoreApp.world.Step((deltaTime) * 0.001, CoreApp.VELOCITY_ITERATION, CoreApp.POSITION_ITERATION)

        dinoScene.update(deltaTime)
        dinoScene.draw()
        
        # Swap to other screen buffer
        pygame.display.flip()  
 
        # One second / Target FPS is ideal frame time lapse
        timeLapse = pygame.time.get_ticks() - currentTime   
        if (timeLapse < 1000 / CoreApp.FPS):
            pygame.time.wait(1000 / CoreApp.FPS - timeLapse) 
            
        # Must empty event or game stalls
        for event in pygame.event.get():
            if event.type == QUIT:
                IS_PLAYING = False
                
        # TEMP: Leave scene if press ESC - CP
        IS_PLAYING = not InputWatcher.isDown(pygame.K_ESCAPE)
        
if __name__ == "__main__":
    gameLoop()