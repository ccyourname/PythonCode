#coding=gbk
#__author__ ="л��" 
from tkinter import *
import dbcfg
import serchbarlog
import errorcode
import barscanlog
import release99
import barcodestatus
if __name__=="__main__":
    # main=main()
    root=Tk()
    root.title("������")
    x1y1=serchbarlog.Show()
    x1y2=barscanlog.barscan()
    x2y1=barcodestatus.localbar()
    x2y2=release99.releasebar()
    x3y1=errorcode.LED()
    root.x1y1 = Button(root,text='���뱨�ϲ�ѯ',command=x1y1.gui)
    root.x1y1.grid(row=0, column=0,padx=10,pady=10)
    root.x1y2 = Button(root,text='ȫ�������ѯ',command=x1y2.gui)
    root.x1y2.grid(row=0, column=2)
    root.x2y1 = Button(root,text='����״̬��ѯ', width=10,command=x2y1.gui)
    root.x2y1.grid(row=2, column=0)
    root.x2y2 = Button(root,text='�����', width=10,command=x2y2.gui)
    root.x2y2.grid(row=2, column=2,padx=10,pady=10)
    root.x3y1 = Button(root,text='�������ѯ', width=10,command=x3y1.gui)
    root.x3y1.grid(row=3, column=0,padx=10,pady=10)
    root.x3y1 = Button(root,text='������������', width=10)
    root.x3y1.grid(row=3, column=2,padx=10,pady=10)
    # bt1=serchbarlog.show()
    root.mainloop()
    # '''�ر����ݿ�ӿ�'''
    dbcfg.cursor1.close()
    dbcfg.cursor2.close()
    dbcfg.cursor3.close()
    dbcfg.cursor4.close()
    dbcfg.conn1.close()
    dbcfg.conn2.close()
    dbcfg.conn3.close()
    dbcfg.conn4.close()



