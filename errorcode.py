#coding=gbk
#__author__ ="л��" 
from tkinter import *
from tkinter import ttk
import pyodbc
import threading
#�������ݿ� ������ʽ��3.0
conn1 = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.226.35.103;DATABASE=DevComm;UID=device_user;PWD=yfpodevice_user')
#�������ݿ��α�
cursor1 = conn1.cursor()
class LED():#tkinter ������
    def checkdata(self):
        barcode1=self.root.e1.get()
        barcode2=self.root.e2.get()
        deviceid=self.root.e3.get()
        cursor1.excute=("SELECT TOP 1 DevID,Cmd,Data,SendTime FROM DevComm.dbo.[%s_MES2DEV_CMD] WHERE Cmd ='%s'ORDER BY ID DESC " %(deviceid,barcode1))
        getdevice=conn1.fetchall()
        for i in getdevice:
            print(i)
    def __init__(self):
        self.root=Tk()
        self.root.title("�������ѯ")
        Label(text="�����룺").grid(row=0,column=0)
        self.e1=Entry()
        self.e1.grid(row=0,column=1)
        Label(text="���룺").grid(row=1,column=0)
        self.e2=Entry()
        self.e2.grid(row=1,column=1)
        # #���������˵�
        # self.root.cbox=StringVar()
        # self.root.cboxchose=ttk.Combobox(self.root,width='6',textvariable=self.root.cbox,state='readonly')#�趨�˵���
        # self.root.cboxchose.grid(row=1,column=2)#���λ��
        # s=('ǰ��','��','������','β��')
        # self.root.cboxchose['values']=s
        # self.root.cboxchose.current(0)#Ĭ����ʾ��0�ֶ�
        Label(text="�豸ID��",width=6).grid(row=0,column=2,sticky=W)
        self.root.e3=Entry(width=3)
        self.root.e3.grid(row=0,column=3,sticky=W)
        Label(text="ID").grid(row=3,column=0)
        Label(text="����").grid(row=3, column=1)
        Label(text="������").grid(row=3, column=4)
        self.root.l1=Listbox(width=6)
        self.root.l1.grid(row=4,column=0)
        self.root.l2=Listbox()
        self.root.l2.grid(row=4,column=1)
        self.root.l3=Listbox(width=30)
        self.root.l3.grid(row=4,column=2,columnspan=10)
        self.root.bt1=Button(text="��ѯ",command=self.checkdata)
        self.root.bt1.grid(row=1,column=2)





# t=threading.Thread(target=)
# t.start()
a=LED()
a.root.mainloop()
cursor1.close()
conn1.close()