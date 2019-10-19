# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.10.19

#1---导入
import requests

#发送GET请求

urlstr = 'https://www.wanandroid.com/article/query?k=Android'

#参数
payload = {'k':'Android'}

#2---发送请求
r = requests.get(url=urlstr)

#3---获取结果
print(r.text)
print(r.status_code)