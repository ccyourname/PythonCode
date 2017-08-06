#coding=gbk
#__author__ ="谢飞" 
from tkinter import *
import test
if __name__=="__main__":
    tk1=Tk()
    tk1.title("主界面")
    cc=test.ca()
    btn=Button(tk1,text="弹窗",command=cc.gui)
    btn.grid(row=1,column=1)
    tk1.mainloop()
