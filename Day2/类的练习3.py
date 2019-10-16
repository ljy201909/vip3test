#coding:utf-8
__author__ = 'ljy'

#2019.10.13

class Student():
    def __init__(self,sno):
        self.sno = sno

    def study(self,kecheng):
        print('学号为',self.sno,'的学生，学习',kecheng)

a = Student('001')

a.study('数学')