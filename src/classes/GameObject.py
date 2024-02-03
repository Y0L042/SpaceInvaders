import pygame
vec2 = pygame.math.Vector2

class GameObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pygame.png")
        self.rect = self.image.get_rect()
    
    def update(self, delta):
        self.process(delta)
        
    def ready(self):
        pass
        
    def process(self, delta):
        pass

    def draw(self, win, delta):
        pass