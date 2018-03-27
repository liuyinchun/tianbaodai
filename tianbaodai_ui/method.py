'''
author:liuyinchun
datetime:2018/3/23
'''
import inspect
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
    desired_caps['resetKeyboard'] = True
    desired_caps['unicodeKeyboard'] = True
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

#=============================获取方法名=================================
def get_current_function_name():

    return inspect.stack()[1][3]


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

#借款还款后页面是否跳转到结果页,若跳转说明成功
def is_resultActivity(self):
    #获取当前页面activity
    ac_result = self.driver.current_activity
    if ac_result == ".view.LoanOrRepaymentResultActivity":
        return True
    else:
        print("未跳转到结果页")
        return False




