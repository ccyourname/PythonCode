#coding=gbk
'''数据库连接'''
import pyodbc , time , threading
#import sys
from tkinter import *

#链接数据库 常熟正式库
conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.226.35.103;DATABASE=IMES3;UID=imes3_user;PWD=yfpoimes31024')
#增加数据库游标 
cursor = conn.cursor()

#链接DevComm库
conn2 = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.226.35.103;DATABASE=DevComm;UID=device_user;PWD=yfpodevice_user')
cursor2 = conn2.cursor()
'''
#读取SQL语句
cursor.execute("select * from  dbo.LGS_JISOrderDet WHERE IsShipped = '0' and isjump !='1' and briefcustpartno= 'l550crb' order by id")
rowall = cursor.fetchall()
'''
def jumpvin():
     vin=e3.get(e3.curselection())
     if vin is not None:
          try:
               cursor.execute("update dbo.LGS_DispPreAssembly SET Status = '1',Finished = '9' WHERE Status = '0' AND id = '%s'" % vin)
               conn.commit()
               output()
          except:
               print("跳过一车执行异常！")

master = Tk()
master.title("L550后保生产看板")
#c = Canvas(master,bg="blue")
master.wm_attributes("-topmost",1)#窗口前置
master.state("zoomed")#窗口最大化
Label(master,text='VIN',font=("宋体",24,"bold")).grid(row=0,column=1)
Label(master,text='配置',font=("宋体",24,"bold")).grid(row=0,column=2,sticky=W)
Label(master,text='标记',font=("宋体",24,"bold")).grid(row=0,column=0)
Label(master,text='条码',font=("宋体",24,"bold")).grid(row=0,column=3)
e1 = Listbox(master,height=14,width=17,font=("宋体",32,"bold"))
e2 = Listbox(master,height=14,width=40,font=("宋体",32,"bold"))
e3 = Listbox(master,height=14,width=6,font=("宋体",32,"bold"))
#e4 = Listbox(master,height=15,width=15,font=("宋体",32,"bold"))
btn1 = Button(master,text='跳过一车',bg='red',font=("宋体",20,"bold"),command = jumpvin)
btn1.grid(row=2,column=0)
e1.grid(row=1,column=1,sticky=E)
e2.grid(row=1,column=2)
e3.grid(row=1,column=0)
#e4.grid(row=1,column=3)
def insert(): #插入表
     cursor.execute("SELECT id ,CustOrderNo ,SeqOrderNo ,PartNo ,StdOrdCfg ,CustPartNo ,ProduceCategory , Category3 ,PartFamily ,IsCCR , IsManual ,VinCode ,SerialNo ,CustCode , BarCode ,JisOrderDetId ,Status ,Finished , CreateTime FROM  dbo.LGS_PreAssembly WHERE id >='179631' AND PartFamily = 'L550CRB' AND Status = '1' AND Finished = '1' AND id NOT IN (SELECT PreAssemblyID FROM  dbo.LGS_DispPreAssembly )")
     getdate = cursor.fetchall()
     for cc in getdate:
          #Pyodbc数据插入
          sql=("INSERT INTO dbo.LGS_DispPreAssembly( CustOrderNo ,SeqOrderNo ,PartNo ,StdOrdCfg ,CustPartNo ,ProduceCategory , Category3 ,PartFamily ,IsCCR , IsManual ,VinCode ,SerialNo ,CustCode , BarCode ,JisOrderDetId ,Status ,Finished ,CreateTime ,PreAssemblyID) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" )
          parama=(cc[1],cc[2],cc[3],cc[4],cc[5],cc[6],cc[7],cc[8],cc[9],cc[10],cc[11],cc[12],cc[13],cc[14],cc[15],0,0,cc[18],cc[0])
          cursor.execute(sql,parama)
          #提交修改
          conn.commit()          
     '''
     cursor.execute("SELECT TOP 1 PreAssemblyID FROM dbo.LGS_DispPreAssembly ORDER BY PreAssemblyID DESC")
     preid = cursor.fetchone()     
     cursor.execute("SELECT id ,CustOrderNo ,SeqOrderNo ,PartNo ,StdOrdCfg ,CustPartNo ,ProduceCategory , Category3 ,PartFamily ,IsCCR , IsManual ,VinCode ,SerialNo ,CustCode , BarCode ,JisOrderDetId ,Status ,Finished , CreateTime FROM dbo.LGS_PreAssembly WHERE Status = '1' and Finished='1' AND PartFamily='L550cRB' AND( ID > %d )" % preid[0])
     getall= cursor.fetchall()       
     for cc in getall:
          #Pyodbc数据插入
          sql=("INSERT INTO dbo.LGS_DispPreAssembly( CustOrderNo ,SeqOrderNo ,PartNo ,StdOrdCfg ,CustPartNo ,ProduceCategory , Category3 ,PartFamily ,IsCCR , IsManual ,VinCode ,SerialNo ,CustCode , BarCode ,JisOrderDetId ,Status ,Finished ,CreateTime ,PreAssemblyID) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" )         
          parama=(cc[1],cc[2],cc[3],cc[4],cc[5],cc[6],cc[7],cc[8],cc[9],cc[10],cc[11],cc[12],cc[13],cc[14],cc[15],0,0,cc[18],cc[0])
          cursor.execute(sql,parama)
          #提交修改
          conn.commit()
          #print(cc)
     '''
