#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
author:liuyinchun
datetime:2018/3/23
'''

#滑动屏幕

#获得机器屏幕大小x,y
def getSize(self):
    x = self.driver.get_window_size()['width']
    y = self.driver.get_window_size()['height']
    return (x, y)
#屏幕向上滑动
def swipeUp(self,t):
    l = getSize(self)
    x1 = int(l[0] * 0.5)
    #x坐标
    y1 = int(l[1] * 0.75)
    #起始y坐标
    y2 = int(l[1] * 0.25)
    #终点y坐标
    self.driver.swipe(x1, y1, x1, y2,t)
#屏幕向下滑动
def swipeDown(self,t):
    l = getSize(self)
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.25)
    y2 = int(l[1] * 0.75)
    self.driver.swipe(x1, y1, x1, y2,t)
#屏幕向左滑动
def swipLeft(self,t):
    l=getSize(self)
    x1=int(l[0]*0.75)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.05)
    self.driver.swipe(x1,y1,x2,y1,t)
#屏幕向右滑动
def swipRight(self,t):
    l=getSize(self)
    x1=int(l[0]*0.05)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.75)
    self.driver.swipe(x1,y1,x2,y1,t)
#调用向左滑动
#swipLeft(1000)
#time.sleep(3)
#调用向右滑动
#swipRight(1000)
#调用向上滑动
#swipeUp(1000)
#调用向下滑动
#swipeDown(1000)
