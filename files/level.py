import pygame, random
from files.settings import *
from files.tile import Tile

class Level:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(str(round(self.clock.get_fps(), 1)))
    
        self.font = pygame.font.SysFont('AGENCYB.TTF', 75)
        self.tinyFont = pygame.font.SysFont('AGENCYB.TTF', 25)

        self.running = True

        self.singleTileSize = [
            WIDTH/4,
            HEIGHT/8
        ]

        self.maxNTiles = int(HEIGHT/self.singleTileSize[1]*1.75)
        self.tileList = []
        self.tileSpeed = 3

        self.createTile()

    def createTile(self):
        pos = []
        size = self.singleTileSize[:]
    
        if len(self.tileList) == 0:
            pos = [
                random.randint(0, 3)*self.singleTileSize[0],
                0
            ]
        
        else:
            lastTile = self.tileList[-1]

            if random.randint(1, 6) == 5:
                size[1] *= 2

            if lastTile.rect.x == 0:
                pos.append(self.tileList[-1].rect.x + self.singleTileSize[0])
            
            elif lastTile.rect.x == WIDTH-lastTile.rect.width:
                pos.append(self.tileList[-1].rect.x - self.singleTileSize[0])

            else:
                pos.append(self.tileList[-1].rect.x + random.choice([-1, 1])*self.singleTileSize[0])
            
            pos.append(self.tileList[-1].rect.y - size[1])
            
        self.tileList.append(Tile(self.screen, pos, size, 'black', self.tileSpeed))
    
    def getTileClicked(self):
        self.mousePressed = pygame.mouse.get_pressed()[0]

        if self.mousePressed:
            self.mousePos = pygame.mouse.get_pos()

            if self.tileList[0].clicked(self.mousePos):
                self.tileList.remove(self.tileList[0])
        
        else:
            self.mousePos = None

    def tileUpdate(self):
        for tile in self.tileList:
            tile.update()

            if tile.offScreen():
                self.tileList.remove(tile)

    def tileHandler(self):
        self.getTileClicked()
        self.tileUpdate()

        if len(self.tileList) < self.maxNTiles:
            self.createTile()

    def events(self):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.clock.tick(FPS)
        self.events()
        self.screen.fill('white')
        self.fps = self.clock.get_fps()
        pygame.display.set_caption(str(round(self.fps)))
        
        ########################################

        self.tileHandler()

        ########################################

        pygame.display.flip()    

    def run(self):
        while self.running:
            self.update()