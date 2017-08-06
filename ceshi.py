#coding=gbk
#__author__ ="谢飞"
import  pyodbc
from tkinter import *
from tkinter import *

root=Tk()

#创建一个框架，在这个框架中响应事件
frame=Frame(root,width=200,height=200,background='green')

def callBack(event):
    print(event.keysym)

frame.bind('<Return>',callBack)
frame.pack()

#当前框架被选中，意思是键盘触发，只对这个框架有效
frame.focus_set()

mainloop()
'''
#链接数据库 常熟正式库
conn1 = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.226.35.103;DATABASE=IMES3;UID=imes3_user;PWD=yfpoimes31024')
#增加数据库游标
cursor1 = conn1.cursor()
#链接数据库 安亭正式库
conn2 = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.250.16.88;DATABASE=IMES3;UID=imes3_user;PWD=piwoiefjoifj')
#增加数据库游标
cursor2 = conn2.cursor()
def checklog():
    barcode = e1.get()
    print(barcode)
    cursor1.execute("SELECT a.Barcode ,a.OrigPartNo ,a.OrigPartVersion,a.OrigQualityStatus ,a.NewPartNo,a.NewPartVersion,a.NewQualityStatus,b.ScanSiteName,a.ActionCode FROM dbo.MFG_BarcodeScanLog a INNER JOIN dbo.MFG_ScanSite b ON a.ScanSiteCode =b.ScanSiteCode  WHERE a.Barcode = '%s'" % barcode)
    getbar=cursor1.fetchall()
    for bar in getbar():
        a =(e2.inert(END,bar[0]))
root = Tk()
root.title('条码扫描记录查询')
Label(root,text='条码：').grid(row=0,column=0)
e1=Entry(root).grid(row=0,column=1)
e2=Listbox(root).grid(row=1,column=1)
btn1 = Button(root,text='查询',command=checklog).grid(row=0,column=2)

mainloop()
cursor1.close()
cursor2.close()
conn1.close()
conn2.close()

'''