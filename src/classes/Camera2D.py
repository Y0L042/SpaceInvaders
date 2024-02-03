from classes.GameObject import GameObject

from abc import ABC, abstractmethod

import pygame
vec2 = pygame.math.Vector2

class Camera2DGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()


class Camera2D(GameObject):
    def __init__(self):
        super().__init__()
        
        self.group = Camera2DGroup()
        
        self.width = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()
        
        self.half_width = self.width / 2
        self.half_height = self.height / 2
        
        self.position = vec2(self.half_width, self.half_height)
        self.prev_position = self.position
        
        # self.set_position(vec2(0,0))

    
    def set_position(self, new_position):
        self.prev_position = self.position
        self.position = new_position
        print(f"Previous Position: {self.prev_position}")
        print(f"Position: {self.position}")
    
    def move(self, delta):
        self.position += delta
           
    def process(self, delta):
        pass
        
        
        
    def update_sprite_positions(self):
        self.delta_pos = (self.position - self.prev_position) * -1
        
        for sprite in self.group:
            sprite.rect.move(self.delta_pos.x, self.delta_pos.y)
            
