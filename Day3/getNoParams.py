# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.10.19

#1---导入
import requests

#发送GET请求

urlstr = 'https://blog.csdn.net/rainshine1190'

#2---发送请求
r = requests.get(url=urlstr)

print(r.text)