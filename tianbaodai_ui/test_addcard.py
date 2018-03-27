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
from .method import StartApp,Params, get_current_function_name
from common.get_screen import getScreen
from common.input_text import inputText
from common import initlogin
from common.logger import Logger

class AddCard(unittest.TestCase):
    def setUp(self):
        StartApp(self)
        initlogin.init_login(self)         #执行登录
    def tearDown(self):
        self.driver.quit()
    #添加银行卡
    def test_addCard(self):
        u"""添加银行卡"""
        print("*************执行添加银行卡用例**************")
        params = Params()
        self.driver.find_element_by_id("iv_head").click()        #点击头像进入个人中心页
        self.driver.find_element_by_id("rl_card_manage").click() #点击银行卡管理
        time.sleep(2)
        try:
            self.driver.find_element_by_id("tv_addBankCard").click()       #点击添加银行卡按钮
            time.sleep(2)
            self.driver.find_element_by_id("et_cardusername").send_keys(params['username'])     #输入持卡人姓名
            self.driver.find_element_by_id("et_idnum").send_keys(params['ID'])      #输入身份证号
            self.driver.find_element_by_id("et_bankcardnum").click()             #输入银行卡号,4位一个空格
            inputText(self,params['cardNumber'])            #调用了延时方法输入
            self.driver.find_element_by_id("et_phone").send_keys(params['phone'])        #输入手机号
            self.driver.find_element_by_id("tv_next").click()         #点击下一步
            time.sleep(2)
            exist = True
            try:
                self.driver.find_element_by_id("et_phone").click()          #输入银行卡信息有误
                print("输入银行卡信息有误")
            except:
                 sms_yanzhengma = input("请输入短信验证码:")            #输入手机验证码
                 time.sleep(8)
                 self.driver.find_element_by_id("et_authcode").send_keys(params['sms_yanzhengma'])
                 self.driver.find_element_by_id('tv_next').click()        #点击下一步
                 time.sleep(5)
                 try:
                     self.driver.find_element_by_id("tv_next").click()     #短信验证码有误
                     print("短信验证码有误")
                 except:
                     exist = False
        except:
            print("绑卡失败")
            #获取当前方法名作为截图名
            pic_name = get_current_function_name()
            #调用截图方法
            getScreen(self,pic_name)
            #写入日志
            logger=Logger(logname='log.txt',loglevel="INFO",logger=pic_name).getlog()
            logger.error(traceback.format_exc())
        self.assertEqual(exist,False)


if __name__ == '__main__':
    unittest.main()
