#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
author:liuyinchun
datetime:2018/3/23
'''

#键盘输入某值
import time

#键盘输入
def enterText(self,text):
    key=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    keyCode=['7','8','9','10','11','12','13','14','15','16','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54']
    for k in range(len(key)):
        if text == key[k]:
            # print key[k], keyCode[k]
            #键盘输入
            self.driver.press_keycode(keyCode[k])
            time.sleep(5)
        else:
            pass
#与上面的方法配合使用,可以输入一个字符串值
def inputText(self,text):
    li = list(text)
    for i in li:
        enterText(self,i)