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
from .method import StartApp,is_resultActivity, Params, get_current_function_name
from common.get_screen import getScreen
from common.input_text import inputText
from common.swipe_screen import swipeUp
from common import initlogin
from common.logger import Logger

#还款
class HuanKuan(unittest.TestCase):
    def setUp(self):
        StartApp(self)
        initlogin.init_login(self)         #执行登录
    def tearDown(self):
        self.driver.quit()
    def test_HuanKuan1(self,exist = False):
        u"""还款--默认首期"""
        print("*************执行 还款-默认首期 用例**************")
        params = Params()
        try:
            self.driver.find_element_by_id("rl_repayment").click()        #点击首页中的去还款
            time.sleep(2)
            self.driver.find_element_by_id("tv_state").click()         #选择第一条数据
            time.sleep(2)
            self.driver.find_element_by_id("tv_repayment").click()      #默认首期,直接点击还款
            time.sleep(2)
            self.driver.find_element_by_id("rl_top").click()           #跳转到银行卡管理页,选择第一个
            time.sleep(8)
            inputText(self,params['applyPWD'])                #输入支付密码
            time.sleep(8)
            exist=is_resultActivity(self)                   #判断是否成功跳转到了还款成功页
        except:
            exist = False
            #获取当前方法名作为截图名
            pic_name = get_current_function_name()
            #调用截图方法
            getScreen(self,pic_name)
            #写入日志
            logger=Logger(logname='log.txt',loglevel="INFO",logger=pic_name).getlog()
            logger.error(traceback.format_exc())
        self.assertEqual(exist, True)



    def test_HuanKuan2(self,exist = False):
        u"""还款--多期(全部还款)"""
        params = Params()
        print("*************执行 还款-多期全部还款 用例**************")
        try:
            self.driver.find_element_by_id("rl_repayment").click()           #点击首页中的去还款
            time.sleep(2)
            self.driver.find_element_by_id("tv_state").click()           #选择第一条数据
            self.driver.find_element_by_id('ll_zoom').click()     #选择多期
            swipeUp(self,1200)                    #往上拉页面
            eles = self.driver.find_elements_by_xpath('//android.widget.ListView/android.widget.LinearLayout')      #获取所有期数
            if len(eles) == 12:             #12期
                print("12期")
                self.driver.find_element_by_xpath('//android.widget.ListView/android.widget.LinearLayout[12]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView').click()
            elif len(eles) ==6:              #6期
                print("6期")
                ele = self.driver.find_element_by_xpath('//android.widget.ListView/android.widget.LinearLayout[6]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView').click()
            else:                           #3期
                print("3期")
                ele = self.driver.find_element_by_xpath('//android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView').click()
            swipeUp(self,1000)         #往上滑动页面,定位还款按钮
            self.driver.find_element_by_id("tv_repayment").click()     # 点击还款
            time.sleep(2)
            self.driver.find_element_by_id("rl_top").click()            #跳转到银行卡管理页,选择第一个
            time.sleep(8)
            inputText(self,params['applyPWD'])            #输入支付密码
            time.sleep(8)
            exist = is_resultActivity(self)            #判断是否成功
        except:
            exist = False
            #获取当前方法名作为截图名
            pic_name = get_current_function_name()
            #调用截图方法
            getScreen(self,pic_name)
            #写入日志
            logger=Logger(logname='log.txt',loglevel="INFO",logger=pic_name).getlog()
            logger.error(traceback.format_exc())
        self.assertEqual(exist, True)
if __name__ == '__main__':
    unittest.main()
