#coding=gbk
'''数据库连接'''
import pyodbc , time , threading
import decimal
#import sys
from tkinter import *
#链接数据库 常熟正式库
conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.226.35.103;DATABASE=IMES3;UID=imes3_user;PWD=yfpoimes31024')
#增加数据库游标 
cursor = conn.cursor()
#FHUB
conn2 = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.226.35.103;DATABASE=FHUB;UID=Fhub_user;PWD=fhubpassword')
cursor2 = conn2.cursor()
master = Tk()
master.title("前保排序漏车明细查询")
Label(master,text='SerialNO',font=("宋体",12,"bold")).grid(row=0,column=0)
Label(master,text='订单',font=("宋体",12,"bold")).grid(row=0,column=1)
Label(master,text='VIN',font=("宋体",12,"bold")).grid(row=0,column=2)
Label(master,text='配置',font=("宋体",12,"bold")).grid(row=0,column=3)
Label(master,text='PartFamily',font=("宋体",8,"bold")).grid(row=0,column=4)
Label(master,text='CARNO',font=("宋体",12,"bold")).grid(row=0,column=5)
Label(master,text='时间',font=("宋体",12,"bold")).grid(row=0,column=6)
e1 = Listbox(master,height=30,width=7,font=("宋体",12,"bold"))
e2 = Listbox(master,height=30,width=13,font=("宋体",12,"bold"))
e3 = Listbox(master,height=30,width=18,font=("宋体",12,"bold"))
e4 = Listbox(master,height=30,width=30,font=("宋体",12,"bold"))
e5 = Listbox(master,height=30,width=8,font=("宋体",12,"bold"))
e6 = Listbox(master,height=30,width=20,font=("宋体",12,"bold"))
e7 = Listbox(master,height=30,width=20,font=("宋体",12,"bold"))

e1.grid(row=2,column=0,sticky=E)
e2.grid(row=2,column=1)
e3.grid(row=2,column=2)
e4.grid(row=2,column=3)
e5.grid(row=2,column=4)
e6.grid(row=2,column=5)
e7.grid(row=2,column=6)

e11 = Listbox(master,height=3,width=7,bg='yellow',font=("宋体",12,"bold"))
e12 = Listbox(master,height=3,width=13,bg='yellow',font=("宋体",12,"bold"))
e13 = Listbox(master,height=3,width=18,bg='yellow',font=("宋体",12,"bold"))
e14 = Listbox(master,height=3,width=30,bg='yellow',font=("宋体",12,"bold"))
e15 = Listbox(master,height=3,width=8,bg='yellow',font=("宋体",12,"bold"))
e16 = Listbox(master,height=3,width=20,bg='yellow',font=("宋体",12,"bold"))
e17 = Listbox(master,height=3,width=20,bg='yellow',font=("宋体",12,"bold"))

e11.grid(row=1,column=0,sticky=E)
e12.grid(row=1,column=1,sticky=N)
e13.grid(row=1,column=2,sticky=N)
e14.grid(row=1,column=3,sticky=N)
e15.grid(row=1,column=4,sticky=N)
e16.grid(row=1,column=5,sticky=N)
e17.grid(row=1,column=6,sticky=N)

e21 = Listbox(master,height=4,width=7,bg='red',font=("宋体",12,"bold"))
e22 = Listbox(master,height=4,width=13,bg='red',font=("宋体",12,"bold"))
e23 = Listbox(master,height=4,width=18,bg='red',font=("宋体",12,"bold"))
e24 = Listbox(master,height=4,width=30,bg='red',font=("宋体",12,"bold"))
e25 = Listbox(master,height=4,width=8,bg='red',font=("宋体",12,"bold"))
e26 = Listbox(master,height=4,width=20,bg='red',font=("宋体",12,"bold"))
e27 = Listbox(master,height=4,width=20,bg='red',font=("宋体",12,"bold"))

e21.grid(row=3,column=0,sticky=S+E)
e22.grid(row=3,column=1,sticky=S)
e23.grid(row=3,column=2,sticky=S)
e24.grid(row=3,column=3,sticky=S)
e25.grid(row=3,column=4,sticky=S)
e26.grid(row=3,column=5,sticky=S)
e27.grid(row=3,column=6,sticky=S)


