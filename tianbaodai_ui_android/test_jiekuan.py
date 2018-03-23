#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
author:liuyinchun
datetime:2018/3/23
'''
import os
import traceback
import unittest,time
from .method import StartApp, get_current_function_name
from .method import slideApplyBar,is_resultActivity,Params
from common.initlogin import *
from common.get_screen import getScreen
from common.input_text import inputText
from common.logger import Logger
from common import initlogin

class JieKuan(unittest.TestCase):

    def setUp(self):
        StartApp(self)    #启动app
        initlogin.init_login(self)         #执行登录
    def tearDown(self):
        self.driver.quit()
    def test_JieKuan3(self):
        u"""借款-3期"""
        params = Params()
        print("*************执行借款用例**************")
        self.driver.find_element_by_id('tv_apply').click()            #点击马上申请
        time.sleep(3)
        try:
            slideApplyBar(self)                #滑动借款条到500
            self.driver.find_element_by_id('rl_borrow_sence').click()       #选择借款场景
            self.driver.find_element_by_id('tv_sence').click()                #家用电器
            self.driver.find_element_by_id('rl_num_periods').click()          #借款周期
            self.driver.find_element_by_id('tv_sence').click()                 #选了分3期的
            time.sleep(8)
            edu = self.driver.find_element_by_id('tv_borrow_num').text      #获取借款额度
            num_edu = int(edu)
            if num_edu>=500:
                self.driver.find_element_by_id('tv_borrow_immedia').click()       #点击马上借
                time.sleep(3)
                inputText(self,params['applyPwd'])         #输入支付密码,加了延时输入
                time.sleep(8)
                exist = is_resultActivity(self)                #判断是否成功跳转到借款成功页
            else:
                exist = False
                self.driver.find_element_by_id('tv_borrow_immedia').click()       #点击马上借
                print(u"额度小于500,无法借款")
        except:
            exist = False
            #获取当前方法名作为截图名
            pic_name = get_current_function_name()
            #调用截图方法
            getScreen(self,pic_name)
            #写入日志
            logger=Logger(logname='log.txt',loglevel="INFO",logger=pic_name).getlog()
            logger.error(traceback.format_exc())
        self.assertEqual(exist,True)

    def test_JieKuan6(self):
        u"""借款-6期"""
        params = Params()
        #点击马上申请
        self.driver.find_element_by_id('tv_apply').click()
        time.sleep(3)
        try:
            slideApplyBar(self)          #滑动借款条到500
            self.driver.find_element_by_id('rl_borrow_sence').click()      #选择借款场景
            self.driver.find_element_by_id('tv_sence').click()              #家用电器
            self.driver.find_element_by_id('rl_num_periods').click()        #借款周期
            self.driver.find_element_by_xpath('//android.widget.ListView/android.widget.LinearLayout[2]/android.widget.TextView').click()     #选了分6期的
            time.sleep(8)
            edu = self.driver.find_element_by_id('com.ibeesaas.tianbaodai:id/tv_borrow_num').text     #获取额度
            num_edu = int(edu)
            if num_edu>=500:
                self.driver.find_element_by_id('tv_borrow_immedia').click()    #点击马上借
                time.sleep(3)
                inputText(self,params['applyPwd'])                 #加了延时输入
                time.sleep(8)
                exist = is_resultActivity(self)                #判断是否成功跳转到借款成功页
            else:
                exist = False
                self.driver.find_element_by_id('tv_borrow_immedia').click()    #点击马上借
                print(u"额度小于500,无法借款")
        except:
            exist = False
            #获取当前方法作为截图名
            pic_name = get_current_function_name()
            #调用截图方法
            getScreen(self,pic_name)
            #写入日志
            logger=Logger(logname='log.txt',loglevel="INFO",logger=pic_name).getlog()
            logger.error(traceback.format_exc())
        self.assertEqual(exist,True)

    def test_JieKuan12(self):
        u"""借款-12期"""
        params = Params()
        #点击马上申请
        self.driver.find_element_by_id('tv_apply').click()
        time.sleep(3)
        try:
            slideApplyBar(self)                   #滑动借款条到500
            self.driver.find_element_by_id('rl_borrow_sence').click()              #选择借款场景:家用电器
            self.driver.find_element_by_id('tv_sence').click()
            self.driver.find_element_by_id('rl_num_periods').click()              #借款周期
            self.driver.find_element_by_xpath('//android.widget.ListView/android.widget.LinearLayout[3]/android.widget.TextView').click()       #选了分12期的
            time.sleep(8)
            edu = self.driver.find_element_by_id('com.ibeesaas.tianbaodai:id/tv_borrow_num').text     #获取额度
            num_edu = int(edu)
            if num_edu>=500:
                self.driver.find_element_by_id('tv_borrow_immedia').click()    #点击马上借
                time.sleep(3)
                inputText(self,params['applyPwd'])                 #加了延时输入
                time.sleep(8)
                exist = is_resultActivity(self)                #判断是否成功跳转到借款成功页
            else:
                exist = False
                self.driver.find_element_by_id('tv_borrow_immedia').click()    #点击马上借
                print(u"额度小于500,无法借款")
        except:
            exist = False
            #获取方法名作为截图名
            pic_name = get_current_function_name()
            #调用截图方法
            getScreen(self,pic_name)
            #写入日志
            logger=Logger(logname='log.txt',loglevel="INFO",logger=pic_name).getlog()
            logger.error(traceback.format_exc())
        self.assertEqual(exist,True)


if __name__ == '__main__':
    unittest.main()
