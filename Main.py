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

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(self.text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
                
            if self.active:
                self.color = COLOR_ACTIVE 
            else:
                self.color = COLOR_INACTIVE
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

import sys 
import pygame as pg

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('lightskyblue3') 
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(100, 100, 140, 32)
input_box2 = InputBox(100, 300, 140, 32)
input_boxes = [input_box1, input_box2]

while(run):
    screen.fill((255, 255, 255))

    for box in input_boxes:
        box.update() 
        box.draw(screen) 
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()
