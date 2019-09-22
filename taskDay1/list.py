#coding:utf-8
__author__ = 'ljy'

s = [1,2,3,4,5,6,7,8,9,10]
b = int(input('please input >>'))
if b in s:
    print(str(b) + '在列表中')
else:
    print(str(b) + '不在列表中')