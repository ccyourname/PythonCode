#coding=gbk
#__author__ ="л��" 
# from  multiprocessing import Process
# import os
# def run_proc(name):
#     print("�ӽ��� %s (%s)" % (name,os.getpid()))
# if __name__=='__main__':
#     print("������ %s" % os.getpid())
#     p =Process(target=run_proc,args=('С',))
#     print("�ӽ�������������")
#     p.start()
#     p.join() #�ȴ����̽�����ִ����һ����
#     print("�ӽ��̽�������")

# from multiprocessing import Pool
# import os,time,random
# def long_time_task(name):
#     print("�ӽ��� %s(%s)" %(name,os.getpid()))
#     start = time.time()
#     time.sleep(random.random()*3)
#     end = time.time()
#     print("�ӽ���%s���� %0.2f ��" %(name,(end - start)))
#
# if __name__=='__main__':
#     print("������%s" % os.getpid())
#     p=Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print("�ȴ��ӽ�����ɡ���")
#     p.close()
#     p.join()
#     print("���н��̽�����")

from multiprocessing import Process , Queue
import  os,time,random
def write(q):
    print("д����%s(%s)" % (q,os.getpid()))
    for value in ['A','B','C']:
        print("д��%s to queue" % value)
        q.put(value)
        time.sleep(random.random())
def read(q):
    print("������%s(%s)" % (q,os.getpid()))
    while 1:
        value = q.get(True)
        print("��ȡ��%s ��queue" % value)
if __name__=="__main__":
    print("����������...")
    p=Queue()
    pw=Process(target=write,args=(p,))
    pr=Process(target=read,args=(p,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()

    print("���̽���")
