#coding=gbk
#__author__ ="谢飞"
#引用数据库连接包
import dbcfg as db
#引用TK界面包
from tkinter import *
class SStdOrdMstr:
    def checkdata(self,Event):
        Inbar=self.master.e1.get()
        self.master.e1.delete(0,END)
        self.master.txt.delete(0,END)
        try:
            # 获取MFG_ProductBarcode表的配置
            sql1 = ("SELECT StdOrdCfg FROM  dbo.MFG_ProductBarcode WHERE Barcode = '%s'" % Inbar)
            pbar = [i[0] for i in db.cursor1.execute(sql1)]
            # 获取MFG_ProductBarcode表的配置
            sql2 = ("SELECT DISTINCT StdOrdCfg FROM  dbo.MFG_ProdBarCodeCCRComps WHERE BarCode = '%s'" % Inbar)
            pbarccr = [i[0] for i in db.cursor1.execute(sql2)]
        except:
            print("SQL读取失败")
        #判断
        # print(pbar,pbarccr)
        if pbar ==pbarccr:
            sql3=("SELECT Description FROM  dbo.LGS_CustStdOrdMstr WHERE StdOrdCfg = '%s'" % pbar[0])
            desc=[i[0] for i in db.cursor1.execute(sql3)]
            self.master.txt.insert(END,desc[0])
        else:
            self.master.txt.insert(END,"无效预排续条码，请补条码！")
    def gui(self):
        #GUI界面部署
        self.master=Tk()
        self.master.title("配置查询")
        self.master.wm_attributes("-topmost",1)
        Label(self.master,text='条码：',width=4).grid(row=0,column=0)
        #输入框
        self.master.e1=Entry(self.master,width="15")
        self.master.e1.grid(row=0,column=1)
        #输出框
        # self.text=StringVar()
        # self.master.msg=Message(self.master,textvariable=self.text,width='360')
        # self.master.msg.grid(row=1,column=0,columnspan=3,sticky='W')
        self.master.txt=Entry(self.master,width=40,)
        self.master.txt.grid(row=1,column=0,columnspan=3,sticky='W')
        #回车事件调用
        self.master.e1.bind('<Return>',self.checkdata)
        #光标绑定
        self.master.e1.focus_set()
if __name__=='__main__':
    c=SStdOrdMstr()
    c.gui()
    c.master.mainloop()
    db.cursor1.close()
    db.conn1.close()
