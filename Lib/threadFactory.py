#!/usr/bin/python
#coding:utf-8
import threading
import time
class ThreadFactory(threading.Thread):
    def __init__(self,func,sleeptime):
        threading.Thread.__init__(self)
        self.func = func
        self.daemon = True #设置为守护线程
        self.stime = sleeptime

    def run(self):
        while True:
            self.func(self.getName()) #启动线程的运行函数
            time.sleep(self.stime)