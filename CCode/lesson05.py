#coding=utf-8
#__author__ ="Charles.Xie"
from tkinter import *
import pyodbc
#链接c_test数据库
conn5 = pyodbc.connect(r'DRIVER={SQL Server};'
                       r'SERVER=localhost;'
                       r'DATABASE=c_test;'
                       r'UID=sa;PWD=student')
#增加数据库游标
cursor5 = conn5.cursor()
class Update_data:
    def __init__(self):
        #gui界面定义布局
        self.topdet=Tk()
        self.topdet.title("学生明细维护")
        self.topdet.wm_attributes("-topmost", 1)
        self.lsid=Label(self.topdet,text='学号：')
        self.lsid.grid(row=0,column=0)
        self.lname=Label(self.topdet,text='姓名：')
        self.lname.grid(row=1,column=0)
        self.lsex=Label(self.topdet,text='性别：')
        self.lsex.grid(row=2,column=0)
        self.lold=Label(self.topdet,text='年龄：')
        self.lold.grid(row=3,column=0)
        self.sid=Entry(self.topdet)
        self.sid.grid(row=0,column=1)
        self.name=Entry(self.topdet)
        self.name.grid(row=1,column=1)
        self.sex=Entry(self.topdet)
        self.sex.grid(row=2,column=1)
        self.old=Entry(self.topdet)
        self.old.grid(row=3,column=1)
        #按钮触发事件，当按下按钮是，触发doupdate函数
        self.modify=Button(self.topdet,text='新增',command=self.doupdate)
        self.modify.grid(row=4,column=1)
    def doupdate(self):
        #读取GUI界面写入数据，并清空
        sid=self.sid.get()
        name=self.name.get()
        sex=self.sex.get()
        old=self.old.get()
        self.sid.delete(0,END)
        self.name.delete(0,END)
        self.sex.delete(0,END)
        self.old.delete(0,END)
        #判断写入值是否为空
        if sid =='':
            print("缺少学号")
        elif name =='':
            print("缺少名字")
        elif sex =='':
            print("缺少性别")
        elif old =='':
            print("缺少年龄")
        else:
            #插入SQL拼接
            mstrsql=("INSERT dbo.Student_mstr "
                     "( Sid, Name )VALUES  ( ?,?)" )
            detsql=("INSERT dbo.Student_det "
                    "( Sid, sex,old )VALUES  ( ?,?,?)")
            try:
                mstr_args=(sid,name)
                det_args=(sid,sex,old)
                #执行SQL
                cursor5.execute(mstrsql,mstr_args)
                cursor5.execute(detsql,det_args)
                #提交数据库更新
                cursor5.commit()
            except:
                print("SQL执行失败！！")
if __name__=="__main__":
    #定义类对象
    u=Update_data()
    #执行gui
    u.topdet.mainloop()
    #关闭数据库连接
    cursor5.close()
    conn5.close()