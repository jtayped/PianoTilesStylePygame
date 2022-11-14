from files.tile import Tile
from files.settings import *
import pygame, random, time

class Level:
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init() 
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('AGENCYB.TTF', 75)

        pygame.display.set_caption(f"{round(self.clock.get_fps())} fps")

        self.tileList = []
        self.nTilesOnScreen = HEIGHT/tileSize[1]*1.75
        self.tileSpeed = 2

        pos = [
            random.choice([0, 1, 2, 3])*tileSize[0],
            0
        ]

        self.tileList.append(Tile(self.screen, pos, tileSize, 'black', self.tileSpeed, self.font, 1))

        self.running = True
        self.clickLimitSpacer = HEIGHT*0.6

        self.mouseClick = None

        self.score = 0
        self.targetScore = 0
        self.scoreIncrementDelay = FPS/10
    
    def reset(self):
        time.sleep(0.5)
        self.__init__()

    def tileUpdate(self):
        if self.mouseClick != None and self.mouseClick[1] > HEIGHT-self.clickLimitSpacer:
            firstTile = self.tileList[0]
        
            if firstTile.clicked(self.mouseClick):
                self.tileList.remove(firstTile)
                self.mouseClick = None
                self.targetScore += firstTile.scoreValue
            
            else:
                self.reset()

        for tile in self.tileList:
            tile.update()
            if tile.offScreen():
                self.reset()

    def getRandomColor(self):
        return [random.randint(150, 200), random.randint(150, 200), random.randint(150, 200)]

    def createTile(self):
        pos = []
        size = tileSize[:]
        color = 'black'
        multiplier = 1

        lastTile = self.tileList[-1]
        if random.randint(0, 6) == 5:
            size[1] *= 2

        if random.randint(0, 20) == 15:
            multiplier *= 2
        if random.randint(0, 20) == 15:
            multiplier *= 2

        # X
        if not kovaxMode and self.score < 250:
            if lastTile.rect.x == 0:
                pos.append(lastTile.rect.x + size[0])
            elif lastTile.rect.x == WIDTH-size[0]:
                pos.append(lastTile.rect.x - size[0])
            else:
                pos.append(lastTile.rect.x + random.choice([-1, 1])*size[0])
        else:
            pos.append(random.choice(range(nColumns))*size[0])
            color = self.getRandomColor()
            multiplier *= 2
        
        # Y
        pos.append(lastTile.rect.top - size[1])
        
        self.tileList.append(Tile(self.screen, pos, size, color, self.tileSpeed, self.font, multiplier))

    def tileHandler(self):
        self.tileUpdate()

        if len(self.tileList) < self.nTilesOnScreen:
            self.createTile()

    def scoreBoard(self):
        if self.targetScore > self.score and self.scoreIncrementDelay <= 0:
            self.score += 1
            self.scoreIncrementDelay = FPS/10
        self.scoreIncrementDelay -= 1

        score = self.font.render(f'{int(self.score)}', True, 'grey')
        scoreWidth, scoreHeight = score.get_width(), score.get_height()

        self.screen.blit(score, (WIDTH/2-scoreWidth/2, 5))

    def tileInArea(self, x, y):
        for tile in self.tileList:
            if tile.rect.x == x and tile.rect.bottom > y:
                return True
        return False
    
    def removeFirstTileClickable(self, tileN):
        firstTile = self.tileList[0]
        if firstTile.rect.bottom > HEIGHT-self.clickLimitSpacer and firstTile.rect.x == tileN*tileSize[0]:
            self.targetScore += firstTile.scoreValue
            self.tileList.remove(firstTile)
            return True
        return False
            
    def controls(self):
        key = pygame.key.get_pressed()
        if not kovaxMode:    
            if key[pygame.K_a]:
                self.removeFirstTileClickable(0)
            elif key[pygame.K_s]:
                self.removeFirstTileClickable(1)
            elif key[pygame.K_d]:
                self.removeFirstTileClickable(2)
            elif key[pygame.K_f]:
                self.removeFirstTileClickable(3)

    def update(self):
        self.clock.tick(FPS)
        self.events()
        self.fps = self.clock.get_fps()
        pygame.display.set_caption(f'{round(self.fps)}')
        self.clickLimitSpacer *= 0.9999

        self.screen.fill('white')

        self.tileHandler()
        self.scoreBoard()
        #self.controls()

        pygame.draw.aaline(self.screen, 'red', (0, HEIGHT-self.clickLimitSpacer), (WIDTH, HEIGHT-self.clickLimitSpacer))
        pygame.draw.aaline(self.screen, 'red', (0, HEIGHT-1), (WIDTH, HEIGHT-1))

        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouseClick = pygame.mouse.get_pos()
            
            if event.type == pygame.KEYDOWN:
                tile = False
                if event.key == pygame.K_f:
                    tile = self.removeFirstTileClickable(0)
                elif event.key == pygame.K_g:
                    tile = self.removeFirstTileClickable(1)
                elif event.key == pygame.K_h:
                    tile = self.removeFirstTileClickable(2)
                elif event.key == pygame.K_j:
                    tile = self.removeFirstTileClickable(3)
                else:
                    tile = True
                
                if not tile:
                    self.reset()

    def run(self):
        while self.running:
            self.update()

