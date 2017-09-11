#coding=gbk
'''数据库连接'''
import pyodbc
#import sys

from tkinter import *

#链接数据库 常熟正式库{SQL ServerSQL Server Native Client 11.0}发布失败
conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.226.35.103;DATABASE=IMES3;UID=imes3_user;PWD=yfpoimes31024')
#增加数据库游标 
cursor = conn.cursor()
#读取SQL语句
#rk = 'INN0150012'
'''
def opendb(db):
    #链接数据库 常熟正式库
    conn = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};SERVER=10.226.35.103;DATABASE=IMES3;UID=imes3_user;PWD=yfpoimes31024')
    #增加数据库游标 
    cursor = conn.cursor()    
'''
def checkrk():
    e1.delete(0,END)
    rk = e2.get()
    if  rk :
        sql1 = ("SELECT hucode FROM  dbo.LGS_HUPkgMstr WHERE RackCode ='%s' order by hucode" % rk)    
        cursor.execute(sql1)
        rowall = cursor.fetchall()
        for rec in rowall:
            aa=(e1.insert(END,rec[0]))
      
def releaserk():
    e1.delete(0,END)
    rk=e2.get()
    if rk :
        resql2=("UPDATE dbo.LGS_HUPkgMstr SET RackCode = '' WHERE RackCode = '%s' AND ( PackageStatus = '20' OR PackageStatus = '99' )" %rk)
        cursor.execute(resql2)
        conn.commit()
        sql2 = ("SELECT hucode FROM  dbo.LGS_HUPkgMstr WHERE RackCode ='%s' order by hucode" % rk) 
        cursor.execute(sql2)
        rowall2=cursor.fetchall()
        for rec2 in rowall2:
            bb=(e1.insert(END,rec2[0]))
       
master = Tk()
master.title('RK解绑程序V1')
Label(master,text='HU').grid(row=0,column=0)
Label(master,text='RK').grid(row=0,column=0)
e1 = Listbox(master)
e2 = Entry(master)
e1.grid(row=1,column=1,sticky=E)
e2.grid(row=0,column=1)
#Button guid标示
button1 = Button(master,text='查询',command = checkrk)
button1.grid(row=0,column=2)
button2 = Button(master,text='解除RK',command = releaserk)
button2.grid(row=1,column=2)
master.mainloop() 
cursor.close()
conn.close() 



