#coding=gbk
#__author__ ="л��"
from socket import *
from time import  ctime

host =""
port=21567 #�˿�
bufsiz=1024 #����
server_id=(host,port)
tcp_server=socket(AF_INET,SOCK_STREAM)
tcp_server.bind(server_id)
tcp_server.listen(5)
while 1:
    print("�����С�����")
    tcp_server,addr =tcp_server.accept()
    print("���ӵ�����",addr)
    while 1:
        data = tcp_server.recv(bufsiz).decode()
        if not data:
            break
        # tcp_server.send('[%s]%s'%(ctime(),data))
        tcp_server.send('[%s]%s' % (ctime(), data.decode()).encode())
    tcp_server.close()
    print("�˳�ʱ���")
tcp_server.close()
print("�˳�������")