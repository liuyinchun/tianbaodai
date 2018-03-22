#!/usr/bin/env python
#-*-coding:utf8-*-

import unittest
from appium import webdriver
import time,os,sys
from .method import *
import logging
import logging.config
from common.logger import Logger
import traceback
from common.initlogin import *

class Login(unittest.TestCase):
    def setUp(self):
        StartApp(self)
        print("*************执行登录用例**************")
    def tearDown(self):
        self.driver.quit()
    '''
    2, 首页进入个人中心页
    3、进入登陆界面
    4、点击忘记密码
    5、点击返回到手机号登陆界面
    6、点击注册，点击返回到手机号登陆界面
    7、什么都不输入，点击登陆
    8、输入任意手机号，点击登陆
    9、输入任意手机号，和任意密码，点击登陆
    10、输入正确手机号和错误密码，点击登陆
    11、输入正确手机号和正确密码点击登陆，进入到首页
    12、退出登陆，回到个人中心页
    '''
    def test_Login(self):
        u"""登录"""
        try:
            init_logout(self)       #退出登录
            time.sleep(2)
            self.driver.find_element_by_id("rl_top").click()      #点击个人中心页中的登录,跳转到登录页
            time.sleep(2)
            self.driver.find_element_by_id("tv_forgetpwd").click()  #点击忘记密码
            time.sleep(2)
            self.driver.find_element_by_id("iv_back").click()       #点击返回
            time.sleep(3)
            self.driver.find_element_by_id("tv_regist").click()     #点击注册
            time.sleep(2)
            self.driver.find_element_by_id("tv_regist_login").click()     #点击立即登录,返回到登录页
            time.sleep(2)
            #输入手机号,不输入密码
            self.driver.find_element_by_id("et_phonenum").send_keys("18310141768")
            self.driver.find_element_by_id("tv_login").click()     #输入手机号,不输入密码
            time.sleep(2)
            #输入任意手机号,任意密码
            self.driver.find_element_by_id("et_phonenum").send_keys("18310141760")
            self.driver.find_element_by_id("et_pwd").send_keys("121212")
            self.driver.find_element_by_id("tv_login").click()          #输入任意手机号,任意密码
            time.sleep(2)
            #输入正确手机号,错误密码
            self.driver.find_element_by_id("et_phonenum").send_keys("18310141768")
            self.driver.find_element_by_id("et_pwd").send_keys("121212")
            self.driver.find_element_by_id("tv_login").click()         #输入正确手机号,错误密码
            time.sleep(2)
            #输入正确登录数据
            params = Params()
            self.driver.find_element_by_id("et_phonenum").send_keys(params['phone'])
            self.driver.find_element_by_id("et_pwd").send_keys(params['loginPWD'])
            try:
                self.driver.find_element_by_id("et_imgpwd").send_keys(params[ 'image_yzm'])    #输入图形验证码
            except:
                pass
            #self.driver.find_element_by_id("tv_login").click()   #输入正确数据登录
            time.sleep(2)
        except:
            #print(traceback.format_exc())
            pic_name = list(os.path.basename(__file__).split('.'))[0]
            #调用截图方法
            getScreen(self,pic_name)
            #写入日志
            logger=Logger(logname='log.txt',loglevel="INFO",logger="test_login.py").getlog()
            logger.error(traceback.format_exc())
        exist = False
        #判断是否存在退出按钮,以此推断是否登录成功
        try:
            self.driver.find_element_by_name('退出登录').click()      #点击个人中心页中退出按钮
            time.sleep(2)
            exist = True
        except:
            pic_name = list(os.path.basename(__file__).split('.'))[0]
            #调用截图方法
            getScreen(self,pic_name)
            #写入日志
            logger=Logger(logname='log.txt',loglevel="INFO",logger="test_login.py").getlog()
            logger.error(traceback.format_exc())
            pass
        self.assertEqual(exist,True)         #判断是否存在退出按钮,不存在则fail



if __name__ == '__main__':
    unittest.main()
