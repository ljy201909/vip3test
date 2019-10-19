# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.10.19


#1---导入
import requests,json

#发送Post请求

urlstr = 'https://www.wanandroid.com/user/login'

data = {'username':'lijingying','password':'123456'}

#2---发送请求
r = requests.post(url=urlstr,data=data)
print('***',r.text)
print('***',r.cookies)
print('***',r.headers)

#获取上次请求放回的response中的cookie，传递给下次请求
cookie = r.cookies

#携带cookie发送请求
r2 = requests.get('https://www.wanandroid.com/lg/todo/list/0',cookies = cookie)
print('***',r2.text,r2.status_code)

