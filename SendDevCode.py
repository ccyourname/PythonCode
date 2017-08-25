#coding=gbk
#__author__ ="谢飞" 
import dbcfg
from tkinter import *
class SendCode:
    def changecode(self):
        "替换对应设备ID的防错码"
        pass
    def serchcode(self):
        "查找原条码对应的设备ID"
        pass
    def gui(self):
        "界面设置"
        self.sendwin=Tk()
        self.sendwin.title("换货后同时更换防错码")
        self.sendwin.wm_attributes("-topmost", 1)
        Label(self.sendwin,text="原条码：").grid(row=0,column=0)
        Label(self.sendwin,text="新条码：").grid(row=1,column=0)
        self.e1=Entry(self.sendwin)
        self.e1.grid(row=0,column=1)
        self.e2=Entry(self.sendwin,)
        self.e2.grid(row=1,column=1)
        self.e1.bind("<Return>",self.changecursor1)
        self.e1.focus_set()
        self.e2.bind("<Return>", self.changecursor2)
    def changecursor1(self,event):
        "切换光标到e2"
        print("切换光标到e2")
        self.e2.focus_set()
    def changecursor2(self,event):
        "切换光标到e1"
        print("切换光标到e1")
        self.e1.focus_set()
if __name__=="__main__":
    a=SendCode()#创建类对象
    a.gui()#调用类的TK函数
    a.sendwin.mainloop()
    dbcfg.cursor1.close()
    dbcfg.conn1.close()
    dbcfg.cursor4.close()
    dbcfg.conn4.colse()
