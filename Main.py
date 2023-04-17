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
import pygame as pg

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
obj = Rectangle(350,190,100,100,120,20,220)

while(run):
    screen.fill((255, 255, 255))
        
    obj.draw(screen)
    
    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_a:
            obj.x -= 10
        
        if event.type == pg.KEYDOWN and event.key == pg.K_d:
            obj.x += 10
        
        if event.type == pg.KEYDOWN and event.key == pg.K_w:
            obj.y -= 10

        if event.type == pg.KEYDOWN and event.key == pg.K_s:
            obj.y += 10
            
        if event.type == pg.QUIT:
            pg.quit()
            run = False
