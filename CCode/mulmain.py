#coding=gbk
#__author__ ="谢飞" 
import random,time,queue
from multiprocessing.managers import BaseManager
#任务发送队列
task_queue=queue.Queue()
#任务接收队列
result_queue=queue.Queue()
class QueueManager(BaseManager):
    pass
#把Queue注册套网络上，callable参数关联Queue对象
QueueManager.register('get_task',callable=lambda :task_queue)
QueueManager.register('get_result',callable=lambda :result_queue)
#绑定端口5000，设置验证码‘abc’
manager = QueueManager(address=('',5000),authkey=b'abc')
#启动Queue
manager.start()

#获得通过网络访问的Queue对象
task=manager.get_task()
result=manager.get_result()
#放置任务
for i in range(10):
    n=random.randint(0,10000)
    print("放置task %d" % n)
    task.put(n)
#从result队列读取数据
print("试图读取result..")
for i in range(10):
    r=result.get(timeout=10)
    print("result队列：%s" %r)

#关闭队列
manager.shutdown()
print("master exit")
