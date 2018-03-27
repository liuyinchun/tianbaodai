#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
author:liuyinchun
datetime:2018/3/27
'''
import traceback
import unittest,time
from .method import Params,StartApp,get_current_function_name
from common import get_screen,initlogin,input_text
from common.logger import Logger

class Credit(unittest.TestCase):
    def setUp(self):
        StartApp(self)            #启动app
        initlogin.init_login(self)            #登录
    def tearDown(self):
        self.driver.quit()

    def test_credit_addCard(self):
        u'''授信'''
        print("*****************执行授信用例****************")
        params = Params()
        self.driver.find_element_by_id("tv_apply").click()      #点击马上申请
        try:
            self.driver.find_element_by_id("tv_id_verify").click()      #点击实名认证
            time.sleep(2)
            self.driver.find_element_by_id("et_cardusername").send_keys(params['username'])     #输入持卡人姓名
            self.driver.find_element_by_id("et_idnum").send_keys(params['ID'])      #输入身份证号
            time.sleep(2)
            exist = False
            while exist == False:
                   self.driver.find_element_by_id("et_bankcardnum").click()             #输入银行卡号,4位一个空格
                   input_text.inputText(self,params['cardNumber'])            #调用了延时方法输入
                   self.driver.find_element_by_id("et_phone").send_keys(params['phone'])        #输入手机号
                   self.driver.find_element_by_id("tv_next").click()         #点击下一步
                   time.sleep(2)
                   try:
                       self.driver.find_element_by_id("et_idnum").click()          #输入银行卡信息有误
                       print("输入银行卡信息有误")
                       self.driver.find_element_by_id("iv_delete_idcard").click()
                       time.sleep(2)
                   except:
                       exist = True

            sms_yanzhengma = input("请输入短信验证码:")            #输入手机验证码
            time.sleep(8)
            self.driver.find_element_by_id("et_authcode").send_keys(sms_yanzhengma)
            self.driver.find_element_by_id('tv_next').click()        #点击下一步
            time.sleep(15)
            try:
                self.driver.find_element_by_id("tv_complete").click()     #点击跳过按钮
                exist = False
            except:
                print("短信验证码有误")
        except:
            print("授信失败")
            pic_name = get_current_function_name()            #获取当前方法名作为截图名
            get_screen.getScreen(self,pic_name)              #调用截图方法
            logger=Logger(logname='log.txt',loglevel="INFO",logger=pic_name).getlog()
            logger.error(traceback.format_exc())           #写入日志
        self.assertEqual(exist,False)



if __name__ == "__main__":
    unittest.main()