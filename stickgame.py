#coding=gbk
#__author__ ="谢飞"
from tkinter import *
import random
import time
class Game:
    def __init__(self):#设置画布
        self.tk=Tk()
        self.tk.title("火柴人逃生")
        self.tk.resizable(0,0)
        self.tk.wm_attributes("-topmost",1)
        self.canvas=Canvas(self.tk,width=500,height=500,highlighttickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height=500
        self.canvas_weight=500
        self.bg=PhotoImage(file="logo.ico")
        w=self.bg.width()
        h=self.bg.height()
        for x in (0,5):
            for y in (0,5):
                self.canvas.create_image(x*w,y*h,image =self.bg,anchor='nw')
        self.sprites=[]
        self.running=True
