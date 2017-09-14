#coding=gbk
#__author__ ="谢飞"
from socket import *
from time import  ctime

host =""
port=21567 #端口
bufsiz=1024 #缓存
server_id=(host,port)
tcp_server=socket(AF_INET,SOCK_STREAM)
tcp_server.bind(server_id)
tcp_server.listen(5)
while 1:
    print("连接中。。。")
    tcp_server,addr =tcp_server.accept()
    print("链接到。。",addr)
    while 1:
        data = tcp_server.recv(bufsiz).decode()
        if not data:
            break
        # tcp_server.send('[%s]%s'%(ctime(),data))
        tcp_server.send('[%s]%s' % (ctime(), data.decode()).encode())
    tcp_server.close()
    print("退出时间戳")
tcp_server.close()
print("退出服务监控")