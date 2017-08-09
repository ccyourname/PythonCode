#coding=gbk
#__author__ ="谢飞" 
import dbcfg
from tkinter import *
class SendCode:
    def gui(self):
        self.sendwin=Tk()
        self.sendwin.title("换货后同时更换防错码")
        Label(self.sendwin,text="原条码：").grid(row=0,column=0)
        Label(self.sendwin,text="新条码：").grid(row=1,column=0)
        self.e1=Entry(self.sendwin)
        self.e1.grid(row=0,column=1)
        self.e2=Entry(self.sendwin,)
        self.e2.grid(row=1,column=1)
        self.e1.bind("<Return>",self.changecursor)
        self.e1.focus_set()
    def changecursor(self,event):
        print("切换光标")

if __name__=="__main__":
    a=SendCode()#创建类对象
    a.gui()#调用类的TK函数
    a.sendwin.mainloop()
