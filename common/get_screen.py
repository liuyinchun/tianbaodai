#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
author:liuyinchun
datetime:2018/3/23
'''
import os,sys

#截图
def getScreen(self,pic_name):
    #绝对路径
    #f = list(sys.argv[0].split('.'))[0]  #获取当前脚本目录名,不带文件名
    #文件名
    #f1 = os.path.realpath(__file__)     #获取当前脚本目录全名,带文件名
    #f2 = os.path.basename(__file__)     #获取当前脚本文件名

    #在执行所有用例时都需要粘贴,
    #pic_name = list(os.path.basename(__file__).split('.'))[0]    #获取脚本文件名,不带后缀  作为图片名


    filePath = os.path.split(os.path.realpath(sys.argv[0]))[0]    #获取当前脚本目录名上一级 输出G:liu/tianbaodai

    filename = filePath+"\\getscreen\\"+pic_name+".png"   #拼接图片路径

    self.driver.get_screenshot_as_file(filename)       #截图并保存

