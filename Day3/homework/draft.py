# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.10.19

#1---导入
import requests,json

#发送Post请求

urlstr = 'https://www.wanandroid.com/user/logout/json'

payload = {"username":"lijingying"}

#2---发送请求

r = requests.post(url=urlstr)

#3---获取结果
print(r.text)