def output():#输出显示结果
     e1.delete(0,END)
     e2.delete(0,END)
     e3.delete(0,END)
     cursor.execute("SELECT a.id,a.IsManual,a.VinCode,a.StdOrdCfg,b.Description FROM   dbo.LGS_DispPreAssembly  AS a WITH (NOLOCK)  INNER JOIN dbo.LGS_CustStdOrdMstr AS b WITH (NOLOCK)  ON a.StdOrdCfg = b.StdOrdCfg WHERE a.Status = '0' and a.Finished='0' order by RIGHT(VinCode,6) ")
     rowall = cursor.fetchall()                
     for rec in rowall:
          aa=(e1.insert(END,rec[2]))
          #e1.itemconfig(1, {'bg': 'blue'})
          ab=(e2.insert(END,rec[4]))
          ac=(e3.insert(END,rec[0]))
     '''
     for i in range (len(rowall)):
         e1.itemconfig(0, fg='blue')
     '''
     #第0行数据标颜色，黑色背景，黄色字体
     e1.itemconfig(0,fg='yellow' ,bg='black')
     e2.itemconfig(0,fg='yellow' ,bg='black')
     e3.itemconfig(0,fg='yellow' ,bg='black')
     e1.update()
     e2.update()
     e3.update()
def updateDPA(): #更新表
     cursor.execute("SELECT barcode FROM   dbo.LGS_DispPreAssembly WHERE Status = '0' ")
     barcode = cursor.fetchall()
     #barcode.sort(key = vin)
     #n=0     
     for bcode in barcode:          
          cursor2.execute("SELECT barcode FROM [DevComm].[dbo].[404_DEV2MES_DATA]  WHERE Barcode = '%s' AND ItemName = 'protect_barcode'" % bcode[0])
          result = cursor2.fetchone()
          #n=n+1
          if result is not None :               
               cursor.execute("update dbo.LGS_DispPreAssembly SET Status = '1' WHERE Status = '0' AND BarCode = '%s'" % result[0])
               conn.commit()
          else:
               #print('update else')
               pass
     #conn.commit()     
def display(inc): #界面显示，循环调用
     while TRUE:
          #insert()
          updateDPA()
          #time.sleep(3)
          #insert()   #调用函数更新DispPreAssembly数据
          '''
          cursor.execute("SELECT a.id,a.IsManual,a.VinCode,a.StdOrdCfg,b.Description FROM   dbo.LGS_DispPreAssembly AS a INNER JOIN dbo.LGS_CustStdOrdMstr AS b ON a.StdOrdCfg = b.StdOrdCfg WHERE a.Status = '0' and a.Finished='0' order by id ")
          rowall = cursor.fetchall()                
          for rec in rowall:
               aa=(e1.insert(END,rec[2]))
               ab=(e2.insert(END,rec[4]))          
          e1.update()
          e2.update()  
          '''
          output()
          time.sleep(inc)
#tkinter 窗口太卡，调用thread处理
t = threading.Thread(target=display,args=(10,))
t.start()  #启动thread
#display(10)

mainloop()
cursor2.close()
conn2.close()
cursor.close()
conn.close()
