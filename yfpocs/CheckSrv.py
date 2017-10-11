#coding=gbk
#__author__ ="谢飞"
# -*- encoding: utf-8 -*-
import logging
# import wmi
import os
import time
from configparser import  ConfigParser
from win32com.client import GetObject
import psutil
import win32serviceutil
CONFIGFILE = 'config.ini'
config = ConfigParser()
config.read(CONFIGFILE)
ProgramPath = config.get('MonitorProgramPath', 'ProgramPath')
ProcessName = config.get('MonitorProcessName', 'ProcessName')
# 读取配置文件中的进程名和系统路径，这2个参数都可以在配置文件中修改
# ProList = []
# 定义一个列表
# c = wmi.WMI()
# wmi=GetObject('winmgmts:/root/cimv2')
# wmi=GetObject('winmgmts:')
# # poc = wmi.ExecQuery('select * form Win32.Process')
# poc= wmi.InstancesOf('Win32.Process')
# p=psutil.Process()
ProList = []
class CheckSrv:
    # def __init__(self):
    #     self.scm=win32service.OpenSCManager(None,None,win32service.SC_MANAGER_ALL_ACCESS)
    def main(self):
        poc = psutil.process_iter()
        for process in poc:
            ProList.append(str(process.name()))
            # print(ProList)
        # 把所有任务管理器中的进程名添加到列表

        if ProcessName in ProList:
         # 判断进程名是否在列表中，如果是True，则所监控的服务正在 运行状态，
            # 打印服务正常运行
            # print("服务正常运行中...")
            pass

        else:
            # 如果进程名不在列表中，即监控的服务挂了，则在log文件下记录日志
            # 日志文件名是以年月日为文件名

            # f = open('.\\log\\' + time.strftime("%Y%m%d", time.localtime()) + '-exception.txt', 'w')
            with open('buglog.txt', 'a') as f:
                # print('Server is not running,Begining to Restart Server...')
                # 打印服务状态
                f.write('\n' + '服务没有启动,开始重启服务...' + '\n')
                f.write(time.strftime('%Y-%m-%d %H:%M:%S --%A--%c', time.localtime()) + '\n')
            # 写入时间和服务状态到日志文件中
            try:
                print("试图重启")
                # os.startfile(ProgramPath) #启动服务
                win32serviceutil.StartService('YFPO.MES.iHnadUpdateServer')
                # win32serviceutil.StartService('cphs')
                print("重启成功")
                print("服务正常工作中...")
                # 调用服务重启
                with open('buglog.txt', 'a') as f:
                    f.write('重启服务成功...' + '\n')
                    f.write(time.strftime('%Y-%m-%d %H:%M:%S --%A--%c', time.localtime()))
            except :
                with open('buglog.txt', 'a') as f:
                    f.write('服务重启失败！.' + '\n')
                    f.write(time.strftime('%Y-%m-%d %H:%M:%S --%A--%c', time.localtime()))
                print("重启失败")

            # f.close()
        # 关闭文件
        # print('Restart Server Success...')
        # print(time.strftime('%Y-%m-%d %H:%M:%S --%A--%c', time.localtime()))
        del ProList[:]


# 清空列表，否则列表会不停的添加进程名，会占用系统资源

if __name__ == "__main__":
    c=CheckSrv()
    while True:
        c.main()
        time.sleep(60)
        # 每隔10秒调用脚本看下服务是否正常，如果不正常则重启服务，如果正常，则打印服务正常