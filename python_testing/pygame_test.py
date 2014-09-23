import pygame
import os
import time

screen = pygame.display.set_mode((512,512))

class Chdir:
    def __init__( self, newPath ):
        self.savedPath = os.getcwd()
        os.chdir(newPath)
    def __del__( self ):
        os.chdir( self.savedPath )

path = Chdir("C:\\Users\\Lennon\\Documents\\GitHub\\HDMI2614BBBK4325_HTML.exe.gz.json\\art\\shadow")

c = 10
car = pygame.image.load("yogso.png")
while(c>0):
    for x in range(0,100):
        screen.blit(car, (50,x))
        pygame.display.flip()
        time.sleep(0.01)
    c = c - 1

del path


