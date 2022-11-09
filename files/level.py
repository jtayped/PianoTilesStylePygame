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

        self.tilesInX = 4
        self.tileList = []
        self.tileSize = [int(WIDTH/self.tilesInX), HEIGHT/7]
        self.tileBuffer = HEIGHT/self.tileSize[1]*2.5

        self.tileSpeed = 2
        self.tileColor = 'grey12'

        pos = [random.randint(0, self.tilesInX-1)*self.tileSize[0], -self.tileSize[1]]
        self.tileList.append(Tile(self.screen, pos, self.tileSize, self.tileColor, self.tileSpeed, False))

        self.mouseButtonDown = False
    
    def generateTile(self):
        pos = []
        size = self.tileSize[:]

        pos.append(random.choice([0, 1, 2, 3])*size[0])
        pos.append(self.tileList[-1].rect.y - self.tileList[-1].rect.height)

        long = False
        if random.randint(0, 5) == 4:
            size[1] *= 2
            long = True

        self.tileList.append(Tile(self.screen, pos, size, self.tileColor, self.tileSpeed, long))

    def tileUpdate(self):
        for tile in self.tileList:
            tile.update()

            if tile.offScreen():
                self.tileList.remove(tile)

            if self.mouseButtonDown and tile.checkClick(self.mouseClick):
                tile.clicked = True
            
            elif not self.mouseButtonDown:
                tile.clicked = False

    def tileHandler(self):
        self.tileUpdate()

        if len(self.tileList) < self.tileBuffer:
            self.generateTile()

    def getMouseHold(self):
        if self.mouseButtonDown:
            self.mouseClick = pygame.mouse.get_pos()

    def events(self):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN: 
                self.mouseButtonDown = True
            
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouseButtonDown = False

    def update(self):
        self.clock.tick(FPS)
        self.events()
        self.screen.fill('white')
        self.fps = self.clock.get_fps()
        pygame.display.set_caption(str(round(self.fps)))
        
        ########################################

        self.getMouseHold()
        self.tileHandler()

        ########################################

        pygame.display.flip()    

    def run(self):
        while self.running:
            self.update()