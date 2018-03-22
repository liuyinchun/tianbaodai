#!/usr/bin/env python
#-*-coding:utf-8-*-

#!/usr/bin/env python
#-*-coding:utf8-*-
import os
import traceback
import unittest,time
from appium import webdriver
from .method import StartApp,inputText, Params, getScreen
from common.logger import Logger


class Updatepwd(unittest.TestCase):
    def setUp(self):
        StartApp(self)
    def tearDown(self):
        self.driver.quit()
    def test_UpdateLogin(self):
        u"""修改登录密码"""
        params = Params()
        self.driver.find_element_by_id("iv_head").click()    #点击进入个人中心页
        self.driver.find_element_by_id("rl_pwd_manage").click()   #点击密码管理
        self.driver.find_element_by_id("rl_reset_loginpwd").click()   #点击修改登录密码
        self.driver.find_element_by_id("et_originpwd").send_keys(params['loginPWD'])   # #输入原密码
        self.driver.find_element_by_id("et_pwd").send_keys(params['loginPWD'])    #输入新密码
        self.driver.find_element_by_id("et_queren_pwd").send_keys(params['loginPWD'])   #再次输入新密码
        self.driver.find_element_by_id("tv_confimchange").click()   #点击确认修改
        time.sleep(2)



    def test_UpdatePay(self):
        u"""修改支付密码"""
        params = Params()
        self.driver.find_element_by_id("iv_head").click()
        self.driver.find_element_by_id("rl_pwd_manage").click()     #点击密码管理
        self.driver.find_element_by_id('tv_changeTranPwd').click()  #点击修改支付密码
        self.driver.find_element_by_id('tv_getAuthCode').click()     #点击获取支付密码

        zf_pwd = input("请输入短信验证码:")    #需要手动输入
        self.driver.find_element_by_id('et_authcode').send_keys(zf_pwd)

        self.driver.find_element_by_id('tv_next').click()  #点击下一步
        time.sleep(3)
        try:
            #输入支付密码
            inputText(self,params['applyPWD'])    #延时输入
            time.sleep(2)
            inputText(self,params['applyPWD'])     #再次确认输入
        except:
            pic_name = list(os.path.basename(__file__).split('.'))[0]   #获取文件名
            getScreen(self,pic_name)   #调用截图方法
            #写入日志
            logger=Logger(logname='log.txt',loglevel="INFO",logger="test_login.py").getlog()
            logger.error(traceback.format_exc())



if __name__ == '__main__':
    unittest.main()
