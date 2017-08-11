# #coding=gbk
# #__author__ ="谢飞"
# 文件分割
def savefile(boy,gril,n):
     a_file_name="d://a"+str(n)+".txt"
     b_file_name = "d://b" + str(n) + ".txt"
     a_file=open(a_file_name,"w")
     b_file=open(b_file_name,"w")
     a_file.writelines(boy)
     b_file.writelines(gril)

     a_file.close()
     b_file.close()
def splitfile(file_name):
     f=open(file_name)
     a=[]
     b=[]
     n=1
     for file_each in f:
          if file_each[:4] !="====":
               (sex,speak)=file_each.split(":",1)
               if sex=="a":
                    a.append(speak)
               elif sex=="b":
                    b.append(speak)
          else:
               savefile(a,b,n)
               a=[]
               b=[]
               n+=1
     savefile(a, b, n)
     f.close()

splitfile("d://xx01.txt")


# def hano(n,x,y,z):
#      "汉诺塔计算"
#      if n==1:
#           print(x+"-->"+z)
#      else:
#
#           hano(n-1,x,z,y)
#           print(x + "-->" + z)
#           hano(n-1,y,x,z)
# a=hano(64,"x","y","z")


# def f(n):
#      x1=1
#      x2=1
#      x3=1
#      while n>2:
#          x3=x1+x2
#          x1=x2
#          x2=x3
#          n=n-1
#      return x3
#
#
# result=f(40)
# print(result)




# from tkinter import *
# # tk=Tk()
# # def  show():
# #     filename = dialo.askopenfile()
# #     print(filename)
# # Button(tk,text="dd",command=show).grid(row=1,column=1)
# # tk.mainloop()
# # g=lambda x:x*x*x
# # print(g(2))
# # print(list(filter(lambda x:x%2,range(20))))#筛选器filter 排除提偶就
# # print(list(map(lambda x:x*2,range(20))))  #map 将第二值代入第一值后处理
# # sql=("scan bar"
# #      "code "
# #      "log %s" % 'mes3')
# # print(sql)
#
# # from dbcfg import *
# # class ca:
# #     def show(self):
# #         print("弹窗按钮被点击")
# #         cursor4.execute("SELECT TOP 1 DevID,Cmd,Data,SendTime FROM [305_MES2DEV_CMD] WHERE Cmd ='AT170516150583'ORDER BY ID DESC")
# #         getdata=cursor4.fetchall()
# #         for data in getdata:
# #             print(data)
# #     def gui(self):
# #         self.tk=Tk()
# #         self.tk.title("弹窗菜单")
# #         self.btn=Button(self.tk,text="弹窗按钮",command=self.show)
# #         self.btn.grid(row=0,column=0,padx=10,pady=10)
# #
# # if __name__=="__main__":
# #     tk1=Tk()
# #     tk1.title("主界面")
# #     cc=ca()
# #     btn=Button(tk1,text="弹窗",command=cc.gui)
# #     btn.grid(row=1,column=1)
# #     tk1.mainloop()
# def change(event):
#      e1.focus_set()
# def ask(event):
#
#      e2.focus_set()
# tk=Tk()
# e1=Entry(tk)
# e1.grid(row=0,column=0)
# e2=Entry(tk)
# e2.grid(row=1,column=0)
# e1.bind("<Return>",ask)
# e2.bind("<Return>",change)
# e1.focus_set()
# tk.mainloop()
#
