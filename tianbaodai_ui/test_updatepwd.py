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
from common.logger import Logger
from common  import initlogin
from common.get_screen import getScreen
from common.input_text import inputText


class Updatepwd(unittest.TestCase):
    def setUp(self):
        StartApp(self)
        initlogin.init_login(self)              #先登录
    def tearDown(self):
        self.driver.quit()
    def test_UpdateLogin(self):
        u"""修改登录密码"""
        print("*************执行修改登录密码用例**************")
        params = Params()
        self.driver.find_element_by_id("iv_head").click()    #点击进入个人中心页
        self.driver.find_element_by_id("rl_pwd_manage").click()   #点击密码管理
        try:
            self.driver.find_element_by_id("rl_reset_loginpwd").click()   #点击修改登录密码
            #异常情况
            self.driver.find_element_by_id("tv_confimchange").click()   #不输入,点击确认修改
            time.sleep(2)

            self.driver.find_element_by_id("et_originpwd").send_keys(params['loginPWD'])   # #输入原密码
            self.driver.find_element_by_id("et_pwd").send_keys(params['loginPWD'])    #输入新密码
            self.driver.find_element_by_id("et_queren_pwd").send_keys("111111")   #再次输入 不一致新密码
            self.driver.find_element_by_id("tv_confimchange").click()   #点击确认修改
            time.sleep(2)
            #正常情况
            self.driver.find_element_by_id("et_originpwd").send_keys(params['loginPWD'])   # #输入原密码
            time.sleep(2)
            self.driver.find_element_by_id("et_pwd").send_keys(params['loginPWD'])    #输入新密码
            time.sleep(2)
            self.driver.find_element_by_id("et_queren_pwd").send_keys(params['loginPWD'])   #再次输入新密码
            self.driver.find_element_by_id("tv_confimchange").click()   #点击确认修改
            time.sleep(2)

            exist = False
            try:
                self.driver.find_element_by_id("tv_confimchange").click()   #点击确认修改
                exist = True
            except:
                pass
        except:
            exist = True
            pic_name = get_current_function_name()
            #调用截图方法
            getScreen(self,pic_name)
            #写入日志
            logger=Logger(logname='log.txt',loglevel="INFO",logger=pic_name).getlog()
            logger.info("*************执行修改登录密码用例**************")
            logger.error(traceback.format_exc())
        self.assertEqual(exist,False)         #已跳转,不在修改页




    def test_UpdatePay(self):
        u"""修改支付密码"""
        print("*************执行修改支付密码用例**************")
        params = Params()
        self.driver.find_element_by_id("iv_head").click()
        self.driver.find_element_by_id("rl_pwd_manage").click()     #点击密码管理
        try:
            self.driver.find_element_by_id('tv_changeTranPwd').click()  #点击修改支付密码
            self.driver.find_element_by_id('tv_getAuthCode').click()     #点击获取支付密码
            zf_pwd = input("请输入短信验证码:")    #需要手动输入
            time.sleep(8)
            self.driver.find_element_by_id('et_authcode').send_keys(zf_pwd)
            self.driver.find_element_by_id('tv_next').click()  #点击下一步
            time.sleep(2)
            try:
                #输入支付密码
                inputText(self,params['applyPWD'])    #延时输入
                time.sleep(2)
                inputText(self,params['applyPWD'])    #再次确认输入
                time.sleep(2)
            except:
                 pass
            exist = False
            try:
                self.driver.find_element_by_id("inputView").click()    #输入框是否隐藏
                exist = True
            except:
                print("两次输入不一致")
                pass
        except:
            exist = True
            pic_name = get_current_function_name()   #获取方法名
            getScreen(self,pic_name)   #调用截图方法
            #写入日志
            logger=Logger(logname='log.txt',loglevel="INFO",logger=pic_name).getlog()
            logger.info("*************执行修改支付密码用例**************")
            logger.error(traceback.format_exc())
        self.assertEqual(exist,False)         #已跳转,不在修改页



if __name__ == '__main__':
    unittest.main()
