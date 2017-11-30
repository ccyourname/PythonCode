#coding=utf-8
#__author__ ="Charles.Xie" 
from tkinter import *
from tkinter import ttk
import pyodbc
#链接c_test数据库
conn5 = pyodbc.connect(r'DRIVER={SQL Server};'
                       r'SERVER=localhost;'
                       r'DATABASE=c_test;'
                       r'UID=sa;PWD=student')
#增加数据库游标
cursor5 = conn5.cursor()
class up:
    def en(self,Event):
        self.id =self.sid.get()
        self.sid.delete(0,END)
        name_sql=("SELECT Name FROM  dbo.Student_mstr WHERE Sid = '%s'" % self.id)
        try:
            name=[i[0] for i in cursor5.execute(name_sql)]
            self.stk.set(name[0])
        except:
            print("学号不存在！")
        # print(name,self.stk)
        # self.master.update()
    def do(self):
        # self.score.bind()
        # print(self.cboxchose,self.cboxchose.get())
        course=self.cboxchose.get()
        score=self.score.get()
        course=("update  dbo.course_score SET score ='%s' "
                "WHERE Sid = '%s' AND course='%s'"
                % (score,self.id,course))
        try:
            cursor5.execute(course)
            cursor5.commit()
        except:
            print("更新失败")
    def __init__(self):
        self.master=Tk()
        self.master.title("成绩更新")
        Label(self.master,text='学号：').grid(row=0,column=0,padx=5,pady=5)
        Label(self.master,text='姓名：').grid(row=1,column=0,padx=5,pady=5)
        self.sid=Entry(self.master,)
        self.sid.grid(row=0,column=1,padx=5,pady=5)
        #动态修改Lable描述
        self.stk=StringVar()
        Label(self.master,textvariable=self.stk,fg='blue').grid(row=1,column=1,padx=5,pady=5)
        #创建下拉菜单
        self.cbox=StringVar()
        self.cboxchose=ttk.Combobox(self.master,width=18,
                                    textvariable=self.cbox,
                                    state='readonly')#设定菜单框
        self.cboxchose.grid(row=2,column=1,padx=5,pady=5)#标记位置
        Label(self.master,text='课程：').grid(row=2,column=0,padx=5,pady=5)
        self.cboxchose['values']=('语文','数学','英语')
        self.cboxchose.current(0)#默认显示第0字段
        #下拉菜单结束
        Label(self.master,text='成绩：').grid(row=3,column=0,padx=5,pady=5)
        self.score=Entry(self.master,)
        self.score.grid(row=3,column=1,padx=5,pady=5)
        #事件绑定
        self.sid.bind('<Return>',self.en)
        self.sid.focus_set()
        #按钮事件
        self.btn=Button(self.master,text='更新成绩',command=self.do)
        self.btn.grid(row=4,column=1,padx=5,pady=5)

if __name__=="__main__":
    #定义类对象
    c=up()
    #执行gui
    c.master.mainloop()
    #关闭数据库连接
    cursor5.close()
    conn5.close()