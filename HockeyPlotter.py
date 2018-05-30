__author__ = 'brycerich'
import tkinter as tk
from tkinter import *

root = tk.Tk()

RED = "#FF0000"
BLUE = "#0000FF"
WHITE = "#FFFFFF"
BLACK = "#000000"

class HockeyPlotter:

    outline = WHITE
    fill = WHITE
    SCALE = 6

    def __init__(self, canvas, scale):
        self.canvas = canvas
        self.SCALE = scale

    def set_fill_and_outline(self, outline, fill):
        self.outline = outline
        self.fill = fill

    def circle(self, x, y, r):
        id = self.canvas.create_oval(x-r,y-r,x+r,y+r, outline = self.outline, fill = self.fill, width = 3)
        return id

    def drawHalfRink(self):
        # cir1 = self.canvas.create_oval(101*self.SCALE, 85*self.SCALE, (100-28*2)*self.SCALE, (85-28*2)*self.SCALE,outline=BLACK,width=3)
        self.set_fill_and_outline(BLACK, WHITE)
        cir1 = self.circle( (100-28)*self.SCALE, (85-28)*self.SCALE, 28*self.SCALE, BLACK, WHITE)
        cir2 = self.circle( (100-28)*self.SCALE, (29)*self.SCALE, 28*self.SCALE, BLACK, WHITE)
        cover1 = self.canvas.create_rectangle((100-29*2)*self.SCALE,(4/self.SCALE)*self.SCALE,(100-28)*self.SCALE,(85-2/self.SCALE)*self.SCALE, outline=WHITE, fill=WHITE)
        cover2 = self.canvas.create_rectangle((100)*self.SCALE,(28)*self.SCALE,(100-28)*self.SCALE,(85-27)*self.SCALE,outline=WHITE,fill=WHITE)
        right_ice = self.canvas.create_rectangle(.5*self.SCALE,1*self.SCALE,100*self.SCALE,85*self.SCALE, width = 3)

    def drawFullRink(self):
        self.set_fill_and_outline(BLACK, WHITE)
        cir1 = self.circle( (200-28)*self.SCALE, (85-28)*self.SCALE, 28*self.SCALE)
        cir2 = self.circle( (200-28)*self.SCALE, (29)*self.SCALE, 28*self.SCALE)
        cir3 = self.circle( (29)*self.SCALE, (85-28)*self.SCALE, 28*self.SCALE)
        cir4 = self.circle( (29)*self.SCALE, (29)*self.SCALE, 28*self.SCALE)
        cover1 = self.canvas.create_rectangle((200-29*2)*self.SCALE,(4/self.SCALE)*self.SCALE,(200-28)*self.SCALE,(85-2/self.SCALE)*self.SCALE, outline=WHITE, fill=WHITE)
        cover2 = self.canvas.create_rectangle((200)*self.SCALE,(28)*self.SCALE,(200-28)*self.SCALE,(85-27)*self.SCALE,outline=WHITE,fill=WHITE)
        cover1 = self.canvas.create_rectangle((29*2)*self.SCALE,(4/self.SCALE)*self.SCALE,(28)*self.SCALE,(85-2/self.SCALE)*self.SCALE, outline=WHITE, fill=WHITE)
        cover2 = self.canvas.create_rectangle((1)*self.SCALE,(28)*self.SCALE,(28)*self.SCALE,(85-27)*self.SCALE,outline=WHITE,fill=WHITE)
        right_ice = self.canvas.create_rectangle(1*self.SCALE,1*self.SCALE,200*self.SCALE,85*self.SCALE, width = 3)

    def drawHalfCrease(self):
        self.set_fill_and_outline(RED, BLUE)
        cir = self.circle((25+64)*self.SCALE,(85/2)*self.SCALE,6*self.SCALE,RED,BLUE)
        rect = self.canvas.create_rectangle((25+64+1/self.SCALE)*self.SCALE,(85/2-6)*self.SCALE, (25+64+6)*self.SCALE,(85/2+6)*self.SCALE, fill=WHITE, outline=WHITE, width=3)

    def drawFullCrease(self):
        self.set_fill_and_outline(RED, BLUE)
        cir = self.circle((100+25+64)*self.SCALE,(85/2)*self.SCALE,6*self.SCALE)
        rect = self.canvas.create_rectangle((100+25+64+1/self.SCALE)*self.SCALE,(85/2-6)*self.SCALE, (100+25+64+6)*self.SCALE,(85/2+6)*self.SCALE, fill=WHITE, outline=WHITE, width=3)

        cir2 = self.circle((100-(25+64))*self.SCALE,(85/2)*self.SCALE,6*self.SCALE)
        rect2 = self.canvas.create_rectangle((100-(25+64+1/self.SCALE))*self.SCALE,(85/2-6)*self.SCALE, (100-(25+64+6))*self.SCALE,(85/2+6)*self.SCALE, fill=WHITE, outline=WHITE, width=3)

    def drawHalfLines(self):
        red_line = self.canvas.create_line(.5*self.SCALE,1*self.SCALE,.5*self.SCALE,85*self.SCALE,
            fill=RED,
            width=5)
        self.canvas.itemconfig(red_line, tags=("red","line"))

        blue_line = self.canvas.create_line(26*self.SCALE,1*self.SCALE,26*self.SCALE,86*self.SCALE,
            fill=BLUE,
            width=3)
        self.canvas.itemconfig(blue_line, tags=("blue","line"))

        goalie_line = self.canvas.create_line(89*self.SCALE,(1+6)*self.SCALE,89*self.SCALE,(85-6)*self.SCALE,
            fill=RED,
            width=3)
        self.canvas.itemconfig(goalie_line, tags=("red","line"))

    def drawFullLines(self):
        red_line = self.canvas.create_line((100+.5)*self.SCALE,1*self.SCALE,(100+.5)*self.SCALE,85*self.SCALE,
            fill=RED,
            width=5)
        self.canvas.itemconfig(red_line, tags=("red","line"))

        blue_line = self.canvas.create_line((100+26)*self.SCALE,1*self.SCALE,(100+26)*self.SCALE,86*self.SCALE,
            fill=BLUE,
            width=3)
        self.canvas.itemconfig(blue_line, tags=("blue","line"))

        goalie_line = self.canvas.create_line((100+89)*self.SCALE,(1+6)*self.SCALE,(100+89)*self.SCALE,(85-6)*self.SCALE,
            fill=RED,
            width=3)
        self.canvas.itemconfig(goalie_line, tags=("red","line"))

        blue_line = self.canvas.create_line((100-26)*self.SCALE,1*self.SCALE,(100-26)*self.SCALE,86*self.SCALE,
            fill=BLUE,
            width=3)
        self.canvas.itemconfig(blue_line, tags=("blue","line"))

        goalie_line = self.canvas.create_line((100-89)*self.SCALE,(1+6)*self.SCALE,(100-89)*self.SCALE,(85-6)*self.SCALE,
            fill=RED,
            width=3)
        self.canvas.itemconfig(goalie_line, tags=("red","line"))

    def drawHalfFaceoffs(self):
        self.set_fill_and_outline(RED, WHITE)
        top_circle = self.circle(70*self.SCALE,(85/2-21)*self.SCALE,15*self.SCALE,RED,WHITE)
        self.canvas.itemconfig(top_circle, tags=("red","faceoff"))
        bottom_circle = self.circle(70*self.SCALE,(85/2+22)*self.SCALE,15*self.SCALE,RED,WHITE)
        self.canvas.itemconfig(bottom_circle, tags=("red","faceoff"))

        self.set_fill_and_outline(BLUE, WHITE)
        center_circle = self.circle(0*self.SCALE,(85/2)*self.SCALE,15*self.SCALE,BLUE,WHITE)
        self.canvas.itemconfig(center_circle, tags=("blue","faceoff"))

        self.set_fill_and_outline(RED, RED)
        top_in = self.circle(70*self.SCALE,(85/2-21)*self.SCALE,2*self.SCALE,RED,RED)
        self.canvas.itemconfig(top_in, tags=("red","faceoff"))
        bottom_in = self.circle(70*self.SCALE,(85/2+22)*self.SCALE,2*self.SCALE,RED,RED)
        self.canvas.itemconfig(bottom_in, tags=("red","faceoff"))

        self.set_fill_and_outline(BLUE, BLUE)
        center_in = self.circle(0*self.SCALE,(85/2)*self.SCALE,2*self.SCALE,BLUE,BLUE)
        self.canvas.itemconfig(center_in, tags=("blue","faceoff"))


    def drawFullFaceoffs(self):
        self.set_fill_and_outline(RED, WHITE)
        top_circle = self.circle((100+70)*self.SCALE,(85/2-21)*self.SCALE,15*self.SCALE)
        self.canvas.itemconfig(top_circle, tags=("red","faceoff"))
        bottom_circle = self.circle((100+70)*self.SCALE,(85/2+22)*self.SCALE,15*self.SCALE)
        self.canvas.itemconfig(bottom_circle, tags=("red","faceoff"))
        top_circle = self.circle((100-70)*self.SCALE,(85/2-21)*self.SCALE,15*self.SCALE)
        self.canvas.itemconfig(top_circle, tags=("red","faceoff"))
        bottom_circle = self.circle((100-70)*self.SCALE,(85/2+22)*self.SCALE,15*self.SCALE)
        self.canvas.itemconfig(bottom_circle, tags=("red","faceoff"))

        self.set_fill_and_outline(BLUE, WHITE)
        center_circle = self.circle((100+0)*self.SCALE,(85/2)*self.SCALE,15*self.SCALE)
        self.canvas.itemconfig(center_circle, tags=("blue","faceoff"))

        self.set_fill_and_outline(RED, RED)
        top_in = self.circle((100+70)*self.SCALE,(85/2-21)*self.SCALE,2*self.SCALE)
        self.canvas.itemconfig(top_in, tags=("red","faceoff"))
        bottom_in = self.circle((100+70)*self.SCALE,(85/2+22)*self.SCALE,2*self.SCALE)
        self.canvas.itemconfig(bottom_in, tags=("red","faceoff"))
        top_in = self.circle((100-70)*self.SCALE,(85/2-21)*self.SCALE,2*self.SCALE)
        self.canvas.itemconfig(top_in, tags=("red","faceoff"))
        bottom_in = self.circle((100-70)*self.SCALE,(85/2+22)*self.SCALE,2*self.SCALE)
        self.canvas.itemconfig(bottom_in, tags=("red","faceoff"))

        self.set_fill_and_outline(BLUE, BLUE)
        center_in = self.circle((100+0)*self.SCALE,(85/2)*self.SCALE,2*self.SCALE)
        self.canvas.itemconfig(center_in, tags=("blue","faceoff"))

    def drawHalfIce(self):
        self.drawHalfRink()
        self.drawHalfFaceoffs()
        self.drawHalfCrease()
        self.drawHalfLines()

    def drawFullIce(self):
        self.drawFullRink()
        self.drawFullCrease()
        self.drawFullLines()
        self.drawFullFaceoffs()


def main():
    scale = 6
    CANVAS_WIDTH = 100
    CANVAS_HEIGHT = 85

    canvas = Canvas(root,
               width=CANVAS_WIDTH*scale*2,
               height=CANVAS_HEIGHT*scale*2)
    canvas.pack()
    hp = HockeyPlotter(canvas, 6)
    hp.drawFullIce()
    # hp.drawHalfIce()
    root.mainloop()

main()