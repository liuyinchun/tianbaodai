#!/usr/bin/env python
#-*-coding:utf-8-*-
#!/usr/bin/env python
#-*-coding:utf8-*-
import unittest,time
from appium import webdriver
from .method import StartApp, inputText,swipeUp,is_resultActivity, Params


#还款
class HuanKuan(unittest.TestCase):
    def setUp(self):
        StartApp(self)
    def tearDown(self):
        self.driver.quit()
    def test_HuanKuan1(self,exist = False):

        u"""还款--默认首期"""
        params = Params()
        #点击首页中的去还款
        self.driver.find_element_by_id("rl_repayment").click()
        time.sleep(2)
        #选择第一条数据
        self.driver.find_element_by_id("tv_state").click()
        #默认首期,直接点击还款
        self.driver.find_element_by_id("tv_repayment").click()
        time.sleep(2)
        #跳转到银行卡管理页
        self.driver.find_element_by_id("rl_top").click()
        time.sleep(8)
        #输入支付密码
        inputText(self,params['applyPWD'])
        time.sleep(8)
        #判断是否成功
        is_resultActivity(self)
        self.assertEqual(exist, True)
    def test_HuanKuan3(self,exist = False):

        u"""还款--多期(选择全部)"""
        params = Params()
        #点击首页中的去还款
        self.driver.find_element_by_id("rl_repayment").click()
        time.sleep(2)
        #选择第一条数据
        self.driver.find_element_by_id("tv_state").click()
        #选择多期
        self.driver.find_element_by_id('ll_zoom').click()
        #往上拉页面
        swipeUp(self,1200)
        #选择所有期中最后一期
        eles = self.driver.find_elements_by_xpath('//android.widget.ListView/android.widget.LinearLayout')
        try:
          if len(eles) == 12:
              print("12期")
              self.driver.find_element_by_xpath('//android.widget.ListView/android.widget.LinearLayout[12]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView').click()
          elif len(eles) ==6:
              print("6期")
              ele = self.driver.find_element_by_xpath('//android.widget.ListView/android.widget.LinearLayout[6]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView').click()
          else:
              print("3期")
              ele = self.driver.find_element_by_xpath('//android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView').click()
        except Exception as e:
            print(e)
        #往上滑动页面,定位还款按钮
        swipeUp(self,1000)
        # 点击还款
        self.driver.find_element_by_id("tv_repayment").click()
        time.sleep(2)
        #跳转到银行卡管理页
        self.driver.find_element_by_id("rl_top").click()
        time.sleep(8)
        #输入支付密码
        inputText(self,params['applyPWD'])
        time.sleep(8)
        #判断是否成功
        is_resultActivity(self)
        self.assertEqual(exist, True)
if __name__ == '__main__':
    unittest.main()
