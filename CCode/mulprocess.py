#coding=gbk
#__author__ ="谢飞" 
# from  multiprocessing import Process
# import os
# def run_proc(name):
#     print("子进程 %s (%s)" % (name,os.getpid()))
# if __name__=='__main__':
#     print("主进程 %s" % os.getpid())
#     p =Process(target=run_proc,args=('小',))
#     print("子进程启动。。。")
#     p.start()
#     p.join() #等待进程结束后执行下一步骤
#     print("子进程结束。。")

# from multiprocessing import Pool
# import os,time,random
# def long_time_task(name):
#     print("子进程 %s(%s)" %(name,os.getpid()))
#     start = time.time()
#     time.sleep(random.random()*3)
#     end = time.time()
#     print("子进程%s运行 %0.2f 秒" %(name,(end - start)))
#
# if __name__=='__main__':
#     print("主进程%s" % os.getpid())
#     p=Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print("等待子进程完成。。")
#     p.close()
#     p.join()
#     print("所有进程结束！")

from multiprocessing import Process , Queue
import  os,time,random
def write(q):
    print("写进程%s(%s)" % (q,os.getpid()))
    for value in ['A','B','C']:
        print("写入%s to queue" % value)
        q.put(value)
        time.sleep(random.random())
def read(q):
    print("读进程%s(%s)" % (q,os.getpid()))
    while 1:
        value = q.get(True)
        print("读取到%s 从queue" % value)
if __name__=="__main__":
    print("主进程启动...")
    p=Queue()
    pw=Process(target=write,args=(p,))
    pr=Process(target=read,args=(p,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()

    print("进程结束")
