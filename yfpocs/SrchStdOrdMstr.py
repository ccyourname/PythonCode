#coding=gbk
#__author__ ="Charles.Xie"
#�������ݿ����Ӱ�
import dbcfg as db  #�����������ݿ�ĳ��򣬲��ڱ�����������Ϊdb
#����TK�����
from tkinter import * #GUI��������룬��ΪGUI�漰�ܶ����ʹ���������÷�ʽ����˼������tkinter�����а�
class SStdOrdMstr: #�½�һ����
    def checkdata(self,Event):#����,self ���������������Ĭ��ʹ�ü��ɣ�Event�������¼�������
        Inbar=self.master.e1.get()#��ȡe1������ı������ݸ�����Inbar
        self.master.e1.delete(0,END)#���e1������
        self.master.txt.delete(0,END)#���txt������
        try:#���ڲ���try except֮��Ĵ�����쳣����û�гɹ�ִ�У�
            # ��ȡMFG_ProductBarcode�������
            #��ö�ȡ���ݿ�����
            sql1 = ("SELECT StdOrdCfg FROM  dbo.MFG_ProductBarcode WHERE Barcode = '%s'" % Inbar)
            pbar = [i[0] for i in db.cursor1.execute(sql1)]#ִ��SQL1,����ֵ��pbar
            # ��ȡMFG_ProductBarcode�������
            # ��ö�ȡ���ݿ�����
            sql2 = ("SELECT DISTINCT StdOrdCfg FROM  dbo.MFG_ProdBarCodeCCRComps WHERE BarCode = '%s'" % Inbar)
            pbarccr = [i[0] for i in db.cursor1.execute(sql2)]#ִ��SQL2����ֵ��pbarccr
        except:#��������쳣����ִ�������������
            print("SQL��ȡʧ��")
        #�ж�
        # print(pbar,pbarccr)
        if pbar ==pbarccr:#�ж�pbar��pbarccr�Ƿ�һ��
            sql3=("SELECT Description FROM  dbo.LGS_CustStdOrdMstr WHERE StdOrdCfg = '%s'" % pbar[0])
            desc=[i[0] for i in db.cursor1.execute(sql3)]
            self.master.txt.insert(END,desc[0])
        else:#�����һ�£���ִ��֮�����������
            self.master.txt.insert(END,"��ЧԤ�������룬�벹���룡")
    def gui(self):#��������������GUI����
        #GUI���沿��
        self.master=Tk()#ע��һ��TK������
        self.master.title("���ò�ѯ")#IK�����ڵı�ǩ
        self.master.wm_attributes("-topmost",1)#������������ʾ
        #��һ����ǩ��λ���ǵ�0�е�0�У������4���ַ�
        Label(self.master,text='���룺',width=4).grid(row=0,column=0)
        #�����λ���ǵ�0�е�1�У������15���ַ�
        self.master.e1=Entry(self.master,width="15")
        self.master.e1.grid(row=0,column=1)
        #�����λ���ǵ�1�е�0�У����3�У�����W����
        # self.text=StringVar()
        # self.master.msg=Message(self.master,textvariable=self.text,width='360')
        # self.master.msg.grid(row=1,column=0,columnspan=3,sticky='W')
        self.master.txt=Entry(self.master,width=40,)
        self.master.txt.grid(row=1,column=0,columnspan=3,sticky='W')
        #�س��¼����ã�ɨ��ǹɨ��֮���Դ��س�����Ҫ���񵽻س��¼����Զ�ִ�г���
        self.master.e1.bind('<Return>',self.checkdata)
        #���󶨵�e1��
        self.master.e1.focus_set()
if __name__=='__main__':
    c=SStdOrdMstr()#���������
    c.gui()#����gui����
    c.master.mainloop()#����GUI
    db.cursor1.close()#�ر����ݿ���
    db.conn1.close()#�ر����ݿ�����
