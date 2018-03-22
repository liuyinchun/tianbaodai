#!/usr/bin/env python
#coding:utf-8
import time
import os
import unittest
from appium import webdriver
from lib2to3.tests.support import driver

import logging

#PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

#初始化
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


desired_caps = {}
#使用哪种移动平台
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
#启动哪种设备,是真机还是模拟器
desired_caps['deviceName'] = '192.168.28.101:5555'
#使用unicodekeyboard的编码方式来发送字符串
desired_caps['unicodeKeyboard'] = True
#将键盘隐藏
desired_caps['resetKeyboard'] = True
#可以获取toast弹窗消息
desired_caps['automationName'] =  'Uiautomator2'
#APP的绝对路径--安装
#desired_caps['app'] = PATH('D:\android-sdk-windows\platform-tools\tianbaodai_v1.0_baidu.apk')
#参数
desired_caps['appPackage'] = "com.ibeesaas.tianbaodai"
desired_caps['appActivity'] = "com.ibeesaas.tianbaodai.view.MainActivity"
#启动APP
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

'''
 is toast exist, return True or False
   :Agrs:
    - driver - 传driver
    - text   - 页面上看到的文本内容
    - timeout - 最大超时时间，默认30s
    - poll_frequency  - 间隔查询时间，默认0.5s查询一次
   :Usage:
    is_toast_exist(driver, "看到的内容")
   

def is_toast_exist(driver,text,timeout=30,poll_frequency=0.5):
   try:
     toast_loc = ("xpath", ".//*[contains(@text,'%s')]"%text)
     WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
     return True
   except:
       return False




#修改登录密码,测试获取toast消息
driver.find_element_by_id("iv_head").click()
#点击密码管理
driver.find_element_by_id("rl_pwd_manage").click()
#点击修改登录密码
driver.find_element_by_id("rl_reset_loginpwd").click()

#输入原密码
driver.find_element_by_id("et_originpwd").send_keys('123123')
#输入新密码
driver.find_element_by_id("et_pwd").send_keys('123123')
#再次输入新密码
driver.find_element_by_id("et_queren_pwd").send_keys('123123')

ac1 = driver.current_activity
print(ac1)

#点击确认修改
driver.find_element_by_id("tv_confimchange").click()
b = is_toast_exist(driver,"登录密码修改成功")

ac2 = driver.current_activity
print(ac2)

print(b)


'''

'''
#修改登录密码,测试获取toast消息
driver.find_element_by_id("iv_head").click()
#点击密码管理
driver.find_element_by_id("rl_pwd_manage").click()
#点击修改登录密码
driver.find_element_by_id("rl_reset_loginpwd").click()

#输入原密码
driver.find_element_by_id("et_originpwd").send_keys('123123')
#输入新密码
driver.find_element_by_id("et_pwd").send_keys('123123')
#再次输入新密码
driver.find_element_by_id("et_queren_pwd").send_keys('123123')
#点击确认修改
driver.find_element_by_id("tv_confimchange").click()


'''

#配置logging
logging.basicConfig(filename='logger.log',level=logging.INFO)  #默认只显示warn等级以上的,现改为info以上


'''
Logger 即记录器，Logger提供了日志相关功能的调用接口。
Handler 即处理器，将（记录器产生的）日志记录发送至合适的目的地。
Filter 即过滤器，提供了更好的粒度控制，它可以决定输出哪些日志记录。
Formatter 即格式化器，指明了最终输出中日志记录的格式。
'''

logger = logging.getLogger('test_example')  #创建了一个记录器,默认为root
logger.setLevel(logging.DEBUG)                #设置显示等级
handler = logging.StreamHandler()             #创建处理器
handler.setLevel(logging.WARN)
formatter =  logging.Formatter('%(asctime)s - %(name)s - %(message)s')
#配置logger
logger.addHandler(handler)     #配置

#使用日志
logger.debug("配置后 debug")
logger.info("配置后 info")
logger.warn("配置后 warn")
logger.error("配置后 error")
logger.critical("配置后 critical")


try:
   #先进入个人中心,再进入登录页
   driver.find_element_by_id("iv_head").click()
   driver.find_element_by_id("tv_login").click()

   #输入用户名
   driver.find_element_by_id("et_phonenum").send_keys("18310141768")
   #输入密码
   driver.find_element_by_id("et_pwd").send_keys("123123")
   #点击登录
   driver.find_element_by_id("tv_login").click()
   #返回按钮
   driver.find_element_by_id('iv_back').click()
except Exception as e:
    print(e)


'''



#借款
#点击马上申请
driver.find_element_by_id("tv_apply").click()
time.sleep(3)

x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
#模拟器现在屏幕数据x=768,y=1184
a = 200.0/768
b = 377.0/1184
x1 = int(x*a)
y1 = int(y*b)
print(x1)
print(y1)
#滑动借款额度条
#借款额度条的绝对坐标
driver.tap([(0,y1),(x1,y1)],100)

time.sleep(5)

'''


'''
#判断借款是否成功,支付密码框自动弹出自动收起,判断是否还在借款页
acJie1=driver.current_activity

#点击马上借
driver.find_element_by_id('tv_borrow_immedia').click()
time.sleep(5)

#弹出支付密码框,输入支付密码
driver.find_element_by_id('inputView').send_keys("123123")
time.sleep(5)

acJie2=driver.current_activity
if acJie1!=acJie2:
    print(u"借款成功")

else:
    print(u"借款失败")



#点击银行卡管理
driver.find_element_by_id("rl_card_manage").click()

#点击添加银行卡按钮
driver.find_element_by_id("tv_addBankCard").click()
#点击右上角 +
#driver.find_element_by_id("iv_add").click()

#输入持卡人姓名
driver.find_element_by_id("et_cardusername").send_keys("刘银春")
#输入身份证号
driver.find_element_by_id("et_idnum").send_keys("412727199006104044")
#输入银行卡号
driver.find_element_by_id("et_bankcardnum").send_keys("6214830180242611")
#输入手机号
driver.find_element_by_id("et_phone").send_keys("18310141768")

#点击下一步
driver.find_element_by_id("tv_next").click()

#输入手机验证码



#点击密码管理
driver.find_element_by_id("rl_pwd_manage").click()
#点击修改登录密码
driver.find_element_by_id("rl_reset_loginpwd").click()

#输入原密码
driver.find_element_by_id("et_originpwd").send_keys('123123')
#输入新密码
driver.find_element_by_id("et_pwd").send_keys('123456')
#再次输入新密码
driver.find_element_by_id("et_queren_pwd").send_keys('123456')

#点击确认修改
driver.find_element_by_id("tv_confimchange").click()


#判断是否退出成功

acExit1 = driver.current_activity
driver.find_element_by_name('退出登录').click()

acExit2 = driver.current_activity
if acExit1 != acExit2:
    print(u"退出成功")
else:
    print(u"退出失败")



#========还款多期

def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
#屏幕向上滑动
def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)
    #x坐标
    y1 = int(l[1] * 0.75)
    #起始y坐标
    y2 = int(l[1] * 0.25)
    #终点y坐标
    driver.swipe(x1, y1, x1, y2,t)


driver.find_element_by_id("rl_repayment").click()
time.sleep(2)
#选择第一条数据
driver.find_element_by_id("tv_state").click()

#选择多期
driver.find_element_by_id('ll_zoom').click()

swipeUp(1000)

try:
 #选择所有期中最后一期
 ele = driver.find_element_by_xpath('//android.widget.ListView/android.widget.LinearLayout[12]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView')
 ele.click()
 print("good")
except Exception as e:
    print(e)

'''



driver.quit()

