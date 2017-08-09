#coding=gbk
'''数据库连接'''
#import pyodbc
#import sys
from tkinter import *
import dbcfg
#链接数据库 常熟正式库{SQL ServerSQL Server Native Client 11.0}发布失败
# try:
#     conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.226.35.103;DATABASE=IMES3;UID=imes3_user;PWD=yfpoimes31024')
#     #增加数据库游标
# except:
#     print("数据库连接失败")
# cursor = conn.cursor()
#读取SQL语句
class releasebar:

    def checkrk(self):
        self.e1.delete(0,END)
        barcode = self.e2.get()
        self.e2.delete(0, END)
        if  barcode :
            sql1 = ("SELECT * FROM  dbo.MFG_ProductBarcode WHERE Barcode ='%s'" % barcode)
            dbcfg.cursor1.execute(sql1)
            rowall = dbcfg.cursor1.fetchall()
            for rec in rowall:
                if  rec[14]=='99':
                    rec[1]=rec[1]+"终结条码"
                    aa=(self.e1.insert(END,rec[1]))
                else:
                    self.e1.insert(END,"非终结条码，解除无效")
    def releaserk(self):
        self.e1.delete(0,END)
        barcode=self.e2.get()
        self.e2.delete(0,END)
        if barcode :
        
            resql2=("update dbo.MFG_ProductBarcode SET BarcodeStatus ='20' WHERE BarcodeStatus='99' and barcode ='%s'" % barcode)
            dbcfg.cursor1.execute(resql2)
            dbcfg.conn1.commit()
            relbind=("DELETE dbo.MFG_BarcodeBindDet WHERE Barcode = '%s'" % barcode)
            dbcfg.cursor1.execute(relbind)
            dbcfg.conn1.commit()
            sql2 = ("SELECT * FROM  dbo.MFG_ProductBarcode WHERE Barcode ='%s'" % barcode)
            dbcfg.cursor1.execute(sql2)
            rowall2=dbcfg.cursor1.fetchall()
            for rec2 in rowall2:
                if rec2[5]=='1':
                    self.e1.insert(END,rec2[1]+"当前质量状态：合格")
                elif rec2[5]=='2':
                    self.e1.insert(END,rec2[1]+"当前质量状态：冻结")
                elif rec2[5]=='3':
                    self.e1.insert(END,rec2[1]+"当前质量状态：报废")
                else:
                    self.e1.insert(END,rec2[1]+"当前质量状态：未知")
    def entrybutton(self,Event):
        self.releaserk()
    def gui(self):
        self.master = Tk()
        self.master.title('条码解绑v1')
        Label(self.master, text='条码').grid(row=0, column=0, sticky="nsew")
        Label(self.master, text='条码').grid(row=0, column=0, sticky="nsew")
        self.e1 = Listbox(self.master, width='36')
        self.e2 = Entry(self.master, width='24')
        self.e1.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.e2.grid(row=0, column=1, sticky="nsew")
        # Button guid标示
        button1 = Button(self.master, text='查询', command=self.checkrk)
        button1.grid(row=0, column=2)
        button2 = Button(self.master, text='解除条码', command=self.releaserk)
        button2.grid(row=1, column=2)
        self.e2.bind('<Return>', self.entrybutton)
        self.e2.focus_set()


if __name__=="__main__":
    a=releasebar()
    a.gui()
    a.master.mainloop()
    #关闭数据库连接
    dbcfg.cursor1.close()
    dbcfg.conn1.close()



