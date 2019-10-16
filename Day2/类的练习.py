#coding:utf-8
__author__ = 'ljy'

#2019.10.13

# class Person():
#
#     #方法
#     def eat(self,food):
#         print('吃',food)
#
#     def sleep(self):
#         print('睡觉')
#
# #实例化
# a = Person()
#
# #调用类中的方法
# a.sleep()
# a.eat('rice')

class Person():
    #初始化方法/构造方法，在实例化的时候自动被执行
    def __init__(self,name,sex):
        print('执行init方法')
        self.name = name
        self.sex = sex

    #方法
    def eat(self,food):
        print('吃',food)

    def sleep(self):
        print(self.name,'睡觉')

#实例化
a = Person('小明','男')

#调用类中的方法
a.sleep()
# a.eat('rice')

