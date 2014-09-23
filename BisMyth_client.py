from pygame import *
import os
import time
import lib_client.classes as clas
import lib_client.client_resources as res

ch_yogso = clas.Character(res.chars["yogso"])

bg = Surface((512,512)) #this is the background
screen = display.set_mode((512,512), DOUBLEBUF) #this is the screen

spr_back = image.load(".\\art\\other\\test_back.png")
#that loads the background sprite into memory
for x in range(0,8):
    for y in range (0,4):
        bg.blit(spr_back,(x*64,y*48))
        #this fills the background with tilings of the sprite

screen.blit(bg, (0,0))
#this draws the background onto the screen

spr_yogso = image.load(".\\art\\shadow\\yogso.png")
spr_yogso.set_colorkey((0xFF,0xFF,0xFF)) #this makes white load as blank

c = 3

yogso = Rect(0,0,64,64) #yogso is a rectangle

display.update()

while(c>0): # move yogso back and forth 3 times
    for x in range(0,100): #move yogso right
        screen.blit(bg, (yogso.left,yogso.top), area=yogso)
        #redraws background over yogso
        yogso.left = 100 + x
        yogso.top = 100
        #moves yogso
        screen.blit(spr_yogso, (yogso.left,yogso.top))
        #redraws yogso
        display.flip()
        #ask lead developer about this
        time.sleep(0.01)
        #wait for 1/20th of a second
    for x in range(0,100): #move yogso left (rest is as above)
        screen.blit(bg, (yogso.left,yogso.top), area=yogso)
        yogso.left = 200 - x
        yogso.top = 100
        screen.blit(spr_yogso, (yogso.left,yogso.top))
        display.flip()
        time.sleep(0.01)
    c = c - 1



