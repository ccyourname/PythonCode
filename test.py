#coding=gbk
#__author__ ="л��"
from tkinter import *
# tk=Tk()
# def  show():
#     filename = dialo.askopenfile()
#     print(filename)
# Button(tk,text="dd",command=show).grid(row=1,column=1)
# tk.mainloop()
# g=lambda x:x*x*x
# print(g(2))
# print(list(filter(lambda x:x%2,range(20))))#ɸѡ��filter �ų���ż��
# print(list(map(lambda x:x*2,range(20))))  #map ���ڶ�ֵ�����һֵ����
# sql=("scan bar"
#      "code "
#      "log %s" % 'mes3')
# print(sql)

# from dbcfg import *
# class ca:
#     def show(self):
#         print("������ť�����")
#         cursor4.execute("SELECT TOP 1 DevID,Cmd,Data,SendTime FROM [305_MES2DEV_CMD] WHERE Cmd ='AT170516150583'ORDER BY ID DESC")
#         getdata=cursor4.fetchall()
#         for data in getdata:
#             print(data)
#     def gui(self):
#         self.tk=Tk()
#         self.tk.title("�����˵�")
#         self.btn=Button(self.tk,text="������ť",command=self.show)
#         self.btn.grid(row=0,column=0,padx=10,pady=10)
#
# if __name__=="__main__":
#     tk1=Tk()
#     tk1.title("������")
#     cc=ca()
#     btn=Button(tk1,text="����",command=cc.gui)
#     btn.grid(row=1,column=1)
#     tk1.mainloop()
tk=Tk()
e1=Entry(tk)
e1.grid(row=0,column=0)
e2=Entry(tk)
e2.grid(row=1,column=0)
tk.mainloop()

