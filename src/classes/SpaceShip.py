import os
import sys
# Add the src directory to sys.path to ensure imports work when running directly
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.append(project_root)

import pygame
from classes.GameObject import GameObject
import os

class SpaceShip(GameObject):
    def __init__(self):
        super().__init__()
        asset_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..\\assets\\graphics\\spaceship.png'))
        self.image = pygame.image.load(asset_path)
        self.rect = self.image.get_rect(midbottom = (0, 0))

def test():
    pass
 
if __name__ == "__main__":
    test()