import ctypes

user32 = ctypes.windll.user32
HEIGHT = 750
WIDTH = 400

FPS = 144

nColumns = 4

kovaxMode = False
if kovaxMode:
    nColumns *= 2

tileSize = [WIDTH/nColumns, HEIGHT/6]