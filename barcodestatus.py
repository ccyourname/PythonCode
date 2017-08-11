#coding=gbk
#__author__ ="谢飞" 
import dbcfg
from tkinter import *
class localbar:
    def scanlog(self,event):
        "producebarcode查询"

        bar=self.e1.get()
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        sql=("SELECT a.Barcode,a.CurrentPartNo,b.PartDesc,c.QualityStatusName,a.IsIsolated,a.BarcodeStatus "
             "FROM  dbo.MFG_ProductBarcode a "
             "LEFT JOIN dbo.MFG_PartDetail b ON a.CurrentPartNo=b.PartNo "
             "LEFT JOIN dbo.QCM_QualityStatus c ON a.QualityStatus=c.QualityStatusCode "
             "WHERE b.FactoryCode='1140' AND a.Barcode='%s'" % bar)
        self.getdata=dbcfg.cursor1.execute(sql)
        for data in self.getdata:
            if data[4]==1:
                data[4]="被隔离"
                a = "x"
            else:
                data[4]="正常"
            if data[5]=="10":
                data[5]="未收货"
                a = "x"
            elif data[5]=="20":
                data[5]="正常"
            elif data[5]=="99":
                data[5]='已被绑定'
                a = "x"
            elif data[5]=="30":
                data[5]="已销售"
                a = "x"
            if data[3] !="合格":
                a="x"
            self.e2.insert(END,data)
            if a=="x":
                self.e2.itemconfig(0, bg="red")
        pass
    def gui(self):
        "TK框架"
        self.master=Tk()
        self.master.title("条码状态查询")
        Label(self.master,text="扫描条码：").grid(row=0,column=0)
        self.e1=Entry(self.master)
        self.e1.grid(row=0,column=1)
        self.e2=Listbox(self.master,width=100,height='2')
        self.e2.grid(row=2,column=0,columnspan=10,sticky="NSEW")
        self.e1.bind("<Return>",self.scanlog)
        self.e1.focus_set()
        # Label(self.master,text="条码").grid(row=1,column=0)
        # Label(self.master, text="物料号").grid(row=1, column=1)
        # Label(self.master, text="物料描述").grid(row=1, column=2)
        # Label(self.master, text="质量状态").grid(row=1, column=3)
        # Label(self.master, text="隔离").grid(row=1, column=4)
        # Label(self.master, text="条码状态").grid(row=1, column=5)


if __name__=="__main__":
    a=localbar()
    a.gui()
    a.master.mainloop()
    dbcfg.cursor1.close()
    dbcfg.conn1.close()
