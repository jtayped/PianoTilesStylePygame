import ctypes

def closestMultiple(n, x):
    if x > n:
        return x
    z = (int)(x / 2)
    n = n + z
    n = n - (n % x)
    return n

user32 = ctypes.windll.user32
HEIGHT = closestMultiple(user32.GetSystemMetrics(1)*0.85, 4)
WIDTH = HEIGHT/2

FPS = 60