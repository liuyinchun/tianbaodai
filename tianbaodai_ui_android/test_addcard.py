#!/usr/bin/env python
#-*-coding:utf-8-*-
#!/usr/bin/env python
#-*-coding:utf8-*-
import unittest,time
from appium import webdriver
from .method import StartApp,inputText, Params


class AddCard(unittest.TestCase):
    def setUp(self):
        StartApp(self)
    def tearDown(self):
        self.driver.quit()
    #添加银行卡
    def test_addCard(self):

        u"""添加银行卡"""
        params = Params()
        self.driver.find_element_by_id("iv_head").click()
        #点击银行卡管理
        self.driver.find_element_by_id("rl_card_manage").click()
        #点击添加银行卡按钮
        self.driver.find_element_by_id("tv_addBankCard").click()
        time.sleep(2)
        #输入持卡人姓名
        self.driver.find_element_by_id("et_cardusername").send_keys(params['username'])
        #输入身份证号
        self.driver.find_element_by_id("et_idnum").send_keys(params['ID'])
        #输入银行卡号,4位一个空格
        self.driver.find_element_by_id("et_bankcardnum").click()
        #调用了延时方法输入
        inputText(self,params['ID'])
        #输入手机号
        self.driver.find_element_by_id("et_phone").send_keys(params['phone'])
        try:
          #点击下一步
          self.driver.find_element_by_id("tv_next").click()
          time.sleep(2)
          if self.driver.find_element_by_id("et_phone").is_displayed():
              exist = True
              print("绑卡失败")
          else:
            #输入手机验证码
           sms_yanzhengma = input("请输入短信验证码:")
           self.driver.find_element_by_id("et_authcode").send_keys(params['sms_yanzhengma'])

           self.driver.find_element_by_id('tv_next').click()
           time.sleep(2)

           try:
            if self.driver.find_element_by_id("tv_next").is_displayed():
                exist = True
           except Exception as e:
            exist = False
        except:
            exist = True
            print("绑卡失败")


        self.assertEqual(exist,False)


if __name__ == '__main__':
    unittest.main()
