import unittest,time,os
from appium import webdriver
from .method import StartApp

class Exit(unittest.TestCase):
    def setUp(self):
        StartApp(self)
    def test_Exit(self):
        u"""退出"""
        #从个人中心进入登录页
        self.driver.find_element_by_id("iv_head").click()
        self. driver.find_element_by_name('退出登录').click()
        try:
            if self.driver.find_element_by_name("退出登录").is_displayed():
                exist = True
        except Exception as e:
            exist = False

        self.assertEqual(exist, False)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
