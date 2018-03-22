#!/usr/bin/env python

#获取操作系统的库
import logging
import os
import platform
#随机数,多开
import random

#import lib.Utils as U

import subprocess
#subprocess.Popen('killall node',shell=True)
#获取devices
import time

cmd = 'adb devices'

#re = subprocess.check_call(cmd)   #中文返回乱码
#print(re)

#可以使用,获取devices
sub = subprocess.getoutput(cmd)
s = sub.split("\n")[1]
#返回值为string
print(s)
#print(type(sub))

#-a 是指监听的ip
#-p 是指定监听的端口
#-bp 是指定连接android设备bootstrap的端口号
#-U 是指定设备
#--session-override 是指覆盖之前的session
#start_appium = 'appium -a 127.0.0.1 -p 4723 -bp 4724 -U '+s+' --session-override'
#start_appium = 'cmd'
#appium = subprocess.getoutput(start_appium)
#print(appium)

class Sp:
    def __init__(self, device):
        self.device = device

    def __start_driver(self, aport, bpport):
        """
        :return:
        """
        if platform.system() == 'Windows':
            import subprocess
            subprocess.Popen("appium -p %s -bp %s -U %s" %
                             (aport, bpport, self.device), shell=True)

    def start_appium(self):
        """
        启动appium
        p:appium port
        bp:bootstrap port
        :return: 返回appium端口参数
        """
        aport = random.randint(4700, 4900)
        bpport = random.randint(4700, 4900)
        self.__start_driver(aport, bpport)

        logging.info(
                'start appium :p %s bp %s device:%s' %
                (aport, bpport, self.device))

        time.sleep(10)
        return aport

    def main(self):
        """
        :return: 启动appium
        """
        return self.start_appium()

    def stop_appium(self):
        '''
        停止appium
        :return:
        '''
        if platform.system() == 'Windows':
            os.popen("taskkill /f /im node.exe")



'''
if __name__ == '__main__':
    s = Sp(s)
    s.main()
'''


