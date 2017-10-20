#coding=utf-8
#__author__ ="Charles.Xie"
#引用数据库连接包
import pyodbc
#链接c_test数据库
conn5 = pyodbc.connect(r'DRIVER={SQL Server};'
                       r'SERVER=localhost;'
                       r'DATABASE=c_test;'
                       r'UID=sa;PWD=student')
#增加数据库游标
cursor5 = conn5.cursor()
#引用TK界面包
#引用tkinter，因为GUI涉及很多包，使用这种引用方式，意思是引用tkinter下所有包
from tkinter import *
class SCS: #新建一个类
    # 函数,self 参数代表类对象本身，默认使用即可，Event是用来事件触发的
    def checkdata(self,Event):
        # 获取e1输入的文本并传递给变量Inbar
        insid=self.master.e1.get()
        # 清空e1的输入
        self.master.e1.delete(0,END)
        # 清空txt的输入
        self.master.txt.delete(0,END)
        # 用于捕获try except之间的代码的异常（既没有成功执行）
        try:
            #获得读取数据库的语句
            sql1 = ("SELECT sid,name FROM"
                    "  Student_mstr WHERE sid = '%s'" % insid)
            for i in cursor5.execute(sql1):
                sid=i[0]
                name=i[1]
            # 获得读取数据库的语句
            sql2 = ("SELECT Sid,course,score FROM "
                    " course_score WHERE sid = '%s'" % insid)
            #定义一个字典dict
            dt={}
            #定义一个列表list
            sscore=[]
            #把查询到的数据存储到sscore中
            for i in cursor5.execute(sql2):
                dt["sid"]=i[0]
                dt["course"]=i[1]
                dt["score"]=i[2]
                sscore.append(dt)
        except:#如果捕获到异常，则执行下列缩进语句
            print("SQL读取失败")
        #判断
        if sid == sscore[0]["sid"]:#判定输入的学号是否有成绩
            for i in sscore:
                #拼接输出字符串
                tmp="姓名："+name+" "+"学科："+i["course"]\
                    +" "+"成绩："+str(i["score"])
                #将输出字符串写进GUI插件
                self.master.txt.insert(END,tmp)
        # 如果不一致，则执行之后缩进的语句
        else:
            self.master.txt.insert(END,"学员信息不存在！请重新扫描！")


    # 函数，用来控制GUI界面
    def gui(self):
        #GUI界面部署
        # 注册一个TK主窗口
        self.master=Tk()
        # TK主窗口的标签
        self.master.title("成绩查询")
        # 主窗口优先显示
        self.master.wm_attributes("-topmost",1)
        #绑定一个标签，位置是第0行第0列，宽度是4个字符
        Label(self.master,text='学号：',width=4).grid(row=0,column=0)
        #输入框，位置是第0行第1列，宽度是15个字符
        self.master.e1=Entry(self.master,width="15")
        self.master.e1.grid(row=0,column=1)
        # #增加个按钮，用于输入学生信息
        # self.master.e2=Button(self.master,text='新增',command=self.modify)
        # self.master.e2.grid(row=0,column=2)
        #输出框，位置是第1行第0列，横跨3列，靠西W排列
        self.master.txt=Listbox(self.master,width=40,)
        self.master.txt.grid(row=1,column=0,columnspan=3,sticky='W')
        #回车事件调用，扫描枪扫描之后自带回车，需要捕获到回车事件后自动执行程序，
        self.master.e1.bind('<Return>',self.checkdata)
        #光标绑定到e1上
        self.master.e1.focus_set()
if __name__=='__main__':
    c=SCS()#定义类对象
    c.gui()#启动gui界面
    c.master.mainloop()#启用GUI
    cursor5.close()#关闭数据库光标
    conn5.close()#关闭数据库连接
