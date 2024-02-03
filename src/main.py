#region Game Imports
from classes.SpaceShip import SpaceShip
#endregion Game Imports

#region Boilerplate

#region Boilerplate Imports
from sys import exit
from classes.Camera2D import Camera2D
import pygame

pygame.init()
#endregion Boilerplate Imports

#region Shorthands
vec2 = pygame.math.Vector2
#endregion Shorthands

#region Game Variables
game_objects = []
delta = 0
#endregion Game Variables

#region Display Config
pygame.display.set_caption("Space Invaders")

MAX_FRAMERATE = 60
CAMERA_WIDTH, CAMERA_HEIGHT = 1280, 720

canvas = pygame.Surface((CAMERA_WIDTH, CAMERA_HEIGHT))
window = pygame.display.set_mode((CAMERA_WIDTH, CAMERA_HEIGHT))
active_camera = Camera2D()
game_objects.append(active_camera)
#endregion Display Config

#region Color Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
TURQOISE = (64, 224, 208)
#endregion Color Constants

#region Coordinate System
STANDARD_PIXELS_PER_UNIT = 10
screen_x0, screen_y0 = 0, 0
screen_x1, screen_y1 = CAMERA_WIDTH - 1, CAMERA_HEIGHT - 1
#endregion Coordinate System

#region Global Variables
cam_pos = vec2(0, 0)
cam_speed = 1000
#endregion Global Variables

#region Loop
def main():
    run = True
    clock = pygame.time.Clock()
    
    ready()
    
    while run:
        delta = clock.tick(MAX_FRAMERATE) /1000
        window.fill(BLACK)
        
        input(delta)

        process(delta)
        process_game_objects(delta)
        
        draw(delta)
        draw_game_objects(delta)

        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
    pygame.quit()
    exit()
#endregion Loop

#region Utility Functions
def process_game_objects(delta):
    for Object in game_objects:
        Object.process(delta)

def draw_game_objects(delta):
    for sprite in active_camera.group:
        if not isinstance(sprite.image, pygame.Surface):
            print(f"Non-surface image found in sprite: {type(sprite)}")

    active_camera.group.draw(window)
    for sprite in active_camera.group:
        sprite_inv_offset_x = (active_camera.position.x - sprite.rect.x)
        sprite_inv_offset_y = (active_camera.position.y - sprite.rect.y)
        sprite.rect = sprite.rect.move( sprite_inv_offset_x, sprite_inv_offset_y)
        
def instantiate(i_new_game_object):
    active_camera.group.add(i_new_game_object)
    game_objects.append(i_new_game_object)
    i_new_game_object.ready()
    return i_new_game_object
#endregion Utility Functions

#endregion Boilerplate
    
#region Main Functions
def ready():
    ship = instantiate(SpaceShip())

def process(delta):
    pass

def input(delta):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
               pass
            elif event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_DOWN:
                pass
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

def draw(delta):
    pass
#endregion Main Functions

if __name__ == "__main__":
    main()