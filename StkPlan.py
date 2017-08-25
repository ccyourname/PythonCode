#coding=gbk
#__author__ ="л��" 
from tkinter import *
import tkinter.messagebox as mes
import dbcfg
import decimal
import time

class StkPlan:
    def click_search(self):
        self.pno = self.e1.get()[:8]
        self.e1.delete(0,END)
        # self.stkname.delete(0, END)
        # self.partno.delete(0, END)
        # self.partdesc.delete(0, END)
        self.maxqty.delete(0, END)
        self.safeqty.delete(0, END)
        sql_search=("SELECT b.StkName,a.PartNo,c.PartDesc,a.MaxQty,a.SaftyQty "
                    "FROM   dbo.WMS_StkPlanCfg a LEFT JOIN dbo.WMS_StkMstr b ON a.StkCode=b.StkCode "
                    "LEFT JOIN dbo.MFG_PartDetail c ON a.PartNo=c.PartNo "
                    "WHERE a.PartNo ='%s' AND c.FactoryCode='1140' AND b.Enabled='1'" % self.pno)
        dbcfg.cursor1.execute(sql_search)
        data=dbcfg.cursor1.fetchall()
        for dt in data:
            # self.stkname.insert(END,dt[0])
            # self.partno.insert(END, str(dt[1]))
            # self.partdesc.insert(END, dt[2])
            Label(self.master, text=dt[2],width="50").grid(row=1, column=0, sticky="W",columnspan=3)
            self.maxqty.insert(END, int(dt[3]))
            self.safeqty.insert(END, int(dt[4]))
    def click_max(self):
        sql_max = ("update dbo.WMS_StkPlanCfg SET MaxQty='%s'WHERE PartNo = '%s'"
                   %(self.maxqty.get(),self.pno))
        try:
            dbcfg.cursor1.execute(sql_max)
            dbcfg.conn1.commit()
            self.ok=mes.showinfo('',"��߿���޸�Ϊ:"+str(self.maxqty.get()))
            # if self.ok=='ok':
            #     self.e1.focus_set()
        except:
            print("���������ʧ�ܣ�")
    def click_safy(self):
        sql_safy = ("update dbo.WMS_StkPlanCfg SET SaftyQty='%s' WHERE PartNo = '%s'"
                    % (self.safeqty.get(), self.pno))
        try:
            dbcfg.cursor1.execute(sql_safy)
            dbcfg.conn1.commit()
            self.ok=mes.showinfo('',"��ȫ����޸�Ϊ:"+str(self.safeqty.get()))
        except:
            print("���°�ȫ���ʧ�ܣ�")
    def click(self,event):
        self.click_search()
    def click_add(self):
        sql_add="INSERT INTO dbo.WMS_StkPlanCfg( StkCode ,PartNo ,PartVersion ,MaxQty ,MinQty ,SaftyQty ," \
                "ReOrderPoint ,PullBatch ,CreateUserAccount ,CreateMachine ,CreateTime , " \
                "LatestModifyUserAccount ,LatestModifyTime , LatestModifyMachine) " \
                "VALUES  ( ?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        ctime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        m=self.maxqty.get()
        s=self.safeqty.get()
        if m =='':
            m=0
        if s =='':
            s=0
        agrms=['11402300',self.e1.get()[:8],'NORMAL',m,0,s,0,0,'CSDIY','CSDIY',ctime,'CSDIY',ctime,'CSDIY']

        sql_list=("SELECT PartNo FROM  dbo.MFG_PartDetail WHERE PartNo='%s'" % self.e1.get()[:8])
        dbcfg.cursor1.execute(sql_list)
        i=len(dbcfg.cursor1.fetchall())
        if i==0:
            mes.showinfo('', "����Ų����ڣ�")
        else:
            try:
                dbcfg.cursor1.execute(sql_add,agrms)
                dbcfg.conn1.commit()
                mes.showinfo('', "����ţ�"+self.e1.get()[:8]+"\n��߿�棺"+str(m)+"\n��ȫ��棺"+str(s)+"\n�����ɹ���")
            except:
                mes.showinfo('', "����ʧ��")


    # def click_pushbtn(self):
    #     self.twin=Tk()
    #     self.twin.title("��ȫ����޸�")
    #     #text="����ţ�"+self.pno
    #     Label(self.twin,text="�����:"+self.pno,fg="red").grid(row=0,column=0)
    #     Label(self.twin,text="��߿��:").grid(row=1,column=0,sticky="W")
    #     Label(self.twin,text="��ȫ���:").grid(row=2,column=0,sticky="W")

    def gui(self):
        self.master=Tk()
        self.master.title("��ȫ�������")
        Label(self.master,text="�����:",width=6).grid(row=0,column=0,padx=5,pady=5,sticky="W")
        self.e1=Entry(self.master,width="9")#����������
        self.e1.grid(row=0,column=1,padx=5,pady=5)
        self.btn=Button(self.master,text="��ѯ",width=7,command=self.click_search)
        self.btn.grid(row=0,column=2,padx=5,pady=5)
        # Label(self.master,text="��λ",width="10").grid(row=1,column=0)
        # Label(self.master,text="�����",width="9").grid(row=1, column=1)
        # Label(self.master,text="�������",width="31").grid(row=1, column=0,sticky="W")
        Label(self.master,text="��߿��:",width="9").grid(row=2, column=0,sticky="W")
        Label(self.master,text="��ȫ���:",width="9").grid(row=3, column=0,sticky="W")
        self.change_max=Button(self.master,text="�޸�����",bg="yellow",command=self.click_max)
        self.change_max.grid(row=2,column=2,padx=5,pady=5)
        self.change_safy=Button(self.master,text="�޸�����",bg="blue",command=self.click_safy)
        self.change_safy.grid(row=3,column=2,padx=5,pady=5)
        self.change_safy=Button(self.master,text="����",bg="RED",command=self.click_add)
        self.change_safy.grid(row=4,column=1,padx=5,pady=5)
        # self.stkname=Listbox(self.master,width=10,height=2)
        # self.stkname.grid(row=2,column=0)
        # self.partno=Listbox(self.master,width="9",height=2)
        # self.partno.grid(row=2,column=1)
        # self.partdesc=Listbox(self.master,width="50",height=2)
        # self.partdesc.grid(row=2,column=2)
        self.maxqty=Entry(self.master,width="9")
        self.maxqty.grid(row=2,column=1)
        self.safeqty=Entry(self.master,width="9")
        self.safeqty.grid(row=3,column=1)
        # self.pushbtn=Button(self.master,text="�޸�����",bg="yellow",command=self.click_pushbtn)
        # self.pushbtn.grid(row=0,column=2)
        self.e1.bind("<Return>",self.click)
        self.e1.focus_set()
if __name__=="__main__":
    c=StkPlan()
    c.gui()
    c.master.mainloop()
    dbcfg.cursor1.close()
    dbcfg.conn1.close()

