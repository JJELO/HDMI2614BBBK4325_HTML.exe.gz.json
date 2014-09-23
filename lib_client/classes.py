import pygame

class Race:
    chars = {}

class Character:
    def __init__(self, sprites):
        for x in sprites:
            pygame.image.load(sprites[x])
    spr = {}
