#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
author:liuyinchun
datetime:2018/3/23
'''
from appium import webdriver
import time

from tianbaodai_ui.method import Params

#未登录时登录
def init_login(self):
    #点击头像到个人中心页
    self.driver.find_element_by_id("iv_head").click()
    try:
        self.driver.find_element_by_id("rl_top").click()      #点击个人中心页中的登录,跳转到登录页
        time.sleep(2)
        params = Params()
        #输入登录数据
        self.driver.find_element_by_id("et_phonenum").send_keys(params['phone'])    #输入手机号
        self.driver.find_element_by_id("et_pwd").send_keys(params['loginPWD'])      #输入密码
        try:
            self.driver.find_element_by_id("et_imgpwd").send_keys(params[ 'image_yzm'])    #输入图形验证码
        except:
            pass
        self.driver.find_element_by_id("tv_login").click()         #点击登录
        time.sleep(3)
        self.driver.find_element_by_id("iv_back").click()          #返回到首页
        time.sleep(2)
    except:
        self.driver.find_element_by_id("iv_back").click()        #已登录就返回到个人中心页
        time.sleep(2)
        self.driver.find_element_by_id("iv_back").click()      #返回到首页
        time.sleep(2)


#已登录时退出
def init_logout(self):
    #点击头像到个人中心页
    self.driver.find_element_by_id("iv_head").click()
    try:
        self.driver.find_element_by_name('退出登录').click()      #点击个人中心页中退出按钮
        time.sleep(2)
        self.driver.find_element_by_id("iv_back").click()      #返回到首页
    except:
        self.driver.find_element_by_id("iv_back").click()      #返回到首页




