#coding=gbk
#__author__ ="谢飞" 
import  pyodbc
#链接数据库 常熟正式库3.0
conn1 = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.226.35.103;DATABASE=IMES3;UID=imes3_user;PWD=yfpoimes31024')
#增加数据库游标
cursor1 = conn1.cursor()
#链接数据库 安亭正式库
conn2 = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.250.16.88;DATABASE=IMES3;UID=imes3_user;PWD=piwoiefjoifj')
#增加数据库游标
cursor2 = conn2.cursor()
# #链接数据库 常熟正式库2.0
conn3 = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.226.35.103;DATABASE=IMES;UID=IBAR_USER;PWD=yfpoibar')
#增加数据库游标
cursor3 = conn3.cursor()
#链接DEVComm数据库 常熟正式库3.0
conn4 = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.226.35.103;DATABASE=DevComm;UID=device_user;PWD=yfpodevice_user')
#增加数据库游标
cursor4 = conn4.cursor()

if __name__=='__main__':
    cursor1.close()
    cursor2.close()
    cursor3.close()
    cursor4.close()
    conn1.close()
    conn2.close()
    conn3.close()
    conn4.close()