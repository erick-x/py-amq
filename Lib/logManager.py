#!/usr/bin/python
#coding:utf-8

import os
import logging
import time

'''
date 2016年4月22日
日志管理类
'''

#日志文件路径
path = "/data/log/"
log_style = '[%(asctime)s]%(filename)s %(funcName)s[line:%(lineno)d] %(message)s'

# 定义日期格式
formdate = time.strftime("%Y-%m-%d-", time.localtime())
# 创建日志路径
filepwd = os.getcwd() + path

'''
date 2016年4月22日
设置日志根式
logname 日志文件名字默认(debug)
'''
#调试类日志
def Debug(message,logname="debug"):

    if os.path.exists(filepwd) == False:
        os.makedirs(filepwd)

    filename = formdate + logname+'.log'
    logging.basicConfig(filename=os.path.join(filepwd, filename), format=log_style,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)
    logging.debug(message)

#日常类日志
def Info(message,logname="info"):
    if os.path.exists(filepwd) == False:
        os.makedirs(filepwd)

    filename = formdate + logname + '.log'
    logging.basicConfig(filename=os.path.join(filepwd, filename), format=log_style,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.INFO)
    logging.info(message)

#错误性日志
def Error(message,logname="error"):
    if os.path.exists(filepwd) == False:
        os.makedirs(filepwd)

    filename = formdate + logname + '.log'
    logging.basicConfig(filename=os.path.join(filepwd, filename), format=log_style,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.ERROR)
    logging.error(message)

#警告日志
def Warn(message,logname="warn"):
    if os.path.exists(filepwd) == False:
        os.makedirs(filepwd)

    filename = formdate + logname + '.log'
    logging.basicConfig(filename=os.path.join(filepwd, filename), format=log_style,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.WARNING)
    logging.warning(message)