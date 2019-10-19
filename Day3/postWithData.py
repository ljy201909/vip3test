# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.10.19

#1---导入
import requests,json

#发送Post请求

urlstr = 'https://www.wanandroid.com/user/login'

payload = {'username':'lijingying','password':'123456'}

#2---发送请求

r = requests.post(url=urlstr,data=payload)

#3---获取结果
print(r.text)
print(type(r.text))
#查看类型后为字典类型，r.json将response中返回的json处理成dict
print(type(r.json()))
#通过dict-key来访问对应的值
print(r.json()['data']['username'])
#判断返回的json数据是否有登录的用户名或通过正则表达式来获取
if r.json()['data']['username'] == payload['username']:
    print('登录成功')
#判断是否为管理员
if r.json()['data']['admin'] == False:
    print('不是管理员')
else:print('是管理员')