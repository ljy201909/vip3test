# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.10.15

#打印小猫爱吃鱼，小猫要喝水
class Cat():
    def __init__(self,name):
        self.name = name

    def drink(self,drinks):
        print(self.name,'要喝',drinks)
    def  eat(self,food):
        print(self.name,'爱吃',food)

a = Cat('小猫')
a.eat('鱼')
a.drink('水')