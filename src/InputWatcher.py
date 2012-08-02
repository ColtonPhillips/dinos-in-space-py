# TODO: Maybe unit test these fuckers below - CP

import pygame

key_state        = pygame.key.get_pressed()
last_key_state   = pygame.key.get_pressed()

def update():
    global key_state
    global last_key_state # Global because modifying
    last_key_state = key_state
    key_state = pygame.key.get_pressed()
    
        
def isDown(key):
    if key_state[key]:
        return True
    else: 
        return False

def wasPressed(key):
    if not last_key_state[key] and key_state[key]:
        return True
    else:
        return False
    
def wasReleased(key):
    if last_key_state[key] and not key_state[key]:
        return True
    else:
        return False