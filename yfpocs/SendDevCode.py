#coding=gbk
#__author__ ="л��" 
import dbcfg
from tkinter import *
class SendCode:
    def changecode(self):
        "�滻��Ӧ�豸ID�ķ�����"
        pass
    def serchcode(self):
        "����ԭ�����Ӧ���豸ID"
        pass
    def gui(self):
        "��������"
        self.sendwin=Tk()
        self.sendwin.title("������ͬʱ����������")
        self.sendwin.wm_attributes("-topmost", 1)
        Label(self.sendwin,text="ԭ���룺").grid(row=0,column=0)
        Label(self.sendwin,text="�����룺").grid(row=1,column=0)
        self.e1=Entry(self.sendwin)
        self.e1.grid(row=0,column=1)
        self.e2=Entry(self.sendwin,)
        self.e2.grid(row=1,column=1)
        self.e1.bind("<Return>",self.changecursor1)
        self.e1.focus_set()
        self.e2.bind("<Return>", self.changecursor2)
    def changecursor1(self,event):
        "�л���굽e2"
        print("�л���굽e2")
        self.e2.focus_set()
    def changecursor2(self,event):
        "�л���굽e1"
        print("�л���굽e1")
        self.e1.focus_set()
if __name__=="__main__":
    a=SendCode()#���������
    a.gui()#�������TK����
    a.sendwin.mainloop()
    dbcfg.cursor1.close()
    dbcfg.conn1.close()
    dbcfg.cursor4.close()
    dbcfg.conn4.colse()
