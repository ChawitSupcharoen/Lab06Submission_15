class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,r=0,g=0,b=0):
        self.x = x
        self.y = y 
        self.w = w 
        self.h = h 
        self.r = r 
        self.g = g 
        self.b = b 
    def draw(self,screen):
        pg.draw.rect(screen,(self.r,self.g,self.b),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0, r=0, g=0, b=0):
        Rectangle.__init__(self,x,y,w,h,r,g,b)

    def isMouseOn(self):
        mouseX,mouseY = pg.mouse.get_pos()
        if(mouseX >= self.x and mouseX <= self.x+self.w and mouseY >= self.y and mouseY <= self.y+self.h):
            return True
        else:
            return False
    
    def isMouseClick(self):
        lClick, mClick, rClick = pg.mouse.get_pressed()
        if(self.isMouseOn() and lClick):
            return True
        else:
            return False

import sys 
import time
import pygame as pg

longClick = False
notClickYet = True
lastClick = 0

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100,120,20,220)

while(run):
    screen.fill((255, 255, 255))
    
    if btn.isMouseClick():
        if notClickYet:
            lastClick = pg.time.get_ticks()
            notClickYet = False

        else:
            if(pg.time.get_ticks() - lastClick >= 500):
                longClick = True

    else:
        longClick = False
        notClickYet = True
        longClick = False

    if longClick:
        btn.r = 120
        btn.g = 20
        btn.b = 220
    
    elif btn.isMouseOn():
        btn.r = 150
        btn.g = 150
        btn.b = 150
        
    else:
        btn.r = 255
        btn.g = 0
        btn.b = 0
        
    btn.draw(screen)
    
    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
