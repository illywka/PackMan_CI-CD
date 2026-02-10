import pygame
from abc import ABC, abstractmethod
from src.utils.constants import TILE_SIZE, GHOSTS_SPEED
import random

class Ghost(pygame.sprite.Sprite, ABC):
    def __init__(self):
        super().__init__()

        self.mode = "Scattering"
        self.speed = 2
        self.pos = pygame.Rect(9*TILE_SIZE, 12*TILE_SIZE, TILE_SIZE, TILE_SIZE)
        
        
    
    @property
    @abstractmethod
    def image(self):
        pass

    @abstractmethod
    def move(self):
        pass


#Pinky, Inky, Sue, Clyde
class Pinky(Ghost):
    start_sprite = (0, 0)
    end_sprite = (16, 16)
    def __init__(self):
        super().__init__()
    
    @property
    def image(self):
        sprite = pygame.image.load(f'src/assets/ghosts/pink_ghost/pink_ghost.png')
        curr_sprite = sprite.subsurface((self.start_sprite, self.end_sprite))
        return curr_sprite

    def move(self):
        x = random.randint(-GHOSTS_SPEED, GHOSTS_SPEED)
        y = random.randint(-GHOSTS_SPEED, GHOSTS_SPEED)

        self.pos = pygame.Rect.move(self.pos, x, y)


    def update(self):
        self.move()

class Inky(Ghost):
    start_sprite = (0, 0)
    end_sprite = (16, 16)
    def __init__(self):
        super().__init__()
    
    @property
    def image(self):
        sprite = pygame.image.load(f'src/assets/ghosts/cyan_ghost/cyan_ghost.png')
        curr_sprite = sprite.subsurface((self.start_sprite, self.end_sprite))
        return curr_sprite

    def move(self):
        x = random.randint(-GHOSTS_SPEED, GHOSTS_SPEED)
        y = random.randint(-GHOSTS_SPEED, GHOSTS_SPEED)

        self.pos = pygame.Rect.move(self.pos, x, y)


    def update(self):
        self.move()

class Sue(Ghost):
    start_sprite = (0, 0)
    end_sprite = (16, 16)
    def __init__(self):
        super().__init__()
    
    @property
    def image(self):
        sprite = pygame.image.load(f'src/assets/ghosts/purple_ghost/purple_ghost.png')
        curr_sprite = sprite.subsurface((self.start_sprite, self.end_sprite))
        return curr_sprite

    def move(self):
        x = random.randint(-GHOSTS_SPEED, GHOSTS_SPEED)
        y = random.randint(-GHOSTS_SPEED, GHOSTS_SPEED)

        self.pos = pygame.Rect.move(self.pos, x, y)


    def update(self):
        self.move()

class Clyde(Ghost):
    start_sprite = (0, 0)
    end_sprite = (16, 16)
    def __init__(self):
        super().__init__()
    
    @property
    def image(self):
        sprite = pygame.image.load(f'src/assets/ghosts/brown_ghost/brown_ghost.png')
        curr_sprite = sprite.subsurface((self.start_sprite, self.end_sprite))
        return curr_sprite

    def move(self):
        x = random.randint(-GHOSTS_SPEED, GHOSTS_SPEED)
        y = random.randint(-GHOSTS_SPEED, GHOSTS_SPEED)

        self.pos = pygame.Rect.move(self.pos, x, y)


    def update(self):
        self.move()