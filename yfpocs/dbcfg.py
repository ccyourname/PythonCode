#coding=gbk
#__author__ ="л��" 
import  pyodbc
#�������ݿ� ������ʽ��3.0
conn1 = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.226.35.103;DATABASE=IMES3;UID=imes3_user;PWD=yfpoimes31024')
#�������ݿ��α�
cursor1 = conn1.cursor()
#�������ݿ� ��ͤ��ʽ��
conn2 = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.250.16.88;DATABASE=IMES3;UID=imes3_user;PWD=piwoiefjoifj')
#�������ݿ��α�
cursor2 = conn2.cursor()
# #�������ݿ� ������ʽ��2.0
conn3 = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.226.35.103;DATABASE=IMES;UID=IBAR_USER;PWD=yfpoibar')
#�������ݿ��α�
cursor3 = conn3.cursor()
#����DEVComm���ݿ� ������ʽ��3.0
conn4 = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.226.35.103;DATABASE=DevComm;UID=device_user;PWD=yfpodevice_user')
#�������ݿ��α�
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