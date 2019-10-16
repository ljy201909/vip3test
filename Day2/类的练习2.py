#coding:utf-8
__author__ = 'ljy'

#2019.10.13

class Student():
    def __init__(self,name):
        self.name = name

    def study(self,kecheng):
        print(self.name,'学习',kecheng)


a = Student('小明')
a.study('数学')