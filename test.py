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
class ca:
    def show(self):
        print("������ť�����")
    def gui(self):
        self.tk=Tk()
        self.tk.title("�����˵�")
        self.btn=Button(self.tk,text="������ť",command=self.show)
        self.btn.grid(row=0,column=0,padx=10,pady=10)

if __name__=="__main__":
    tk1=Tk()
    tk1.title("������")
    cc=ca()
    btn=Button(tk1,text="����",command=cc.gui)
    btn.grid(row=1,column=1)
    tk1.mainloop()


