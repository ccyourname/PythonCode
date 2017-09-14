#coding=gbk
#__author__ ="谢飞" 
from socket import *
host='localhost'
port=21567
bufsiz=1024
server_id=(host,port)
tcp_customer=socket(AF_INET,SOCK_STREAM)
tcp_customer.connect(server_id)
while 1:
    data = input('请输入：')
    if not data:
        break
    tcp_customer.send(data.encode())

    data=tcp_customer.recv(bufsiz)
    if not data:
        break
    print(data)
tcp_customer.close()
