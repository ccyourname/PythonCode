#coding=gbk
#__author__ ="л��" 
import dbcfg
from tkinter import *
class SendCode:
    def gui(self):
        self.sendwin=Tk()
        self.sendwin.title("������ͬʱ����������")
        Label(self.sendwin,text="ԭ���룺").grid(row=0,column=0)
        Label(self.sendwin,text="�����룺").grid(row=1,column=0)
        self.e1=Entry(self.sendwin)
        self.e1.grid(row=0,column=1)
        self.e2=Entry(self.sendwin,)
        self.e2.grid(row=1,column=1)
        self.e1.bind("<Return>",self.changecursor)
        self.e1.focus_set()
    def changecursor(self,event):
        print("�л����")

if __name__=="__main__":
    a=SendCode()#���������
    a.gui()#�������TK����
    a.sendwin.mainloop()
