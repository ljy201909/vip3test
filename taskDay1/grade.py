#coding:utf-8
__author__ = 'ljy'


a = int(input('please input >>'))
if 90<=a<=100 :
    print('等级为A')
elif 80<=a<90:
    print('等级为B')
elif 70<=a<80:
    print('等级为C')
elif 60<=a<70:
    print('等级为D')
elif 0<=a<60:
    print('等级为E')
else:
    print('请输入0-100的整数')
