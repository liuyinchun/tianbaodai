'''
author:liuyinchun
datetime:2018/3/23
'''
import os
import traceback
import unittest,time
from .method import StartApp, Params, get_current_function_name
from common.logger import Logger
from common.get_screen import getScreen
from common import initlogin

#重置密码
class ResetPWD(unittest.TestCase):
    def setUp(self):
        StartApp(self)
        initlogin.init_logout(self)     #先退出登录
    def tearDown(self):
        self.driver.quit()
    def test_reset_pwd(self):
        u'''忘记密码'''
        print("*************执行忘记密码用例**************")
        params = Params()
        try:
            self.driver.find_element_by_id("iv_head").click()   #点击头像到个人中心页
            time.sleep(2)
            self.driver.find_element_by_id("rl_top").click()      #点击个人中心页中的登录,跳转到登录页
            time.sleep(2)
            self.driver.find_element_by_id('tv_forgetpwd').click()   #跳转到登录页,点击忘记密码
            time.sleep(2)
            #异常情况
            self.driver.find_element_by_id('et_phonenum').send_keys(params['phone'])   #输入手机号,其他不输入
            self.driver.find_element_by_id('tv_queren_reset').click()          #点击确认重置
            time.sleep(2)

            self.driver.find_element_by_id('et_phonenum').send_keys(params['phone'])   #输入手机号,其他不输入
            self.driver.find_element_by_id('tv_getAuthCode').click()    #获取短信验证码
            sms_yanzhengma = input("请输入短信验证码:")                 #手动输入
            time.sleep(8)
            self.driver.find_element_by_id('et_authcode').send_keys(sms_yanzhengma)   #脚本自动输入短信验证码
            self.driver.find_element_by_id('et_pwd').send_keys(params['loginPWD'])               #输入密码
            self.driver.find_element_by_id('et_queren_pwd').send_keys("111111")      #再次输入密码不一致
            self.driver.find_element_by_id('tv_queren_reset').click()          #点击确认重置

            #正确情况
            self.driver.find_element_by_id('et_phonenum').send_keys(params['phone'])   #输入手机号
            self.driver.find_element_by_id('tv_getAuthCode').click()    #获取短信验证码
            sms_yanzhengma = input("请输入短信验证码:")                 #手动输入
            time.sleep(8)
            self.driver.find_element_by_id('et_authcode').send_keys(sms_yanzhengma)   #脚本自动输入短信验证码
            self.driver.find_element_by_id('et_pwd').send_keys(params['loginPWD'])               #输入密码
            self.driver.find_element_by_id('et_queren_pwd').send_keys(params['loginPWD'])      #再次输入密码
            self.driver.find_element_by_id('tv_queren_reset').click()          #点击确认重置

            exist = False
            try:
                self.driver.find_element_by_id('tv_queren_reset').click()     #判断是否还存在确认按钮,确认是否成功修改
                print("输入密码有误")
                exist = True
            except Exception as e:
                pass

        except:
            exist = True
            pic_name = get_current_function_name()     #获取当前用例名
            getScreen(self,pic_name)   #调用截图方法
            logger=Logger(logname='log.txt',loglevel="INFO",logger=pic_name).getlog()
            logger.error(traceback.format_exc())
        self.assertEqual(exist, False)                      #修改失败,确认按钮存在



if __name__ == '__main__':
    unittest.main()
