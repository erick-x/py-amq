#!/usr/bin/python
#coding:utf-8

from __init__ import *
import os
import signal
import time
def start():

    #加载配置项
    loadConf()

    # 注册所有线程方法
    registerInit()
    mythread = ThreadManager()
    mythread.start()
    while True:
        time.sleep(0.01)

def stop():
    mythread = ThreadManager()
    mythread.exit()

    parentList = os.popen("ps -ef|grep monitor.py|grep -v grep|awk '{print $2}'").readlines()
    for pid in parentList:
        print pid
        os.kill(int(pid), signal.SIGTERM)

#读取数据库配置文件
def loadDBConf():

    #加载路径
    xmlpath = os.getcwdu()+"\Sysconf\DBMSConf.xml"
    list =["m_iMajorVersion", "m_iMinVersion", "m_szDBMSName", "m_szDBMSConnectionInfo", "m_szDBMSCurDatabaseName", "m_szDBMSUser", "m_szDBMSPassword"]

    allchild = operationXML(xmlpath, "DBMSInfo", list)
    print allchild

#读取消息队列配置文件
def loadAMQConf():

    #加载路径
    xmlpath = os.getcwdu()+"\Sysconf\AMQConf.xml"
    operationXML(xmlpath, "employee", ["name", "sex", "age"])

    for node in xml.allchild:
        print "m_szDBMSName ",node['m_szDBMSName'],'m_szDBMSCurDatabaseName',node['m_szDBMSCurDatabaseName'],'m_szDBMSUser',node['m_szDBMSUser']
