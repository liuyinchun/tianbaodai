#!/usr/bin/env python
#-*-coding:utf-8-*-

#!/usr/bin/env python
#-*-coding:utf8-*-
import os
import unittest,time
from .method import StartApp, getScreen
from .method import inputText,slideApplyBar,is_resultActivity,Params
from common.initlogin import *

from common.logger import Logger

class JieKuan(unittest.TestCase):

    def setUp(self):
        StartApp(self)    #启动app
        init_login(self)  #登录
    def tearDown(self):
        init_logout(self)  #退出
        self.driver.quit()
    def test_JieKuan3(self):

        u"""借款-3期"""
        params = Params()
        try:
            #点击马上申请
            self.driver.find_element_by_id('tv_apply').click()
            time.sleep(3)
            #滑动借款条到500
            slideApplyBar(self)
            #选择借款场景:家用电器
            self.driver.find_element_by_id('rl_borrow_sence').click()
            self.driver.find_element_by_id('tv_sence').click()
            #借款周期
            self.driver.find_element_by_id('rl_num_periods').click()
            #选了分3期的
            self.driver.find_element_by_id('tv_sence').click()
            time.sleep(5)
            #获取借款额度
            edu = self.driver.find_element_by_id('com.ibeesaas.tianbaodai:id/tv_borrow_num').text
            num_edu = int(edu)
            if num_edu>=500:
                #点击马上借
                self.driver.find_element_by_id('tv_borrow_immedia').click()
                time.sleep(3)
                #加了延时输入
                inputText(self,params['applyPwd'])
                time.sleep(8)
                #判断是否成功
                is_resultActivity(self)
            else:
                exist = False
                print(u"额度小于500,无法借款")
        except Exception as e:
            exist = False
            #获取当前用例文件名作为截图名
            pic_name = list(os.path.basename(__file__).split('.'))[0]
            #调用截图方法
            getScreen(self,pic_name)
            #写入日志
            logger=Logger(logname='log.txt',loglevel="INFO",logger="test_login.py").getlog()
            logger.error(e)
        self.assertEqual(exist,True)

    def test_JieKuan6(self):
        u"""借款-6期"""
        params = Params()
        #点击马上申请
        self.driver.find_element_by_id('tv_apply').click()
        time.sleep(3)
        #滑动借款条到500
        slideApplyBar(self)
        #选择借款场景:家用电器
        self.driver.find_element_by_id('rl_borrow_sence').click()
        self.driver.find_element_by_id('tv_sence').click()
        #借款周期
        self.driver.find_element_by_id('rl_num_periods').click()
         #选了分6期的
        self.driver.find_element_by_xpath('//android.widget.ListView/android.widget.LinearLayout[2]/android.widget.TextView').click()
        time.sleep(5)
        #点击马上借
        edu = self.driver.find_element_by_id('com.ibeesaas.tianbaodai:id/tv_borrow_num').text
        num_edu = int(edu)
        if num_edu>=500:
            self.driver.find_element_by_id('tv_borrow_immedia').click()
            time.sleep(3)
            #加了延时输入
            inputText(self,params['applyPwd'])
            time.sleep(8)
            #判断是否成功
            is_resultActivity(self)
        else:
            exist = False
            print(u"额度小于500,无法借款")
        self.assertEqual(exist,True)
    def test_JieKuan12(self):
        u"""借款-12期"""
        params = Params()
        #点击马上申请
        self.driver.find_element_by_id('tv_apply').click()
        time.sleep(3)
        #滑动借款条到500
        slideApplyBar(self)
        #选择借款场景:家用电器
        self.driver.find_element_by_id('rl_borrow_sence').click()
        self.driver.find_element_by_id('tv_sence').click()
        #借款周期
        self.driver.find_element_by_id('rl_num_periods').click()
        #选了分12期的
        self.driver.find_element_by_xpath('//android.widget.ListView/android.widget.LinearLayout[3]/android.widget.TextView').click()
        time.sleep(5)
        #点击马上借
        edu = self.driver.find_element_by_id('com.ibeesaas.tianbaodai:id/tv_borrow_num').text
        num_edu = int(edu)
        if num_edu>=500:
          self.driver.find_element_by_id('tv_borrow_immedia').click()
          time.sleep(3)
          #加了延时输入
          inputText(self,params['applyPwd'])
          time.sleep(8)
          #判断跳转到结果页
          is_resultActivity(self)
        else:
            exist = False
            print(u"额度小于500,无法借款")
        self.assertEqual(exist,True)
if __name__ == '__main__':
    unittest.main()
