class Rectangle:
    def __init__(self, x=0, y=0, w=0, h=0, r=0, g=0, b=0, br=0):
        self.x = x
        self.y = y 
        self.w = w 
        self.h = h 
        self.r = r 
        self.g = g 
        self.b = b 
        self.br = br
    def draw(self,screen):
        pg.draw.rect(screen,(self.r,self.g,self.b),(self.x,self.y,self.w,self.h),self.br)

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0, r=0, g=0, b=0, br=0):
        self.x = x
        self.y = y 
        self.w = w 
        self.h = h

        self.hitbox = pg.Rect(x,y,w,h)
        self.r = r 
        self.g = g 
        self.b = b 
        self.br = br
        Rectangle.__init__(self,x,y,w,h,r,g,b,br)
        
    def isMouseOn(self):
        mX,mY = pg.mouse.get_pos()
        if (mX >= self.x and mX <= self.x + self.w and mY >= self.y and mY <= self.y + self.h):
            return True
        else:
            return False
    
    def isMouseClick(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.hitbox.collidepoint(event.pos):
                return True
            else:
                return False
        else:
            pass
    

class TextBox:
    def __init__(self, x, y, text=''):
        self.x = x
        self.y = y
        self.color = (0,0,0)
        self.text = text
        self.txt_surface = FONT.render(self.text, True, self.color)

    def draw(self, Screen):
        # Blit the text.
        self.txt_surface = FONT.render(self.text, True, self.color)
        Screen.blit(self.txt_surface, (self.x, self.y))

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(self.text, True, self.color)
        self.active = False
        self.useNum = False
        self.useChar = False
        self.useExtraChar = False

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
                    self.active = False
                    self.color = COLOR_INACTIVE
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    buf = event.unicode
                    if self.useExtraChar:
                        self.text += event.unicode

                    elif self.useNum and buf.isnumeric():
                        self.text += event.unicode

                    elif self.useChar and buf.isalpha():
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
txts = ''

input_box1 = InputBox(100, 100, 140, 32)
input_box1.useChar = True
input_box2 = InputBox(100, 200, 140, 32)
input_box2.useChar = True
input_box3 = InputBox(100, 300, 140, 32)
input_box3.useNum = True
input_boxes = [input_box1, input_box2, input_box3]

txtBox1 = TextBox(100,75,"First Name")
txtBox2 = TextBox(100,175,"Last Name")
txtBox3 = TextBox(100,275,"Age")
txtBox4 = TextBox(610,335,"Submit")
txtBox5 = TextBox(100,425, txts)
txtBoxes = [txtBox1, txtBox2, txtBox3, txtBox4, txtBox5]

submitButton = Button(600,300,100,100,0,0,0,5)

while(run):
    screen.fill((255, 255, 255))

    if submitButton.isMouseOn():
        submitButton.r = 200
        submitButton.g = 200
        submitButton.b = 200
        txtBox4.color = (200,200,200)
        
    else:
        submitButton.r = 0
        submitButton.g = 0
        submitButton.b = 0
        txtBox4.color = (0,0,0)

    for box in input_boxes:
        box.update() 
        box.draw(screen) 

    for box in txtBoxes:
        box.draw(screen)

    submitButton.draw(screen)
        
    for event in pg.event.get():
        
        for box in input_boxes:
            box.handle_event(event)

        if submitButton.isMouseClick(event):
            txtBox5.text = "Hello " + input_box1.text + " " + input_box2.text + "! You are " + input_box3.text + " years old." 

        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()
