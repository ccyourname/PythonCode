#coding=gbk
#__author__ ="л��" 
from dbcfg import  *
from tkinter import *
#LOG��־����
# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
#logging.disable(logging.CRITICAL)   #log ȡ��
class Show():
    def gui(self):

        self.win=Tk()
        self.win.title="�����ж�"
        #self.win.wm_attributes("-topmost", 1)
        #self.tk.title("�����ж�")
        Label(self.win,text='���룺').grid(row=0, column=0)
        self.win.e1 = Entry(self.win,)
        self.win.e1.grid(row=0, column=1, sticky=W)
        self.win.btn = Button(self.win,text="��ѯ", command=self.display)
        self.win.btn.grid(row=0, column=2)
        self.win.e2 = Listbox(self.win,width='30')
        self.win.e2.grid(row=1, column=0, columnspan=3, sticky=W)
        # ��ť���¼�
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
            print("�����¼��ѯʧ��")
        try:
            for bar in getdata:
                if bar[1]=='3' or bar[1]=='9':
                    bar[1]="�ѱ���"
                    self.win.e2.insert(END,bar)
                else:
                    bar[1]="����δ����"
                    self.win.e2.insert(END,bar)
                    self.win.e2.itemconfig(0,fg='red',bg='black')
                    #logging.debug("xxxxx")  #logд��
        except:
            print("����״̬�ж�ʧ�ܣ�")
    def btndisplay(self,Event):
        self.display()


if __name__=="__main__":
    show = Show()
    tk=Tk()
    tk.title("����Ļ")
    bt=Button(tk,text='��ѯ',command=show.gui)
    bt.grid(row=0,column=0,padx=10,pady=10)
    # show.gui()
    # show.gui(tk)
    #tk.protocol("WM_DELETE_WINDOW", show.colsewin(tk))  # ���ڹرմ����¼�
    mainloop()



# tk=Tk()
# show=show(tk)


#tk.mainloop()
# cursor1.close()
# conn1.close()
