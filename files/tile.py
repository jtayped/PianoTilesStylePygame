import pygame
from files.settings import *

class Tile:
    def __init__(self, surface, pos, size, color, speed) -> None:
        self.screen = surface
        self.color = color
        self.speed = speed

        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
    
    def clicked(self, mouseClick):
        return self.rect.collidepoint(mouseClick)

    def offScreen(self):
        return self.rect.top > HEIGHT*1.5
    
    def movement(self):
        self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def update(self):
        self.movement()
        self.draw()