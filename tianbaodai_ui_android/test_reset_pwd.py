import unittest,time
from .method import StartApp, Params


class ResetPWD(unittest.TestCase):
    def setUp(self):
        StartApp(self)
    def tearDown(self):
        self.driver.quit()
    def test_reset_pwd(self):

        u'''忘记密码'''
        params = Params()
        #从首页点击马上申请
        self.driver.find_element_by_id("tv_apply").click()
        time.sleep(1)
        #跳转到登录页,点击忘记密码
        self.driver.find_element_by_id('tv_forgetpwd').click()
        #输入手机号
        self.driver.find_element_by_id('et_phonenum').send_keys(params['phone'])
        #输入短信验证码
        self.driver.find_element_by_id('tv_getAuthCode').click()
        #只有登录和注册可以用通用验证码
        sms_yanzhengma = input("请输入短信验证码:")
        self.driver.find_element_by_id('et_authcode').send_keys(sms_yanzhengma)

        #输入两次密码
        self.driver.find_element_by_id('et_pwd').send_keys(params['loginPWD'])
        self.driver.find_element_by_id('et_queren_pwd').send_keys(params['loginPWD'])

        #点击确认重置
        self.driver.find_element_by_id('tv_queren_reset').click()
        try:
            #判断是否还存在确认按钮,确认是否成功修改
            if self.driver.find_element_by_id('tv_queren_reset').is_displayed():
                exist = True
        except Exception as e:
            exist = False
        self.assertEqual(exist, False)


if __name__ == '__main__':
    unittest.main()
