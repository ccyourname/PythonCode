#coding=gbk
'''���ݿ�����'''
import pyodbc
#import sys
from tkinter import *
#�������ݿ� ������ʽ��{SQL ServerSQL Server Native Client 11.0}����ʧ��
try:
    conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.226.35.103;DATABASE=IMES3;UID=imes3_user;PWD=yfpoimes31024')
    #�������ݿ��α�
except:
    print("���ݿ�����ʧ��")
cursor = conn.cursor()
#��ȡSQL���
def checkrk():
    e1.delete(0,END)
    barcode = e2.get()
    e2.delete(0, END)
    if  barcode :
        sql1 = ("SELECT * FROM  dbo.MFG_ProductBarcode WHERE Barcode ='%s'" % barcode)    
        cursor.execute(sql1)
        rowall = cursor.fetchall()            
        for rec in rowall:
            if  rec[14]=='99':
                rec[1]=rec[1]+"�ս�����"
                aa=(e1.insert(END,rec[1]))
            else:
                e1.insert(END,"���ս����룬�����Ч")
def releaserk():    
    e1.delete(0,END)
    barcode=e2.get()
    e2.delete(0,END)
    if barcode :
        
        resql2=("update dbo.MFG_ProductBarcode SET BarcodeStatus ='20' WHERE BarcodeStatus='99' and barcode ='%s'" % barcode)
        cursor.execute(resql2)
        conn.commit()
        relbind=("DELETE dbo.MFG_BarcodeBindDet WHERE Barcode = '%s'" % barcode)
        cursor.execute(relbind)
        conn.commit()
        sql2 = ("SELECT * FROM  dbo.MFG_ProductBarcode WHERE Barcode ='%s'" % barcode)    
        cursor.execute(sql2)
        rowall2=cursor.fetchall()
        for rec2 in rowall2:
            if rec2[5]=='1':
                e1.insert(END,rec2[1]+"��ǰ����״̬���ϸ�")
            elif rec2[5]=='2':
                e1.insert(END,rec2[1]+"��ǰ����״̬������")
            elif rec2[5]=='3':
                e1.insert(END,rec2[1]+"��ǰ����״̬������")
            else:
                e1.insert(END,rec2[1]+"��ǰ����״̬��δ֪")
def entrybutton(Event):
    releaserk()

master = Tk()
master.title('������v1')
Label(master,text='����').grid(row=0,column=0,sticky="nsew")
Label(master,text='����').grid(row=0,column=0,sticky="nsew")
e1 = Listbox(master,width='36')
e2 = Entry(master,width='24')
e1.grid(row=1,column=0,columnspan=2,sticky="nsew")
e2.grid(row=0,column=1,sticky="nsew")
#Button guid��ʾ
button1 = Button(master,text='��ѯ',command = checkrk)
button1.grid(row=0,column=2)
button2 = Button(master,text='�������',command = releaserk)
button2.grid(row=1,column=2)
e2.bind('<Return>',entrybutton)
e2.focus_set()

master.mainloop() 
#�ر����ݿ�����
cursor.close()
conn.close() 



