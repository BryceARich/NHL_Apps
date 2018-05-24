__author__ = 'brycerich'
import tkinter as tk
from tkinter import *

root = tk.Tk()

CANVAS_WIDTH = 100
CANVAS_HEIGHT = 85
SCALE = 6

def circle(canvas, x, y, r, out, fil, wi):
    id = canvas.create_oval(x-r,y-r,x+r,y+r, outline = out, fill = fil, width = wi)
    return id

def drawRink(canvas):
    # cir1 = canvas.create_oval(101*SCALE, 85*SCALE, (100-28*2)*SCALE, (85-28*2)*SCALE,outline="#000000",width=3)
    cir1 = circle(canvas, (100-28)*SCALE, (85-28)*SCALE, 28*SCALE, "#000000", "#FFFFFF", 3)
    cir2 = circle(canvas, (100-28)*SCALE, (29)*SCALE, 28*SCALE, "#000000", "#FFFFFF", 3)
    cover1 = canvas.create_rectangle((100-29*2)*SCALE,(4/SCALE)*SCALE,(100-28)*SCALE,(85-2/SCALE)*SCALE, outline="#FFFFFF", fill="#FFFFFF")
    cover2 = canvas.create_rectangle((100)*SCALE,(28)*SCALE,(100-28)*SCALE,(85-27)*SCALE,outline="#FFFFFF",fill="#FFFFFF")
    right_ice = canvas.create_rectangle(.5*SCALE,1*SCALE,100*SCALE,85*SCALE, width = 3)

def drawCrease(canvas):
    cir = circle(canvas,(25+64)*SCALE,(85/2)*SCALE,6*SCALE,"#FF0000","#0000FF",3)
    rect = canvas.create_rectangle((25+64+1/SCALE)*SCALE,(85/2-6)*SCALE, (25+64+6)*SCALE,(85/2+6)*SCALE, fill="#FFFFFF", outline="#FFFFFF", width=3)

def drawLines(canvas):
    red_line = canvas.create_line(.5*SCALE,1*SCALE,.5*SCALE,85*SCALE,
        fill="#FF0000",
        width=5)
    canvas.itemconfig(red_line, tags=("red","line"))

    blue_line = canvas.create_line(26*SCALE,1*SCALE,26*SCALE,86*SCALE,
        fill="#0000FF",
        width=3)
    canvas.itemconfig(blue_line, tags=("blue","line"))

    goalie_line = canvas.create_line(89*SCALE,(1+6)*SCALE,89*SCALE,(85-6)*SCALE,
        fill="#FF0000",
        width=3)
    canvas.itemconfig(goalie_line, tags=("red","line"))

def drawFaceoffs(canvas):
    top_circle = circle(canvas,70*SCALE,(85/2-21)*SCALE,15*SCALE,"#FF0000","#FFFFFF",3)
    canvas.itemconfig(top_circle, tags=("red","faceoff"))
    bottom_circle = circle(canvas,70*SCALE,(85/2+22)*SCALE,15*SCALE,"#FF0000","#FFFFFF",3)
    canvas.itemconfig(bottom_circle, tags=("red","faceoff"))
    center_circle = circle(canvas,0*SCALE,(85/2)*SCALE,15*SCALE,"#0000FF","#FFFFFF",3)
    canvas.itemconfig(center_circle, tags=("blue","faceoff"))
    top_in = circle(canvas,70*SCALE,(85/2-21)*SCALE,2*SCALE,"#FF0000","#FF0000",3)
    canvas.itemconfig(top_in, tags=("red","faceoff"))
    bottom_in = circle(canvas,70*SCALE,(85/2+22)*SCALE,2*SCALE,"#FF0000","#FF0000",3)
    canvas.itemconfig(bottom_in, tags=("red","faceoff"))
    center_in = circle(canvas,0*SCALE,(85/2)*SCALE,2*SCALE,"#0000FF","#0000FF",3)
    canvas.itemconfig(center_in, tags=("blue","faceoff"))

def drawHalfIce():
    global w
    w = Canvas(root,
           width=CANVAS_WIDTH*SCALE,
           height=CANVAS_HEIGHT*SCALE)
    w.pack()

    drawRink(w)
    drawFaceoffs(w)
    drawCrease(w)
    drawLines(w)

def main():
    drawHalfIce()
    root.mainloop()

main()