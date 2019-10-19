# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.10.19

#1---导入
import requests

#发送Post请求

urlstr = 'https://www.wanandroid.com/user/login'

data = {'username':'lijingying','password':'123456'}

#初始化session对象
s = requests.session()

#2---通过session对象发送请求，#服务器配置在本地的cookie会保存在本地
r = s.post(url=urlstr,data=data)

#通过session继续发送post请求，自动携带上一个请求返回的cookie
r2 = s.get('https://www.wanandroid.com/lg/todo/list/0')

print('****',r2.text)
print('***',r.text)
