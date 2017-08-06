#coding=gbk
#__author__ ="谢飞" 
from tkinter import *
import dbcfg
import serchbarlog
#from serchbarlog import *

if __name__=="__main__":
    # main=main()
    root=Tk()
    root.title("主界面")
    x1y1=serchbarlog.Show()
    root.btn1 = Button(text='条码报废查询',command=x1y1.gui)
    root.btn1.grid(row=0, column=0,padx=10,pady=10)
    root.btn2 = Button(text='条码记录查询')
    root.btn2.grid(row=0, column=2)
    root.btn3 = Button(text='解除RK', width=10)
    root.btn3.grid(row=2, column=0)
    root.btn4 = Button(text='解除绑定', width=10)
    root.btn4.grid(row=2, column=2,padx=10,pady=10)
    # bt1=serchbarlog.show()
    mainloop()
# '''关闭数据库接口'''
dbcfg.cursor1.close()
dbcfg.cursor2.close()
dbcfg.cursor3.close()
dbcfg.conn1.close()
dbcfg.conn2.close()
dbcfg.conn3.close()



