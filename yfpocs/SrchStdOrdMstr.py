#coding=gbk
#__author__ ="л��"
#�������ݿ����Ӱ�
import dbcfg as db
#����TK�����
from tkinter import *
class SStdOrdMstr:
    def checkdata(self,Event):
        Inbar=self.master.e1.get()
        self.master.e1.delete(0,END)
        self.master.txt.delete(0,END)
        try:
            # ��ȡMFG_ProductBarcode�������
            sql1 = ("SELECT StdOrdCfg FROM  dbo.MFG_ProductBarcode WHERE Barcode = '%s'" % Inbar)
            pbar = [i[0] for i in db.cursor1.execute(sql1)]
            # ��ȡMFG_ProductBarcode�������
            sql2 = ("SELECT DISTINCT StdOrdCfg FROM  dbo.MFG_ProdBarCodeCCRComps WHERE BarCode = '%s'" % Inbar)
            pbarccr = [i[0] for i in db.cursor1.execute(sql2)]
        except:
            print("SQL��ȡʧ��")
        #�ж�
        # print(pbar,pbarccr)
        if pbar ==pbarccr:
            sql3=("SELECT Description FROM  dbo.LGS_CustStdOrdMstr WHERE StdOrdCfg = '%s'" % pbar[0])
            desc=[i[0] for i in db.cursor1.execute(sql3)]
            self.master.txt.insert(END,desc[0])
        else:
            self.master.txt.insert(END,"��ЧԤ�������룬�벹���룡")
    def gui(self):
        #GUI���沿��
        self.master=Tk()
        self.master.title("���ò�ѯ")
        self.master.wm_attributes("-topmost",1)
        Label(self.master,text='���룺',width=4).grid(row=0,column=0)
        #�����
        self.master.e1=Entry(self.master,width="15")
        self.master.e1.grid(row=0,column=1)
        #�����
        # self.text=StringVar()
        # self.master.msg=Message(self.master,textvariable=self.text,width='360')
        # self.master.msg.grid(row=1,column=0,columnspan=3,sticky='W')
        self.master.txt=Entry(self.master,width=40,)
        self.master.txt.grid(row=1,column=0,columnspan=3,sticky='W')
        #�س��¼�����
        self.master.e1.bind('<Return>',self.checkdata)
        #����
        self.master.e1.focus_set()
if __name__=='__main__':
    c=SStdOrdMstr()
    c.gui()
    c.master.mainloop()
    db.cursor1.close()
    db.conn1.close()
