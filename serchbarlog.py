#coding=gbk
#__author__ ="谢飞" 
from dbcfg import  *
from tkinter import *
#LOG日志增加
# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
#logging.disable(logging.CRITICAL)   #log 取消
class Show():
    def gui(self):

        self.win=Tk()
        self.win.title="报废判定"
        #self.win.wm_attributes("-topmost", 1)
        #self.tk.title("报废判定")
        Label(self.win,text='条码：').grid(row=0, column=0)
        self.win.e1 = Entry(self.win,)
        self.win.e1.grid(row=0, column=1, sticky=W)
        self.win.btn = Button(self.win,text="查询", command=self.display)
        self.win.btn.grid(row=0, column=2)
        self.win.e2 = Listbox(self.win,width='30')
        self.win.e2.grid(row=1, column=0, columnspan=3, sticky=W)
        # 按钮绑定事件
        self.win.e1.bind('<Return>', self.btndisplay)
        self.win.e1.focus_set()
    def display(self):
        self.win.e2.delete(0,END)
        barcode=self.win.e1.get()
        self.win.e1.delete(0,END)
        sql = ("SELECT Barcode,QualityStatus FROM  dbo.MFG_ProductBarcode  WHERE  Barcode ='%s'" % barcode)
        try:
            getdata = cursor1.execute(sql)
        except:
            print("条码记录查询失败")
        try:
            for bar in getdata:
                if bar[1]=='3' or bar[1]=='9':
                    bar[1]="已报废"
                    self.win.e2.insert(END,bar)
                else:
                    bar[1]="条码未报废"
                    self.win.e2.insert(END,bar)
                    self.win.e2.itemconfig(0,fg='red',bg='black')
                    #logging.debug("xxxxx")  #log写入
        except:
            print("报废状态判定失败！")
    def btndisplay(self,Event):
        self.display()


if __name__=="__main__":
    show = Show()
    tk=Tk()
    tk.title("主屏幕")
    bt=Button(tk,text='查询',command=show.gui)
    bt.grid(row=0,column=0,padx=10,pady=10)
    # show.gui()
    # show.gui(tk)
    #tk.protocol("WM_DELETE_WINDOW", show.colsewin(tk))  # 窗口关闭触发事件
    mainloop()



# tk=Tk()
# show=show(tk)


#tk.mainloop()
# cursor1.close()
# conn1.close()
