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

        self.tileList = []
        self.tileSize = [int(WIDTH/4), HEIGHT/7]
        self.tileBuffer = HEIGHT/self.tileSize[1]*2.5

        self.tileSpeed = 7
        self.tileColor = 'grey12'
        self.inLineCounter = 0
        self.maxInLine = 3

        pos = [2*self.tileSize[0], -self.tileSize[1]]
        self.tileList.append(Tile(self.screen, pos, self.tileSize, self.tileColor))
    
    def generateTile(self):
        pos = []
        if self.tileList[-1].rect.x == WIDTH-self.tileSize[0]:
            pos.append(self.tileList[-1].rect.x + random.randint(-1, 0)*self.tileSize[0])
    
        elif self.tileList[-1].rect.x == 0:
            pos.append(self.tileList[-1].rect.x + random.randint(0, 1)*self.tileSize[0])

        else:
            pos.append(self.tileList[-1].rect.x + random.randint(-1, 1)*self.tileSize[0])

        if pos[0] == self.tileList[-1].rect.x:
            self.inLineCounter += 1
            if self.inLineCounter == self.maxInLine:
                self.generateTile()
                self.inLineCounter = 0

        else:
            self.inLineCounter = 0

        pos.append(self.tileList[-1].rect.y - self.tileSize[1])
        self.tileList.append(Tile(self.screen, pos, self.tileSize, self.tileColor))

    def tileUpdate(self):
        for tile in self.tileList:
            tile.update(self.tileSpeed)

            if tile.offScreen():
                self.tileList.remove(tile)
            
            if tile.dead():
                self.__init__()

    def tileHandler(self):
        self.tileUpdate()

        if len(self.tileList) < self.tileBuffer:
            self.generateTile()

    def events(self):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONUP:
                self.mouseClick = pygame.mouse.get_pos()  

                for tile in self.tileList:
                    if tile.clicked(self.mouseClick):
                        tile.color = 'green'

                        tileNextIndex = 1
                        while self.tileList[self.tileList.index(tile)+tileNextIndex].rect.x == tile.rect.x:
                            self.tileList[self.tileList.index(tile)+tileNextIndex].color = 'green'
                            tileNextIndex += 1
                            

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