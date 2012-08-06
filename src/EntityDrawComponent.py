import CoreApp
import pygame
import math

def draw(entityList):
   for entity in entityList:
        draw_image = pygame.transform.rotate(entity.image, math.degrees(entity.bodyList[0].angle))
        pos = CoreApp.worldToPixels(entity.bodyList[0].worldCenter)
        CoreApp.screen.blit(draw_image, (pos[0] - draw_image.get_width()/2 , pos[1] - draw_image.get_height()/2) )