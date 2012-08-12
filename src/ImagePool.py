#TODO: This is just some code i copied. you actually have to do the thing. So yeah. do it. - CP

# TODO: Mystically, with great precision and beauty, abstract the loading 
# and use of images.

import pygame

# TODO: This is some Bey function. Thought it was good shit. It will live here now.
def get_image( image_name, color=None ):

    root_dir = "res/"
    image = pygame.image.load( root_dir + image_name )

    if color:
        image.fill( color, special_flags=pygame.BLEND_RGB_MULT )

    return image