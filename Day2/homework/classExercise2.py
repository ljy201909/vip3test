# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.10.15

# 2、小明爱跑步，爱吃东西。
# 1）小明体重75.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 4）小美的体重是45.0公斤

class Person():
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def initial(self):
        print(self.name,'的体重是',self.weight,'公斤')

    def eat(self):
        self.weight = self.weight + 1
        print(self.name,'的体重变为',self.weight,'公斤')

    def run(self):
        self.weight = self.weight - 0.5
        print(self.name,'的体重变为',self.weight,'公斤')

a = Person('小明',75.0)
b = Person('小美',45.0)
a.initial()
b.initial()
a.eat()
a.run()
b.eat()
b.run()
