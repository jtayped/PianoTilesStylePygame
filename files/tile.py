import pygame, random
from files.settings import *

class Tile:
    def __init__(self, surface, pos, size, color, speed, font, multiplier) -> None:
        self.screen = surface
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

        self.color = color
        self.speed = speed

        self.pressed = False

        self.scoreValue = size[1]/tileSize[1]
        if multiplier > 1:
            self.scoreValue *= multiplier
            self.color = self.getRandomColor()

        self.long = False
        if size[1] > tileSize[1]:
            self.long = True
        
        self.font = font
        self.score = self.font.render(f'+{int(self.scoreValue)}', True, 'white')
        self.scoreWidth, self.scoreHeight = self.score.get_width(), self.score.get_height()

    def getRandomColor(self):
        return [random.randint(150, 200), random.randint(150, 200), random.randint(150, 200)]

    def clicked(self, mouseClick):
        return self.rect.collidepoint(mouseClick)

    def offScreen(self):
        return self.rect.bottom >= HEIGHT

    def movement(self):
        self.rect.y += self.speed
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.score, (self.rect.centerx-self.scoreWidth/2, self.rect.centery-self.scoreHeight/2))
    
    def update(self):
        self.movement()
        self.draw()