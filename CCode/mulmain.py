#coding=gbk
#__author__ ="л��" 
import random,time,queue
from multiprocessing.managers import BaseManager
#�����Ͷ���
task_queue=queue.Queue()
#������ն���
result_queue=queue.Queue()
class QueueManager(BaseManager):
    pass
#��Queueע���������ϣ�callable��������Queue����
QueueManager.register('get_task',callable=lambda :task_queue)
QueueManager.register('get_result',callable=lambda :result_queue)
#�󶨶˿�5000��������֤�롮abc��
manager = QueueManager(address=('',5000),authkey=b'abc')
#����Queue
manager.start()

#���ͨ��������ʵ�Queue����
task=manager.get_task()
result=manager.get_result()
#��������
for i in range(10):
    n=random.randint(0,10000)
    print("����task %d" % n)
    task.put(n)
#��result���ж�ȡ����
print("��ͼ��ȡresult..")
for i in range(10):
    r=result.get(timeout=10)
    print("result���У�%s" %r)

#�رն���
manager.shutdown()
print("master exit")
