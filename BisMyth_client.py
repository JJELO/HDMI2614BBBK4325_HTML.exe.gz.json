from pygame import *
import os
import time
import lib_client.classes as clas
import lib_client.client_resources as res

yogso = clas.Character(res.char_spr["yogso"])

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

#spr_yogso = image.load(".\\art\\shadow\\yogso.png")
#spr_yogso.set_colorkey((0xFF,0xFF,0xFF)) #this makes white load as blank

c = 3

#yogso = Rect(0,0,64,64) #yogso is a rectangle

yogso.box.top = 100

display.update()

while(c>0): # move yogso back and forth 3 times
    for x in range(0,100): #move yogso right
        screen.blit(bg, (yogso.box.left,yogso.box.top), area=yogso.box)
        #redraws background over yogso
        yogso.box.left = 100 + x
        #moves yogso
        screen.blit(yogso.spr["still"], (yogso.box.left,yogso.box.top))
        #redraws yogso
        display.flip()
        #ask lead developer about this
        time.sleep(0.01)
        #wait for 1/20th of a second
    for x in range(0,100): #move yogso left (rest is as above)
        screen.blit(bg, (yogso.box.left,yogso.box.top), area=yogso.box)
        yogso.box.left = 200 - x
        screen.blit(yogso.spr["still"], (yogso.box.left,yogso.box.top))
        display.flip()
        time.sleep(0.01)
    c = c - 1

display.quit()
