#coding=gbk
#__author__ ="л��" 
from tkinter import *
import test
if __name__=="__main__":
    tk1=Tk()
    tk1.title("������")
    cc=test.ca()
    btn=Button(tk1,text="����",command=cc.gui)
    btn.grid(row=1,column=1)
    tk1.mainloop()
