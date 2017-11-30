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
# ProgramPath = config.get('MonitorProgramPath', 'ProgramPath')
# ProcessName = config.get('MonitorProcessName', 'ProcessName')
ServiceName = config.get('MonitorServiceName','ServiceName')
# 读取配置文件中的进程名和系统路径，这2个参数都可以在配置文件中修改
# ProList = []
# 定义一个列表
# c = wmi.WMI()
# wmi=GetObject('winmgmts:/root/cimv2')
# wmi=GetObject('winmgmts:')
# # poc = wmi.ExecQuery('select * form Win32.Process')
# poc= wmi.InstancesOf('Win32.Process')
# p=psutil.Process()
# ProList = []
class CheckSrv:
    # def __init__(self):
    #     self.scm=win32service.OpenSCManager(None,None,win32service.SC_MANAGER_ALL_ACCESS)
    # _svc_name_ ="CheckISvc"#服务名
    # _svc_display_name_="Check Ihand Service" #服务在windows系统中显示的名称
    # _svc_description_="这个服务用于监控Ihand update服务是否正常启动"#服务的描述
    def main(self):
        # poc = psutil.process_iter()
        # 服务状态
        # UNKNOWN = 0
        # STOPPED = 1
        # START_PENDING = 2
        # STOP_PENDING = 3
        # RUNNING = 4
        # 检查服务的状态
        result = win32serviceutil.QueryServiceStatus(ServiceName)[1]
        #检测服务当前状态
        # for process in poc:
        #
        #     ProList.append(str(process.name()))
        #     # print(ProList)
        # # 把所有任务管理器中的进程名添加到列表

        # if ProcessName in ProList:
        #  # 判断进程名是否在列表中，如果是True，则所监控的服务正在 运行状态，
        #     # 打印服务正常运行
        #     # print("服务正常运行中...")
        #     pass
        # 判断当前服务处于什么状态
        if result == 4 or result == 2:
            #打印服务正常运行
            print("服务正常运行中...")

        else:
            # 如果服务状态不是已启动或正在启动，即监控的服务挂了，则在log文件下记录日志
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
                
                win32serviceutil.StartService(ServiceName)#启动服务
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
        # del ProList[:]

if __name__ == "__main__":
    c=CheckSrv()
    while True:
        c.main()
        time.sleep(60)
        # 每隔60秒调用脚本看下服务是否正常，如果不正常则重启服务，如果正常，则打印服务正常