#!/usr/bin/python
#coding:utf-8
'''
线程管理类
quThread 线程队列
外部注册线程的执行方法
默认注册线程方法为1个线程，sleep时间为0.01秒
'''

from threadFactory import ThreadFactory
from logManager import *
from singleton import *

class ThreadManager():

    __metaclass__ = Singleton

    def __init__(self):
        #线程队列
        self.quThread={}

    def __del__(self):
        del self.quThread

    #注册外部方法
    def RegisterFunc(self,func,number=1,stime =1):
        self.quThread[func] = (number,stime)

    def start(self):
        if(len(self.quThread) ==0):
            Debug("空列表")
            return

        for k in self.quThread.keys():
            for i in range(self.quThread[k][0]):
                thread = ThreadFactory(k,self.quThread[k][1])
                thread.start()

