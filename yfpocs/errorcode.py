#coding=gbk
#__author__ ="谢飞" 
from tkinter import *
from tkinter import ttk
from dbcfg import  *
import threading
cursor4 = conn4.cursor()
class LED():#tkinter 主窗口
    def checkdata(self):
        self.errwin.l1.delete(0,END)
        self.errwin.l2.delete(0, END)
        self.errwin.l3.delete(0, END)
        barcode1=self.errwin.e1.get()
        barcode2=self.errwin.e2.get()
        deviceid=self.errwin.e3.get()
        sql1=("SELECT TOP 1 DevID,Cmd,Data,SendTime FROM [%s_MES2DEV_CMD] WHERE Cmd ='%s'ORDER BY ID DESC" %(deviceid,barcode1))
        cursor4.execute(sql1)
        getdevice1=cursor4.fetchall()
        sql2 = ("SELECT TOP 1 DevID,Cmd,Data,SendTime FROM [%s_MES2DEV_CMD] WHERE Cmd ='%s'ORDER BY ID DESC" % (deviceid, barcode2))
        cursor4.execute(sql2)
        getdevice2 = cursor4.fetchall()
        for i1 in getdevice1:
            self.errwin.l1.insert(END,i1[0])
            self.errwin.l2.insert(END,i1[1])
            self.errwin.l3.insert(END,i1[2])
        for i2 in getdevice2:
            self.errwin.l1.insert(END,i2[0])
            self.errwin.l2.insert(END,i2[1])
            self.errwin.l3.insert(END,i2[2])
    def gui(self):
        self.errwin=Tk()
        self.errwin.title("防错码查询")
        Label(self.errwin,text="主条码：").grid(row=0,column=0)
        self.errwin.e1=Entry(self.errwin)
        self.errwin.e1.grid(row=0,column=1)
        Label(self.errwin,text="条码：").grid(row=1,column=0)
        self.errwin.e2=Entry(self.errwin)
        self.errwin.e2.grid(row=1,column=1)
        # #创建下拉菜单
        # self.root.cbox=StringVar()
        # self.root.cboxchose=ttk.Combobox(self.root,width='6',textvariable=self.root.cbox,state='readonly')#设定菜单框
        # self.root.cboxchose.grid(row=1,column=2)#标记位置
        # s=('前保','后保','扰流板','尾门')
        # self.root.cboxchose['values']=s
        # self.root.cboxchose.current(0)#默认显示第0字段
        Label(self.errwin,text="设备ID：",width=6).grid(row=0,column=2,sticky=W)
        self.errwin.e3=Entry(self.errwin,width=3)
        self.errwin.e3.grid(row=0,column=3,sticky=W)
        Label(self.errwin,text="ID").grid(row=3,column=0)
        Label(self.errwin,text="条码").grid(row=3, column=1)
        Label(self.errwin,text="防错码").grid(row=3, column=4)
        self.errwin.l1=Listbox(self.errwin,width=6)
        self.errwin.l1.grid(row=4,column=0)
        self.errwin.l2=Listbox(self.errwin)
        self.errwin.l2.grid(row=4,column=1)
        self.errwin.l3=Listbox(self.errwin,width=60)
        self.errwin.l3.grid(row=4,column=2,columnspan=10)
        self.errwin.bt1=Button(self.errwin,text="查询",command=self.checkdata)
        self.errwin.bt1.grid(row=1,column=2)
# t=threading.Thread(target=)
# t.start()
if __name__=="__main__":
    a=LED()
    a.gui()
    a.errwin.mainloop()
    cursor4.close()
    conn4.close()