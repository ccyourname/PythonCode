#coding=gbk
#__author__ ="л��" 
import dbcfg
from tkinter import *
import time
import threading
class EX_Monitor:
    def check_data(self):
        self.master.e1.delete(0,END)
        self.master.l1.delete(0, END)
        self.master.l2.delete(0, END)
        self.master.l3.delete(0, END)
        self.master.l4.delete(0, END)
        self.master.l5.delete(0, END)
        self.master.l6.delete(0, END)
        self.master.l7.delete(0, END)
        now_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()-7200))
        cogi_sql=("SELECT  a.CogiGUID,a.StkCode,a.PartNo,a.Qty,a.CreateTime ,c.PartDesc "
                  "FROM  dbo.WMS_COGI a LEFT JOIN dbo.MFG_PartDetail c ON a.PartNo=c.PartNo "
                  "WHERE a.IsPost = '0' AND a.IsDel = '0' and c.FactoryCode ='1140'"
                  "and a.CreateTime <'%s'" % now_time )
        rct_sql=("SELECT a.RctBillGuid,a.StkCode,a.PartNo,a.Qty,a.Barcode,b.UserName,a.CreateTime ,c.PartDesc "
                 "FROM  dbo.WMS_StkRctDet a LEFT JOIN dbo.SYS_User b ON a.CreateUserAccount = b.UserAccount "
                 "LEFT JOIN dbo.MFG_PartDetail c ON a.PartNo=c.PartNo "
                 "WHERE a.IsTransDone = '0' AND a.CloseReason='0' and c.FactoryCode ='1140'"
                 "and a.CreateTime <'%s'" % now_time)
        out_sql=("SELECT a.OutBillGuid,a.StkCode,a.PartNo,a.Qty,a.Barcode,b.UserName,a.CreateTime ,c.PartDesc "
                 "FROM  dbo.WMS_StkOutDet a LEFT JOIN dbo.SYS_User b ON a.CreateUserAccount = b.UserAccount "
                 "LEFT JOIN dbo.MFG_PartDetail c ON a.PartNo=c.PartNo"
                 " WHERE a.IsTransDone = '0' AND a.CloseReason='0' and c.FactoryCode ='1140' "
                 "and a.CreateTime <'%s'" % now_time)

        try:
            dbcfg.cursor1.execute(rct_sql)
            rct_data = dbcfg.cursor1.fetchall()
            if  rct_data:
                # ���rct_data��Ϊ��
                for rdata in rct_data:
                    self.master.l1.insert(END, rdata[7])
                    self.master.l2.insert(END, rdata[1])
                    self.master.l3.insert(END, rdata[2])
                    self.master.l4.insert(END, round(rdata[3],2))
                    self.master.l5.insert(END, rdata[4])
                    self.master.l6.insert(END, rdata[5])
                    self.master.l7.insert(END, rdata[6])
                    self.master.e1.insert(END, '����쳣')
        except:
            print("rct_sql ִ�д���")
        try:
            dbcfg.cursor1.execute(out_sql)
            out_data = dbcfg.cursor1.fetchall()
            if  out_data:
                # ���out_data��Ϊ��
                for odata in out_data:
                    self.master.l1.insert(END, odata[7])
                    self.master.l2.insert(END, odata[1])
                    self.master.l3.insert(END, odata[2])
                    self.master.l4.insert(END, round(odata[3],2))
                    self.master.l5.insert(END, odata[4])
                    self.master.l6.insert(END, odata[5])
                    self.master.l7.insert(END, odata[6])
                    self.master.e1.insert(END, '�����쳣')
        except:
            print("out_sql ִ�д���")
        try:
            dbcfg.cursor1.execute(cogi_sql)
            cogi_data =dbcfg.cursor1.fetchall()
            if cogi_data:
                # ���cogi_data��Ϊ��
                for cdata in cogi_data:
                    # self.master.l1.insert(END, cdata[0])
                    self.master.l2.insert(END, cdata[1])
                    self.master.l3.insert(END, cdata[2])
                    self.master.l4.insert(END, round(cdata[3],2))
                    self.master.l1.insert(END, cdata[5])
                    # self.l6 = cdata[0]
                    self.master.l7.insert(END, cdata[4])
                    self.master.e1.insert(END, 'COGI')
        except:
            print("cogi_sql ִ�д���")
        update = self.master.e1.update()
        self.master.l1.update()
        self.master.l2.update()
        self.master.l3.update()
        self.master.l4.update()
        self.master.l5.update()
        self.master.l6.update()
        self.master.l7.update()
    def display(self,inc):
        while 1:
            self.check_data()
            time.sleep(inc)
    def gui(self):
        self.master=Tk()
        self.master.title("�쳣������")
        Label(self.master,text='��������').grid(row=0,column=0)
        Label(self.master, text='��������').grid(row=0, column=1)
        Label(self.master, text='��λ').grid(row=0, column=2)
        Label(self.master, text='���Ϻ�').grid(row=0, column=3)
        Label(self.master, text='����').grid(row=0, column=4)
        Label(self.master, text='����').grid(row=0, column=5)
        Label(self.master, text='�û�').grid(row=0, column=6)
        Label(self.master, text='����ʱ��').grid(row=0, column=7)
        self.master.e1=Listbox(self.master,width=8,height='30')
        self.master.e1.grid(row=1,column=0,padx=5,pady=5)
        self.master.l1 = Listbox(self.master,height='30',width='36')
        self.master.l1.grid(row=1, column=1, )
        self.master.l2 = Listbox(self.master,height='30',width='8')
        self.master.l2.grid(row=1, column=2,)
        self.master.l3 = Listbox(self.master,height='30',width='9')
        self.master.l3.grid(row=1, column=3,)
        self.master.l4 = Listbox(self.master,height='30',width='5')
        self.master.l4.grid(row=1, column=4,)
        self.master.l5 = Listbox(self.master,height='30',width='15')
        self.master.l5.grid(row=1, column=5,)
        self.master.l6 = Listbox(self.master,height='30',width='6')
        self.master.l6.grid(row=1, column=6,)
        self.master.l7 = Listbox(self.master,height='30',width='25')
        self.master.l7.grid(row=1, column=7,)

if __name__=='__main__':
    p=EX_Monitor()
    p.gui()
    t = threading.Thread(target=p.display,args=(3600,))
    t.start()
    p.master.mainloop()
    dbcfg.cursor1.close()
    dbcfg.conn1.close()


