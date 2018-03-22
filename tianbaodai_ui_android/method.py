#!/usr/bin/env python
#-*-coding:utf-8-*-

import os,time
import sys
from appium import webdriver
import logging

PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

#========================================初始化=======================================
def StartApp(self):
    desired_caps = {}
    desired_caps['platformName'] = 'android'
    desired_caps['platformVersion'] = '6.0'
    desired_caps['deviceName'] = 'a316ca28'     #oppo R9
    #模拟器
    #desired_caps['deviceName'] = '192.168.28.101:5555'
    #apk路径
    #desired_caps['app'] = PATH('G:\\liuyinchun\\tianbaodai\\app\\tianbaodai_v1.1_shunfengjin.apk')
    #不用每次都安装
    desired_caps['noReset'] = True
    #包名
    desired_caps['appPackage'] = 'com.ibeesaas.tianbaodai'
    desired_caps['appActivity'] = '.view.MainActivity'
    #可以获取toast弹窗消息----此方法没用
    #desired_caps['automationName'] =  'Uiautomator2'
    #隐藏键盘/中文编码方式
    #desired_caps['resetKeyboard'] = True
    #desired_caps['unicodeKeyboard'] = True
    #启动app
    self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    self.driver.wait_activity(".view.MainActivity", 10)

    time.sleep(2)


#================================定义参数====================================

def Params():
    params = {
        'username':'刘银春',
        'ID':'412727199006104044',
        'phone':'18310141768',
        'loginPWD':'123123',
        'cardNumber':'6214830180242611',
        'applyPWD':'123123',
        #只有登录和注册可以用通用验证码
        #短信验证码
        'sms_yzm':'999000',
         #图形验证码
        'image_yzm':'9900'
    }
    return params




#==============================截  图=======================================

def getScreen(self,pic_name):
    #绝对路径
    #f = list(sys.argv[0].split('.'))[0]  #获取当前脚本目录名,不带文件名
    #文件名
    #f1 = os.path.realpath(__file__)     #获取当前脚本目录全名,带文件名
    #f2 = os.path.basename(__file__)     #获取当前脚本文件名

    #在执行所有用例时都需要粘贴,
    #pic_name = list(os.path.basename(__file__).split('.'))[0]    #获取脚本文件名,不带后缀  作为图片名


    filePath = os.path.split(os.path.realpath(sys.argv[0]))[0]    #获取当前脚本目录名上一级 输出G:liu/tianbaodai

    filename = filePath+"\\getscreen\\"+pic_name+".png"   #拼接图片路径

    self.driver.get_screenshot_as_file(filename)       #截图并保存





#===============================滑动借款额度条================================


def slideApplyBar(self):
    #滑动借款额度条
    #self.driver.find_element_by_id('seekBar').click()
    #获取屏幕比值
    x = self.driver.get_window_size()['width']
    y = self.driver.get_window_size()['height']
    #模拟器现在屏幕数据x=768,y=1184
    a = 200.0/768
    b = 377.0/1184
    x1 = int(x*a)
    y1 = int(y*b)
    #借款额度条的相对坐标,每次借款最小值500
    self.driver.tap([(0,y1),(x1,y1)],100)

#===============================判断用例是否跳转===========================
#判断是否跳转到了登录页
def is_loginActivity(self):
    ac_result = self.driver.current_activity
    if ac_result == ".view.LoginActivity":
        exist = True
    else:
        print("已登录")
        exist = False
    return exist
#借款还款后页面是否跳转到结果页,若跳转说明成功
def is_resultActivity(self):
    #获取当前页面activity
    ac_result = self.driver.current_activity
    if ac_result == ".view.LoanOrRepaymentResultActivity":
        exist = True
    else:
        print("未跳转到结果页")
        exist = False
    return exist



#===============================键盘输入================================

#键盘输入某值
def enterText(self,text):
    key=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    keyCode=['7','8','9','10','11','12','13','14','15','16','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54']
    for k in range(len(key)):
        if text == key[k]:
            # print key[k], keyCode[k]
            #键盘输入
            self.driver.press_keycode(keyCode[k])
            time.sleep(2)
        else:
            pass
#与上面的方法配合使用,可以输入一个字符串值
def inputText(self,text):
    li = list(text)
    for i in li:
        enterText(self,i)






#================================滑动屏幕=================================
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


#========================清除文本框内容=================
def deleView(self,text):
    self.driver.sendKeyEvent(123);             #123：光标移动到输入框最右边
    i=0
    if i < text.length():
       i = i+1
       self.driver.sendKeyEvent(67)             #67：delete键


