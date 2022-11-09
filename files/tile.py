from files.settings import *
import pygame

class Tile:
    def __init__(self, surface, pos, size, color, speed, long) -> None:
        self.screen = surface
        self.color = color
        self.speed = speed
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.long = long

        self.circleCenter = [self.rect.x + self.rect.width/2, self.rect.y + self.rect.height*0.8]
        self.circleRadius = WIDTH/45

        self.clicked = False
        self.circleDisplace = 0

        self.top = self.rect.y + self.rect.height*0.2
        self.dead = False

    def offScreen(self):
        return self.rect.top > HEIGHT*1.5

    def checkClick(self, point):
        if self.rect.collidepoint(point):
            self.clicked = True

    def checkDead(self):
        if self.circleCenter[1] < self.top and self.long:
            self.dead = True
            self.color = 'green'

    def movement(self):
        self.rect.y += self.speed
        if not self.clicked and self.long and not self.dead:
            self.circleCenter = [self.rect.x + self.rect.width/2, self.rect.y + self.rect.height*0.8 + self.circleDisplace]
        else:
            self.circleDisplace -= self.speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

        if self.long:
            pygame.draw.circle(self.screen, 'grey', self.circleCenter, self.circleRadius, 1)
            pygame.draw.line(self.screen, 'grey', 
            (self.circleCenter[0], self.top),
            [self.rect.x + self.rect.width/2, self.rect.y + self.rect.height*0.8],
            1
            )
    
    def update(self):
        self.top += self.speed
        self.movement()
        self.checkDead()
        self.draw()