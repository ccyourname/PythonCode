#coding=gbk
#__author__ ="л��"
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
# ��ȡ�����ļ��еĽ�������ϵͳ·������2�������������������ļ����޸�
# ProList = []
# ����һ���б�
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
    # _svc_name_ ="CheckISvc"#������
    # _svc_display_name_="Check Ihand Service" #������windowsϵͳ����ʾ������
    # _svc_description_="����������ڼ��Ihand update�����Ƿ���������"#���������
    def main(self):
        # poc = psutil.process_iter()
        # ����״̬
        # UNKNOWN = 0
        # STOPPED = 1
        # START_PENDING = 2
        # STOP_PENDING = 3
        # RUNNING = 4
        # �������״̬
        result = win32serviceutil.QueryServiceStatus(ServiceName)[1]
        #������ǰ״̬
        # for process in poc:
        #
        #     ProList.append(str(process.name()))
        #     # print(ProList)
        # # ����������������еĽ�������ӵ��б�

        # if ProcessName in ProList:
        #  # �жϽ������Ƿ����б��У������True��������صķ������� ����״̬��
        #     # ��ӡ������������
        #     # print("��������������...")
        #     pass
        # �жϵ�ǰ������ʲô״̬
        if result == 4 or result == 2:
            #��ӡ������������
            print("��������������...")

        else:
            # �������״̬��������������������������صķ�����ˣ�����log�ļ��¼�¼��־
            # ��־�ļ�������������Ϊ�ļ���

            # f = open('.\\log\\' + time.strftime("%Y%m%d", time.localtime()) + '-exception.txt', 'w')
            with open('buglog.txt', 'a') as f:
                # print('Server is not running,Begining to Restart Server...')
                # ��ӡ����״̬
                f.write('\n' + '����û������,��ʼ��������...' + '\n')
                f.write(time.strftime('%Y-%m-%d %H:%M:%S --%A--%c', time.localtime()) + '\n')
            # д��ʱ��ͷ���״̬����־�ļ���
            try:
                print("��ͼ����")
                # os.startfile(ProgramPath) #��������
                
                win32serviceutil.StartService(ServiceName)#��������
                print("�����ɹ�")
                print("��������������...")
                # ���÷�������
                with open('buglog.txt', 'a') as f:
                    f.write('��������ɹ�...' + '\n')
                    f.write(time.strftime('%Y-%m-%d %H:%M:%S --%A--%c', time.localtime()))
            except :
                with open('buglog.txt', 'a') as f:
                    f.write('��������ʧ�ܣ�.' + '\n')
                    f.write(time.strftime('%Y-%m-%d %H:%M:%S --%A--%c', time.localtime()))
                print("����ʧ��")

            # f.close()
        # �ر��ļ�
        # print('Restart Server Success...')
        # print(time.strftime('%Y-%m-%d %H:%M:%S --%A--%c', time.localtime()))
        # del ProList[:]

if __name__ == "__main__":
    c=CheckSrv()
    while True:
        c.main()
        time.sleep(60)
        # ÿ��60����ýű����·����Ƿ��������������������������������������ӡ��������