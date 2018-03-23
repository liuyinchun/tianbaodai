#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
author:liuyinchun
datetime:2018/3/23
'''

#========================清除文本框内容=================
def deleView(self,text):
    self.driver.sendKeyEvent(123);             #123：光标移动到输入框最右边
    i=0
    if i < text.length():
        i = i+1
        self.driver.sendKeyEvent(67)             #67：delete键