def openwindows():
        topwin.deiconify()#还原窗口
def closewindows():
        topwin.withdraw()#隐藏窗口
        #TopLevel关闭时清空数据
        tope1.delete(0,END)
        tope10.delete(0,END)
        tope11.delete(0, END)
        tope12.delete(0, END)
        tope13.delete(0, END)
        tope14.delete(0, END)
        tope15.delete(0, END)
        tope16.delete(0, END)
topwin=Toplevel(master,)
topwin.wm_attributes("-topmost",1)
topwin.title("排序接入信息监控")
topwin.protocol("WM_DELETE_WINDOW", closewindows)#窗口关闭触发事件
Label(topwin, text='流水号：').grid(row=0, column=0, sticky=W)
tope1 = Entry(topwin, width=8)
tope1.grid(row=0, column=0, sticky=E)

Label(topwin, text='ID').grid(row=1, column=0)
Label(topwin, text='流水号').grid(row=1, column=1)
Label(topwin, text='订单').grid(row=1, column=2)
Label(topwin, text='车号').grid(row=1, column=3)
Label(topwin, text='车流水号').grid(row=1, column=4)
Label(topwin, text='是否散件').grid(row=1, column=5)
Label(topwin, text='状态').grid(row=1, column=6)
tope10 = Listbox(topwin)
tope11 = Listbox(topwin,width=6)
tope12 = Listbox(topwin,width=12)
tope13 = Listbox(topwin,width=19 )
tope14 = Listbox(topwin, )
tope15 = Listbox(topwin,width=8 )
tope16 = Listbox(topwin,width=10)
tope10.grid(row=2, column=0)
tope11.grid(row=2, column=1)
tope12.grid(row=2, column=2)
tope13.grid(row=2, column=3)
tope14.grid(row=2, column=4)
tope15.grid(row=2, column=5)
tope16.grid(row=2, column=6)
#tope1.bind('<Return>', select)
#tope1.focus_set()
topwin.withdraw()#隐藏窗口
btn1 = Button(master,text='漏车查询',bg='yellow',font=("宋体",12,"bold"),command=openwindows).grid(row=4,column=3)
def select():
        tope10.delete(0, END)
        tope11.delete(0, END)
        tope12.delete(0, END)
        tope13.delete(0, END)
        tope14.delete(0, END)
        tope15.delete(0, END)
        tope16.delete(0, END)
        serno = tope1.get()
        cursor2.execute(
                "select    id ,ZCSN,ZORDNR,ZVIN ,ZVMCSN,ZSTATUS,IsTested  from  [FHUB].[dbo].[cjlr_tls_line]  where ZCSN = '%s' " % serno)
        getall = cursor2.fetchall()
        try:
                for tls in getall:
                        tp0 = (tope10.insert(END, tls[0]))
                        tp1 = (tope11.insert(END, tls[1]))
                        tp2 = (tope12.insert(END, tls[2]))
                        tp3 = (tope13.insert(END, tls[3]))
                        tp4 = (tope14.insert(END, tls[4]))
                        # tp5 = (tope15.insert(END, tls[5]))
                        # 判定是否散件
                        if tls[5] == 'TLS-CCR':
                                tp5 = (tope15.insert(END, "散件"))
                        elif tls[5] == 'TLS-JIS':
                                tp5 = (tope15.insert(END, "总成"))
                        else:
                                pass
                        # 判定状态
                        if tls[6] == 1:
                                tp6 = (tope16.insert(END, "已排序"))
                        elif tls[6] == 0:
                                tp6 = (tope16.insert(END, "未排序"))
                        else:
                                pass
                                # tp6 = (tope16.insert(END, tls[6]))
                topwin.update()

        except:
                print("select函数异常")
btn2 = Button(topwin, text='查询', command=select).grid(row=0, column=1,sticky=W)
def updatetls():
        sernoup = str(tope1.get())
        try:
                cursor2.execute("UPDATE [FHUB].[dbo].[cjlr_tls_line] SET IsTested = '0' where ZCSN ='%s' " % sernoup)
                conn2.commit()
        except:
                print("TLS 状态更新失败")
        select()
        #print("更新TLS-LINE")
btn3 = Button(topwin, text='再次发布',bg='red', command=updatetls).grid(row=0, column=6)

def gettls():
        e21.delete(0,END)
        e22.delete(0,END)
        e23.delete(0,END)
        e26.delete(0,END)
        e27.delete(0,END)
        sql="SELECT  ZCSN,ZORDNR,ZVIN,ZVM,ZVMCSN,handleTime FROM [FHUB].[dbo].[cjlr_tls_line] where IsTested=0"
        cursor2.execute(sql)
        tlsmsg=cursor2.fetchall()
        for tls in tlsmsg:
                a21=(e21.insert(END,tls[0]))
                a22=(e22.insert(END,tls[1]))
                a23=(e23.insert(END,tls[2]))
                #a24=(e24.insert(END,tls[0]))
                #a25=(e25.insert(END,tls[3]))
                a26=(e26.insert(END,tls[4]))
                a27=(e27.insert(END,tls[5]))
def display(inc): #界面显示
        #insert()   #调用函数更新DispPreAssembly数据
        while 1 :                
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e4.delete(0,END)
                e5.delete(0,END)
                e6.delete(0,END)
                e7.delete(0,END)
                e11.delete(0,END)
                e12.delete(0,END)
                e13.delete(0,END)
                e14.delete(0,END)
                e15.delete(0,END)
                e16.delete(0,END)
                e17.delete(0,END)        
                cursor.execute("SELECT   SerialNo = MAX(SerialNo) FROM  dbo.LGS_JISOrderInterim WHERE Category3 = 'fb' AND IsOrdered ='1' GROUP BY VehicleCode ORDER BY SerialNo DESC ") 
                getno=cursor.fetchall()
                for serialno in getno:
                        cursor.execute("SELECT a.CustOrderNo ,a.VinCode,b.Description ,a.PartFamily ,a.CarNo ,"
                                       "a.ExpectedArrivalTime ,a.SerialNo FROM  dbo.LGS_JISOrderInterim  a "
                                       " INNER JOIN dbo.LGS_CustStdOrdMstr b ON a.StdOrdCfg = b.StdOrdCfg	"
                                       " WHERE   a.Category3 = 'fb'  and a.carno !='00000000000000000000' "
                                       "AND a.IsOrdered ='1' AND a.SerialNo = '%d' " % serialno[0] )
                        gethist=cursor.fetchall()
                        for hist in gethist:
                                aa1=(e11.insert(0,hist[6]))
                                ab1=(e12.insert(0,hist[0]))
                                ac1=(e13.insert(0,hist[1]))
                                ad1=(e14.insert(0,hist[2]))
                                ae1=(e15.insert(0,hist[3]))
                                af1=(e16.insert(0,hist[4]))
                                ag1=(e17.insert(0,hist[5]))
     
                cursor.execute("SELECT a.CustOrderNo ,a.VinCode,b.Description ,a.PartFamily ,a.CarNo ,a.ExpectedArrivalTime ,a.SerialNo FROM  dbo.LGS_JISOrderInterim  a  INNER JOIN dbo.LGS_CustStdOrdMstr b ON a.StdOrdCfg = b.StdOrdCfg	WHERE a.IsOrdered = '0' AND a.Category3 = 'fb' order by serialno")
                rowall = cursor.fetchall()      

                for rec in rowall:
            
                        aa=(e1.insert(END,rec[6]))
                        ab=(e2.insert(END,rec[0]))
                        ac=(e3.insert(END,rec[1]))
                        ad=(e4.insert(END,rec[2]))
                        ae=(e5.insert(END,rec[3]))
                        af=(e6.insert(END,rec[4]))
                        ag=(e7.insert(END,rec[5]))
                gettls()
                e1.update()
                e2.update()
                e3.update()
                e4.update()
                e5.update()
                e6.update()
                e7.update()
                e11.update()
                e12.update()
                e13.update()
                e14.update()
                e15.update()
                e16.update()
                e17.update()
                e21.update()
                e22.update()
                e23.update()
                e26.update()
                e27.update()
                time.sleep(inc)
#tkinter 窗口太卡，调用thread处理
t = threading.Thread(target=display,args=(120,))
t.start()  #启动thread
mainloop()
cursor2.close()
conn2.close()
cursor.close()
conn.close()



