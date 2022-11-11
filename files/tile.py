from files.settings import *
import pygame

class Tile:
    def __init__(self, surface, pos, size, color) -> None:
        self.screen = surface
        self.color = color
        self.speed = speed

        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

        self.color = color
        self.ballRadius = WIDTH/35

    def dead(self):
        return self.rect.bottom > HEIGHT and self.color == 'grey12'

    def clicked(self, mouseClick):
        return self.rect.collidepoint(mouseClick)

    def offScreen(self):
        return self.rect.top > HEIGHT*1.5

    def movement(self):
        self.rect.y += self.speed
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

        if self.color == 'grey12':
            centerBall = (self.rect.x+self.rect.width/2, self.rect.y+self.rect.height*0.675)
            pygame.draw.line(self.screen, 'grey', (self.rect.x+self.rect.width/2, self.rect.y+self.rect.height*0.2), (self.rect.x+self.rect.width/2, self.rect.y+self.rect.height*0.8))
    
    def update(self, speed):
        self.speed = speed
        self.movement()
        self.draw()