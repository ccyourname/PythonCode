#coding=gbk
#__author__ ="л��"
import  pyodbc
from tkinter import *
from tkinter import *

root=Tk()

#����һ����ܣ�������������Ӧ�¼�
frame=Frame(root,width=200,height=200,background='green')

def callBack(event):
    print(event.keysym)

frame.bind('<Return>',callBack)
frame.pack()

#��ǰ��ܱ�ѡ�У���˼�Ǽ��̴�����ֻ����������Ч
frame.focus_set()

mainloop()
'''
#�������ݿ� ������ʽ��
conn1 = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.226.35.103;DATABASE=IMES3;UID=imes3_user;PWD=yfpoimes31024')
#�������ݿ��α�
cursor1 = conn1.cursor()
#�������ݿ� ��ͤ��ʽ��
conn2 = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.250.16.88;DATABASE=IMES3;UID=imes3_user;PWD=piwoiefjoifj')
#�������ݿ��α�
cursor2 = conn2.cursor()
def checklog():
    barcode = e1.get()
    print(barcode)
    cursor1.execute("SELECT a.Barcode ,a.OrigPartNo ,a.OrigPartVersion,a.OrigQualityStatus ,a.NewPartNo,a.NewPartVersion,a.NewQualityStatus,b.ScanSiteName,a.ActionCode FROM dbo.MFG_BarcodeScanLog a INNER JOIN dbo.MFG_ScanSite b ON a.ScanSiteCode =b.ScanSiteCode  WHERE a.Barcode = '%s'" % barcode)
    getbar=cursor1.fetchall()
    for bar in getbar():
        a =(e2.inert(END,bar[0]))
root = Tk()
root.title('����ɨ���¼��ѯ')
Label(root,text='���룺').grid(row=0,column=0)
e1=Entry(root).grid(row=0,column=1)
e2=Listbox(root).grid(row=1,column=1)
btn1 = Button(root,text='��ѯ',command=checklog).grid(row=0,column=2)

mainloop()
cursor1.close()
cursor2.close()
conn1.close()
conn2.close()

'''