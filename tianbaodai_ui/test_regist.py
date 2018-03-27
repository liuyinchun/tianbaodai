#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
author:liuyinchun
datetime:2018/3/23
'''
import os
import traceback
import unittest,time
from appium import webdriver
from .method import StartApp, Params, get_current_function_name
from common import initlogin
from common.logger import Logger
from common.get_screen import getScreen

#注册
class Register(unittest.TestCase):
    def setUp(self):
        StartApp(self)
        initlogin.init_logout(self)     #先退出登录
    def tearDown(self):
        self.driver.quit()
    def test_Register(self):
        u"""注册"""
        print("*************执行注册用例**************")
        params = Params()
        self.driver.find_element_by_id("iv_head").click()   #点击头像到个人中心页
        time.sleep(2)
        self.driver.find_element_by_id("rl_top").click()      #点击个人中心页中的登录,跳转到登录页
        time.sleep(2)
        try:
            self.driver.find_element_by_id("tv_regist").click()         #点击注册按钮,跳转到注册页
            time.sleep(2)
            self.driver.find_element_by_id("tv_regist_login").click()       #点击注册页中的立即登录,跳转到登录
            time.sleep(2)
            self.driver.find_element_by_id("tv_regist").click()          #再点击注册
            time.sleep(2)
            #异常情况
            self.driver.find_element_by_id("tv_getAuthCode").click()     #不输入手机号,点击获取短信验证码
            time.sleep(2)

            self.driver.find_element_by_id("et_phonenum").send_keys(params['phone'])      #输入手机号,其他不输入
            self.driver.find_element_by_id("tv_regist").click()    #点击注册
            time.sleep(2)

            self.driver.find_element_by_id("et_phonenum").send_keys(params['phone'])      #输入手机号
            self.driver.find_element_by_id("tv_getAuthCode").click()                      #点击获取短信验证码
            self.driver.find_element_by_id("et_authcode").send_keys(params['sms_yzm'])   #输入通用短信验证码
            self.driver.find_element_by_id("tv_regist").click()    #点击注册
            time.sleep(2)

            self.driver.find_element_by_id("et_phonenum").send_keys(params['phone'])      #输入手机号
            self.driver.find_element_by_id("tv_getAuthCode").click()                      #点击获取短信验证码
            time.sleep(2)
            self.driver.find_element_by_id("et_authcode").send_keys(params['sms_yzm'])   #输入通用短信验证码
            time.sleep(2)
            self.driver.find_element_by_id("et_imgpwd").send_keys("123123")              #输入错误图形验证码
            time.sleep(2)
            self.driver.find_element_by_id("et_pwd").send_keys(params['loginPWD'])       #输入密码
            self.driver.find_element_by_id("tv_regist").click()    #点击注册
            time.sleep(2)

            self.driver.find_element_by_id("et_phonenum").send_keys(params['phone'])       #输入手机号
            self.driver.find_element_by_id("tv_getAuthCode").click()                       #点击获取短信验证码
            time.sleep(2)
            self.driver.find_element_by_id("et_authcode").send_keys("123")                #输入错误短信验证码
            time.sleep(2)
            self.driver.find_element_by_id("et_imgpwd").send_keys(params['image_yzm'])   #输入错误图形验证码
            time.sleep(2)
            self.driver.find_element_by_id("et_pwd").send_keys(params['loginPWD'])       #输入密码
            self.driver.find_element_by_id("tv_regist").click()    #点击注册
            time.sleep(2)

            #输入正确注册信息
            self.driver.find_element_by_id("et_phonenum").send_keys(params['phone'])      #输入手机号
            self.driver.find_element_by_id("tv_getAuthCode").click()                      #点击获取短信验证码
            time.sleep(2)
            self.driver.find_element_by_id("et_authcode").send_keys(params['sms_yzm'])   #输入通用短信验证码
            time.sleep(2)
            self.driver.find_element_by_id("et_imgpwd").send_keys(params['image_yzm'])   #输入通用短信验证码
            time.sleep(2)
            self.driver.find_element_by_id("et_pwd").send_keys(params['loginPWD'])        #输入密码

            self.driver.find_element_by_id("tv_regist").click()     #点击注册按钮
            time.sleep(5)

            exist = False
            #判断是否存在注册按钮,以此推断是否登录成功
            #例如有已注册手机号
            try:
                self.driver.find_element_by_id("tv_regist").click()      #再次点击注册
                print("手机号已注册")
                time.sleep(2)
                exist = True
            except:
                pass
        except:
            exist = True
            pic_name = get_current_function_name()     #获取当前用例名
            getScreen(self,pic_name)   #调用截图方法
            logger=Logger(logname='log.txt',loglevel="INFO",logger=pic_name).getlog()
            logger.error(traceback.format_exc())     #写入日志
        self.assertEqual(exist,False)         #注册失败





if __name__ == '__main__':
    unittest.main()
