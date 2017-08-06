#coding=gbk
'''数据库连接'''
import pyodbc
#import sys
from tkinter import *
#链接数据库 常熟正式库{SQL ServerSQL Server Native Client 11.0}发布失败
try:
    conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.226.35.103;DATABASE=IMES3;UID=imes3_user;PWD=yfpoimes31024')
    #增加数据库游标
except:
    print("数据库连接失败")
cursor = conn.cursor()
#读取SQL语句
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
                rec[1]=rec[1]+"终结条码"
                aa=(e1.insert(END,rec[1]))
            else:
                e1.insert(END,"非终结条码，解除无效")
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
                e1.insert(END,rec2[1]+"当前质量状态：合格")
            elif rec2[5]=='2':
                e1.insert(END,rec2[1]+"当前质量状态：冻结")
            elif rec2[5]=='3':
                e1.insert(END,rec2[1]+"当前质量状态：报废")
            else:
                e1.insert(END,rec2[1]+"当前质量状态：未知")
def entrybutton(Event):
    releaserk()

master = Tk()
master.title('条码解绑v1')
Label(master,text='条码').grid(row=0,column=0,sticky="nsew")
Label(master,text='条码').grid(row=0,column=0,sticky="nsew")
e1 = Listbox(master,width='36')
e2 = Entry(master,width='24')
e1.grid(row=1,column=0,columnspan=2,sticky="nsew")
e2.grid(row=0,column=1,sticky="nsew")
#Button guid标示
button1 = Button(master,text='查询',command = checkrk)
button1.grid(row=0,column=2)
button2 = Button(master,text='解除条码',command = releaserk)
button2.grid(row=1,column=2)
e2.bind('<Return>',entrybutton)
e2.focus_set()

master.mainloop() 
#关闭数据库连接
cursor.close()
conn.close() 



