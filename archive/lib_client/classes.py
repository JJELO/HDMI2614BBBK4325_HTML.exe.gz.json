import pygame

class Race:
    chars = {}

class Character:
    spr = {}
    box = pygame.Rect(0,0,64,64)
    def __init__(self, sprites, colorkey = (255,255,255)):
        
        for x in sprites:
            self.spr[x] = pygame.image.load(sprites[x])
            self.spr[x].set_colorkey(colorkey)
            
