#coding=gbk
'''���ݿ�����'''
#import pyodbc
#import sys
from tkinter import *
import dbcfg
#�������ݿ� ������ʽ��{SQL ServerSQL Server Native Client 11.0}����ʧ��
# try:
#     conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.226.35.103;DATABASE=IMES3;UID=imes3_user;PWD=yfpoimes31024')
#     #�������ݿ��α�
# except:
#     print("���ݿ�����ʧ��")
# cursor = conn.cursor()
#��ȡSQL���
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
                    rec[1]=rec[1]+"�ս�����"
                    aa=(self.e1.insert(END,rec[1]))
                else:
                    self.e1.insert(END,"���ս����룬�����Ч")
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
                    self.e1.insert(END,rec2[1]+"��ǰ����״̬���ϸ�")
                elif rec2[5]=='2':
                    self.e1.insert(END,rec2[1]+"��ǰ����״̬������")
                elif rec2[5]=='3':
                    self.e1.insert(END,rec2[1]+"��ǰ����״̬������")
                else:
                    self.e1.insert(END,rec2[1]+"��ǰ����״̬��δ֪")
    def entrybutton(self,Event):
        self.releaserk()
    def gui(self):
        self.master = Tk()
        self.master.title('������v1')
        Label(self.master, text='����').grid(row=0, column=0, sticky="nsew")
        Label(self.master, text='����').grid(row=0, column=0, sticky="nsew")
        self.e1 = Listbox(self.master, width='36')
        self.e2 = Entry(self.master, width='24')
        self.e1.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.e2.grid(row=0, column=1, sticky="nsew")
        # Button guid��ʾ
        button1 = Button(self.master, text='��ѯ', command=self.checkrk)
        button1.grid(row=0, column=2)
        button2 = Button(self.master, text='�������', command=self.releaserk)
        button2.grid(row=1, column=2)
        self.e2.bind('<Return>', self.entrybutton)
        self.e2.focus_set()


if __name__=="__main__":
    a=releasebar()
    a.gui()
    a.master.mainloop()
    #�ر����ݿ�����
    dbcfg.cursor1.close()
    dbcfg.conn1.close()



