from files.tile import Tile
from files.settings import *
import pygame, random

class Level:
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init() 
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption(f"{self.clock.get_fps()} fps")
        self.nColumns = 4

        self.tileList = []
        self.tileSize = [WIDTH/self.nColumns, HEIGHT/15]
        self.createTile(True)

    def getNewTilePos(self):
        pos = []
        size = self.tileSize[:]

        if len(self.tileList) == 0:
            pos.append(0)

        else:
            pos.append(random.choice([0, 1, 2, 3]*size[0]))

        return pos

    def createTile(self, start=False):
        if start:
            pos = self.getNewTilePos()
