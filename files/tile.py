import pygame
from files.settings import *

class Tile:
    def __init__(self, surface, pos, size, color, speed) -> None:
        self.screen = surface
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

        self.color = color
        self.speed = speed
    
    def offScreen(self):
        return self.rect.y > HEIGHT*1.5

    def movement(self):
        self.rect.y += self.speed
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def update(self):
        self.movement()
        self.draw()