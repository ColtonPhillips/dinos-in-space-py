# The Scene for the core #DinosaursInSpace game. 
# TODO: Is this just for 1 player? AKA, are modes part of this scene, or new scene?


import PhysicsDebug

# TODO: Does this need to have a Scene base class?
class DinoScene():
    def __init__(self):
        self.debugRenderer = PhysicsDebug.DebugRenderer()
        
    def update(self, dt):
        pass
        
    def draw(self):
        self.debugRenderer.draw()
        pass