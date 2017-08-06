#coding=gbk
#__author__ ="谢飞"
from tkinter import *
# tk=Tk()
# def  show():
#     filename = dialo.askopenfile()
#     print(filename)
# Button(tk,text="dd",command=show).grid(row=1,column=1)
# tk.mainloop()
# g=lambda x:x*x*x
# print(g(2))
# print(list(filter(lambda x:x%2,range(20))))#筛选器filter 排除提偶就
# print(list(map(lambda x:x*2,range(20))))  #map 将第二值代入第一值后处理
class ca:
    def show(self):
        print("弹窗按钮被点击")
    def gui(self):
        self.tk=Tk()
        self.tk.title("弹窗菜单")
        self.btn=Button(self.tk,text="弹窗按钮",command=self.show)
        self.btn.grid(row=0,column=0,padx=10,pady=10)

if __name__=="__main__":
    tk1=Tk()
    tk1.title("主界面")
    cc=ca()
    btn=Button(tk1,text="弹窗",command=cc.gui)
    btn.grid(row=1,column=1)
    tk1.mainloop()


