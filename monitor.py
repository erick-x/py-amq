#!/usr/bin/python
#coding:utf-8

from main import *
import sys
import os
if __name__ == "__main__":
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            start()
        elif 'stop' == sys.argv[1]:
            stop()
        elif 'restart' == sys.argv[1]:
            pass
        else:
            print 'unkonw command'
            sys.exit(2)

    loadDBConf()

