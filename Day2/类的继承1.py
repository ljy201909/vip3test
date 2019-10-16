#coding:utf-8
__author__ = 'ljy'

#2019.10.13

class Animal:
    def __init__(self,color):
        self.color = color

    def eat(self):
        print('------吃')
    def drink(self):
        print('------喝')

class Dog(Animal):
    def __init__(self,color,size):
        Animal.__init__(self,color)
        self.size = size

    def bark(self):
        print(self.color,'颜色的',self.size,'型的狗------汪汪叫')

class Cat(Animal):
    def __init__(self,color):
        Animal.__init__(self,color)

    def catch(self):
        print('------抓老鼠')

wangcai = Dog('黑','大')
wangcai.eat()
wangcai.bark()

tom = Cat('黑')
tom.catch()


