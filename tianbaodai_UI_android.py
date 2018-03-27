#!/usr/bin/env python
#-*-coding:utf8-*-
'''
author:liuyinchun
datetime:2018/3/23
'''
import unittest,time,os
from email import charset
import smtplib
import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header

os.system('start startAppiumServer.bat')    #启动appium服务
time.sleep(8)     #等待appium服务启动完毕

#导入用例
from tianbaodai_ui import test_login,test_addcard,test_huankuan,test_jiekuan,test_regist,test_updatepwd,test_reset_pwd,test_credit

#添加用例集
suite = unittest.TestSuite()

#==============================执行用例=======================

#注册
#suite.addTest(unittest.makeSuite(test_regist.Register))

#授信
suite.addTest(unittest.makeSuite(test_credit.Credit))

#忘记密码
#suite.addTest(unittest.makeSuite(test_reset_pwd.ResetPWD))

#登录
#suite.addTest(unittest.makeSuite(test_login.Login))

#添加银行卡
#suite.addTest(unittest.makeSuite(test_addcard.AddCard))

#借款
#suite.addTest(unittest.makeSuite(test_jiekuan.JieKuan))

#还款
#suite.addTest(unittest.makeSuite(test_huankuan.HuanKuan))

#修改密码
#suite.addTest(unittest.makeSuite(test_updatepwd.Updatepwd))


#执行用例
runner = unittest.TextTestRunner()
runner.run(suite)

os.system('start stopAppiumServer.bat')     #关闭appium服务

'''
#==============生成测试报告=============

#定义全局时间
now = time.strftime('%Y%m%d %H%M%S')

def newReport(testReport):
    lists = os.listdir(testReport)#返回测试报告所在目录下的所有文件列表
    lists2 = sorted(lists)#获得按升序排序后的测试报告列表
    file_new = os.path.join(testReport, lists2[-1])#获取最后一个即最新的测试报告地址
    return file_new

#==============发送邮件=============

def sendReport(file_new):
    print('1')
    #计算case通过率
    with open(file_new,'rb') as f:
        chst = charset.Charset(input_charset = 'utf-8')
        htmlf=open(file_new,'r',encoding="utf-8")
        mail_body=htmlf.read()

    msg = MIMEText('<html><body><h1>hi,all</h1>'+'<h2>测试内容:登录,借款等</h2>'
                   +'<h3>如下报告不可点击，要查看详细：<a href= "file:///G:/liuyinchun/tianbaodai/tianbaodai_report/report'+now+'.html"'+'>click here</a>...</h3>'
                   +'</body></html>'+mail_body,'html','utf-8')
    msg['Subject'] = Header(u'天宝贷ui自动化测试报告')
    msg['From'] = "liuyinchun@ibeesaas.com"
    msg['To'] = "766056364@qq.com"
    msg['Cc'] = "m18310141768@163.com"

    smtp = smtplib.SMTP_SSL('smtp.exmail.qq.com',port=465) #端口smtp
    smtp.login('liuyinchun@ibeesaas.com','Liuyc2017')
    smtp.sendmail(msg['From'],msg['To'].split(';') + msg['Cc'].split(';'),msg.as_string().encode('utf-8'))
    smtp.quit()

    print('test report has send out!')
if __name__ == '__main__':
    test_report = 'G:/liuyinchun/tianbaodai/tianbaodai_report'#测试报告所在目录
    filePath = 'G:/liuyinchun/tianbaodai/tianbaodai_report/report'+now+'.html'#通过加入报告生成时间，区分报告名称，否则报告会被覆盖
    fp = open(filePath,'wb')#打开文件，以二进制方式将结果写入文件
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'天宝贷ui自动化测试报告',description=u'ui测试')
    runResult=runner.run(suite)#执行测试，调用测试套件返回结果
    fp.close()#关闭文件，打开文件后一定要关闭文件，否则会占用资源。
    sendReport(filePath)
'''
