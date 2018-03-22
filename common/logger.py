#!/usr/bin/env python
#-*-coding:utf-8-*-
import logging
import logging.config
class Logger():
    def __init__(self,logname,loglevel,logger):
        #创建一个logger
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        #创建一个handler，用于写入日志文件  
        fh=logging.FileHandler(logname)
        fh.setLevel(loglevel)
        #再创建一个handler，用于输出到控制台  
        ch=logging.StreamHandler()
        ch.setLevel(loglevel)
        #定义handler的输出格式      
        log_format=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s-[%(filename)s:%(lineno)d]')
        fh.setFormatter(log_format)
        ch.setFormatter(log_format)
        #给logger添加handler  
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger