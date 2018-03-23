#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
author:liuyinchun
datetime:2018/3/23
'''
import logging
import logging.config
#日志模块
class Logger():
    def __init__(self,logname,loglevel,logger):

        self.logger=logging.getLogger(logger)    #创建一个logger
        self.logger.setLevel(logging.DEBUG)

        fh=logging.FileHandler(logname)     #创建一个handler，用于写入日志文件 
        fh.setLevel(loglevel)

        ch=logging.StreamHandler()       #再创建一个handler，用于输出到控制台
        ch.setLevel(loglevel)
        #定义handler的输出格式      
        log_format=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s-[%(filename)s:%(lineno)d]')
        fh.setFormatter(log_format)
        ch.setFormatter(log_format)

        self.logger.addHandler(fh)  #给logger添加handler
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger