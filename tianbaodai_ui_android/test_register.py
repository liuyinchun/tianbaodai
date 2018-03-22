#!/usr/bin/env python
#-*-coding:utf-8-*-
#!/usr/bin/env python
#-*-coding:utf8-*-
import os
import traceback
import unittest,time
from appium import webdriver
from .method import StartApp, Params, getScreen
from common.logger import Logger


class Register(unittest.TestCase):
    def setUp(self):
        StartApp(self)
    def tearDown(self):
        self.driver.quit()
    def test_Register(self):
        u"""注册"""
        params = Params()
        #从首页点击马上申请
        self.driver.find_element_by_id("tv_apply").click()
        time.sleep(2)
        try:
            self.driver.find_element_by_id("tv_regist").click()     #跳转到登录页,点击注册
            #输入注册信息
            self.driver.find_element_by_id("et_phonenum").send_keys(params['phone'])
            self.driver.find_element_by_id("tv_getAuthCode").click()
            self.driver.find_element_by_id("et_authcode").send_keys(params['sms_yzm'])
            self.driver.find_element_by_id("et_imgpwd").send_keys(params['image_yzm'])
            self.driver.find_element_by_id("et_pwd").send_keys(params['loginPWD'])
            #点击注册按钮
            self.driver.find_element_by_id("tv_regist").click()
            time.sleep(3)
        except:
            pic_name = list(os.path.basename(__file__).split('.'))[0]
            #调用截图方法
            getScreen(self,pic_name)
            #写入日志
            logger=Logger(logname='log.txt',loglevel="INFO",logger="test_login.py").getlog()
            logger.error(traceback.format_exc())
        exist = False
        #判断是否存在退出按钮,以此推断是否登录成功
        try:
            self.driver.find_element_by_id("tv_regist").click()      #点击注册按钮
            time.sleep(2)
            exist = True
        except:
            pass
        self.assertEqual(exist,False)         #判断是否存在注册按钮,存在则fail





if __name__ == '__main__':
    unittest.main()
