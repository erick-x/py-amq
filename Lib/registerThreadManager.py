#!/usr/bin/python
#coding:gbk

from threadManager import ThreadManager

def testFunc(name):
    print "��һ���߳�:%s \n"%name

def Func(name):
    print "�ڶ����߳�:%s \n"%name

def registerInit():
    mythread = ThreadManager()
    mythread.RegisterFunc(testFunc,2,4)
    mythread.RegisterFunc(Func, 2, 2)