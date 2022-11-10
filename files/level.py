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
        self.tileSize = [WIDTH/self.nColumns, HEIGHT/6]
        self.nTilesOnScreen = HEIGHT/self.tileSize[1]*1.75
        self.tileSpeed = 3

        pos = [
            random.choice([0, 1, 2, 3])*self.tileSize[0],
            0
        ]

        self.tileList.append(Tile(self.screen, pos, self.tileSize, 'black', self.tileSpeed))

        self.running = True
    
    def tileUpdate(self):
        mouseClickPos = pygame.mouse.get_pressed()[0]
        if mouseClickPos:
            mouseClickPos = pygame.mouse.get_pos()
        else:
            mouseClickPos = None

        for tile in self.tileList:
            tile.update()
            if tile.offScreen():
                self.tileList.remove(tile)
            
            if mouseClickPos != None:
                if tile.clicked(mouseClickPos):
                    self.tileList.remove(tile)



    def createTile(self):
        pos = []
        size = self.tileSize[:]

        lastTile = self.tileList[-1]
        if random.randint(0, 6) == 5:
            size[1] *= 2

        # X
        if lastTile.rect.x == 0:
            pos.append(lastTile.rect.x + size[0])
        elif lastTile.rect.x == WIDTH-size[0]:
            pos.append(lastTile.rect.x - size[0])
        else:
            pos.append(lastTile.rect.x + random.choice([-1, 1])*size[0])
        
        # Y
        pos.append(lastTile.rect.top - size[1])
        
        self.tileList.append(Tile(self.screen, pos, size, 'black', self.tileSpeed))

    def tileHandler(self):
        self.tileUpdate()

        if len(self.tileList) < self.nTilesOnScreen:
            self.createTile()

    def update(self):
        self.clock.tick(FPS)
        self.events()
        self.fps = self.clock.get_fps()
        pygame.display.set_caption(f'{self.fps}')

        self.screen.fill('white')

        self.tileHandler()

        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        while self.running:
            self.update()

