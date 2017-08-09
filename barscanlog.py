#coding=gbk
#__author__ ="谢飞"
import  pyodbc
import time
import dbcfg
from tkinter import *
#import  tkinter as tk
from tkinter import ttk
import  threading

# #链接数据库 常熟正式库3.0
# conn1 = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.226.35.103;DATABASE=IMES3;UID=imes3_user;PWD=yfpoimes31024')
# #增加数据库游标
# cursor1 = conn1.cursor()
#
# # #链接数据库 常熟正式库2.0
# conn3 = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.226.35.103;DATABASE=IMES;UID=IBAR_USER;PWD=yfpoibar')
# #增加数据库游标
# cursor3 = conn3.cursor()
#
# #链接数据库 安亭正式库
# conn2 = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.250.16.88;DATABASE=IMES3;UID=imes3_user;PWD=piwoiefjoifj')
# #增加数据库游标
# cursor2 = conn2.cursor()
getbar = ''
class barscan:
    def checklog(self):
        self.scanwin.e2.delete(0,END)
        self.barcode = self.scanwin.e1.get()
        self.scanwin.e1.delete(0,END)
        self.getvin = self.scanwin.evin.get()

        if self.getvin ==''  and self.barcode !='':
            self.barcode=self.barcode
        elif self.getvin !='' and self.barcode =='' :
            self.barcode=self.getbar[0]
        dbcfg.cursor2.execute("SELECT a.Barcode , a.NewPartNo,c.PartDesc,a.NewQualityStatus,b.ScanSiteName,"
                              "a.ActionCode ,a.createtime FROM dbo.MFG_BarcodeScanLog a "
                              "INNER JOIN dbo.MFG_ScanSite b ON a.ScanSiteCode =b.ScanSiteCode "
                              "LEFT JOIN dbo.MFG_PartDetail c ON a.NewPartNo =c.PartNo  "
                              "WHERE a.Barcode = '%s' and a.ScanSiteCode != 'StdStockTaking' "
                              "and actioncode !='packagebox' and c.FactoryCode='2010' "
                              "order by a.id" % self.barcode)
        self.getbar2=dbcfg.cursor2.fetchall()
        for bar2 in self.getbar2:
            if bar2[3]=='1':
                bar2[3]='合格'
            elif bar2[3]=='2':
                bar2[3]='冻结'
            elif bar2[3]=='3':
                bar2[3]='报废'
            else:
                bar2[3] = '其他'

            try:
                bar2[-1]=bar2[-1].strftime("%Y-%m-%d %H:%M:%S")
            except:
                print("时间格式修改失败")
            aa = (self.scanwin.e2.insert(END, bar2))
        try:
            dbcfg.cursor3.execute("SELECT  a.barlog_code,a.barlog_fromsite,b.Desc1,a.barlog_result"
                                  " FROM dbo.barlog_det a LEFT JOIN idaq.Item b ON a.barlog_part=b.Code "
                                  "WHERE a.barlog_code = '%s' AND a.barlog_fromsite!='料箱操作扫描'"
                                  "and a.barlog_fromsite!='转储操作扫描' order by barlog_date" % self.barcode)
            getbar3 = dbcfg.cursor3.fetchall()
        except:
            print("MES2扫描记录查询失败")
        if getbar3:
            try:
                for i in getbar3:
                    i[-1]=i[-1].strftime("%Y-%m-%d %H:%M:%S")
                    self.scanwin.e2.insert(END,i)
            except:
                pass
        else:
            dbcfg.cursor1.execute("SELECT a.Barcode , a.NewPartNo,c.PartDesc,a.NewQualityStatus,b.ScanSiteName,a.ActionCode ,a.createtime FROM dbo.MFG_BarcodeScanLog a INNER JOIN dbo.MFG_ScanSite b ON a.ScanSiteCode =b.ScanSiteCode LEFT JOIN dbo.MFG_PartDetail c ON a.NewPartNo =c.PartNo  WHERE a.Barcode = '%s' and a.ScanSiteCode != 'StdStockTaking' and c.FactoryCode='1140' order by a.id" % self.barcode)
            getbar1 = dbcfg.cursor1.fetchall()
            for bar1 in getbar1:
                if bar1[3] == '1':
                    bar1[3] = '合格'
                elif bar1[3] == '2':
                    bar1[3] = '冻结'
                elif bar1[3] == '3':
                    bar1[3] = '报废'
                else:
                    bar1[3] = '其他'
                try:
                    bar1[-1] = bar1[-1].strftime("%Y-%m-%d %H:%M:%S")
                except:
                    print("时间字段修改失败")
                ab = (self.scanwin.e2.insert(END, bar1))
    def checklogET(self,event):
        self.checklog()
    def checkvin(self):
        vin=self.scanwin.evin.get()
        if self.cboxchose.get()=='前保':
            cg3='FB'
        elif self.cboxchose.get()=='后保':
            cg3='RB'
        elif self.cboxchose.get()=='扰流板':
            cg3='RLB3'
        else:
            cg3='wm3'
        dbcfg.cursor1.execute("SELECT ProductBarcode FROM   dbo.LGS_JISOrderDet "
                              "WHERE VinCode LIKE '%s' AND Category3 ='%s'" %("%"+vin,cg3))
        # global getbar
        self.getbar=dbcfg.cursor1.fetchone()
        if self.getbar :
            print('3.0查询成功，不再查询2.0!')
        else:
            cg3=self.cboxchose.get()
            dbcfg.cursor3.execute("SELECT  a.bar_code FROM  dbo.bar_mstr a "
                                  "LEFT JOIN dbo.barindet_det b ON a.bar_part =b.barindet_part "
                                  "WHERE a.bar_cust_gano LIKE '%s' AND b.barindet_custloc LIKE '%s'"
                                  % ("%" + vin, "%" + cg3 + "%"))
            self.getbar = dbcfg.cursor3.fetchone()
    #print(getbar)
        self.checklog()
    #print(ct3)
    def gui(self):
        self.scanwin = Tk()
        self.scanwin.title('条码扫描记录查询')
        Label(self.scanwin,text='条码：').grid(row=0,column=0,sticky='W')
        Label(self.scanwin,text='VIN：').grid(row=1,column=0,sticky='W')
        #单元格 位置必须分离
        self.scanwin.e1=Entry(self.scanwin,width=18)
        self.scanwin.e1.grid(row=0,column=1,sticky='W')
        self.scanwin.evin=Entry(self.scanwin,width=18)
        self.scanwin.evin.grid(row=1,column=1,sticky='W')
        self.scanwin.e2=Listbox(self.scanwin,width=120,height=30)
        self.scanwin.e2.grid(row=2,column=0,columnspan=9,sticky='W')
        self.scanwin.btn1 = Button(self.scanwin,text='条码查询',command=self.checklog).grid(row=0,column=3,sticky='W')
        self.scanwin.btn2 = Button(self.scanwin,text='VIN查询',command=self.checkvin).grid(row=1,column=3,sticky='W')

        #创建下拉菜单
        self.cbox=StringVar()
        self.cboxchose=ttk.Combobox(self.scanwin,width='6',textvariable=self.cbox,state='readonly')#设定菜单框
        self.cboxchose.grid(row=1,column=2)#标记位置
        self.cboxchose['values']=('前保','后保','扰流板','尾门')
        self.cboxchose.current(0)#默认显示第0字段
        #按钮事件绑定
        self.scanwin.e1.bind('<Return>',self.checklogET)
        self.scanwin.e1.focus_set()

if __name__=="__main__":
    #tkinter 窗口太卡，调用thread处理
    barscan=barscan()
    barscan.gui()
    barscan.scanwin.mainloop()
    # t = threading.Thread(target=barscan.gui)
    # t.start()  #启动thread
    # mainloop()
    dbcfg.cursor1.close()
    dbcfg.cursor2.close()
    dbcfg.cursor3.close()
    dbcfg.conn1.close()
    dbcfg.conn2.close()
    dbcfg.conn3.close()
