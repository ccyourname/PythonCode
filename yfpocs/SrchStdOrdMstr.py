#coding=gbk
#__author__ ="Charles.Xie"
#引用数据库连接包
import dbcfg as db  #引用链接数据库的程序，并在本程序中命名为db
#引用TK界面包
from tkinter import * #GUI界面包进入，因为GUI涉及很多包，使用这种引用方式，意思是引用tkinter下所有包
class SStdOrdMstr: #新建一个类
    def checkdata(self,Event):#函数,self 参数代表类对象本身，默认使用即可，Event是用来事件触发的
        Inbar=self.master.e1.get()#获取e1输入的文本并传递给变量Inbar
        self.master.e1.delete(0,END)#清空e1的输入
        self.master.txt.delete(0,END)#清空txt的输入
        try:#用于捕获try except之间的代码的异常（既没有成功执行）
            # 获取MFG_ProductBarcode表的配置
            #获得读取数据库的语句
            sql1 = ("SELECT StdOrdCfg FROM  dbo.MFG_ProductBarcode WHERE Barcode = '%s'" % Inbar)
            pbar = [i[0] for i in db.cursor1.execute(sql1)]#执行SQL1,并赋值给pbar
            # 获取MFG_ProductBarcode表的配置
            # 获得读取数据库的语句
            sql2 = ("SELECT DISTINCT StdOrdCfg FROM  dbo.MFG_ProdBarCodeCCRComps WHERE BarCode = '%s'" % Inbar)
            pbarccr = [i[0] for i in db.cursor1.execute(sql2)]#执行SQL2并赋值给pbarccr
        except:#如果捕获到异常，则执行下列缩进语句
            print("SQL读取失败")
        #判断
        # print(pbar,pbarccr)
        if pbar ==pbarccr:#判定pbar和pbarccr是否一致
            sql3=("SELECT Description FROM  dbo.LGS_CustStdOrdMstr WHERE StdOrdCfg = '%s'" % pbar[0])
            desc=[i[0] for i in db.cursor1.execute(sql3)]
            self.master.txt.insert(END,desc[0])
        else:#如果不一致，则执行之后缩进的语句
            self.master.txt.insert(END,"无效预排续条码，请补条码！")
    def gui(self):#函数，用来控制GUI界面
        #GUI界面部署
        self.master=Tk()#注册一个TK主窗口
        self.master.title("配置查询")#IK主窗口的标签
        self.master.wm_attributes("-topmost",1)#主窗口优先显示
        #绑定一个标签，位置是第0行第0列，宽度是4个字符
        Label(self.master,text='条码：',width=4).grid(row=0,column=0)
        #输入框，位置是第0行第1列，宽度是15个字符
        self.master.e1=Entry(self.master,width="15")
        self.master.e1.grid(row=0,column=1)
        #输出框，位置是第1行第0列，横跨3列，靠西W排列
        # self.text=StringVar()
        # self.master.msg=Message(self.master,textvariable=self.text,width='360')
        # self.master.msg.grid(row=1,column=0,columnspan=3,sticky='W')
        self.master.txt=Entry(self.master,width=40,)
        self.master.txt.grid(row=1,column=0,columnspan=3,sticky='W')
        #回车事件调用，扫描枪扫描之后自带回车，需要捕获到回车事件后自动执行程序，
        self.master.e1.bind('<Return>',self.checkdata)
        #光标绑定到e1上
        self.master.e1.focus_set()
if __name__=='__main__':
    c=SStdOrdMstr()#定义类对象
    c.gui()#启动gui界面
    c.master.mainloop()#启用GUI
    db.cursor1.close()#关闭数据库光标
    db.conn1.close()#关闭数据库连接
