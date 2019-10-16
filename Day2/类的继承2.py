#coding:utf-8
__author__ = 'ljy'

#2019.10.13

class Person():
    def __init__(self,name):
        self.name = name

    def namePrint(self):
        print('名字是',self.name,end=',')

    def eat(self):
        print('吃饭')

class Teacher(Person):
    def __init__(self,name,gh):
        Person.__init__(self,name)
        self.gh = gh

    def ghPrint(self):
        print('工号为',self.gh,'的老师',end='，')

    def teach(self,course):
        print('教',course,'课')

    def work(self,company,salary):
        print('在',company,'上班，一个月工资',salary)

a = Teacher('张三','001')
a.ghPrint()
a.teach('数学')
b = Teacher('李四','002')
b.ghPrint()
b.work('实验中学',3000.00)
c = Teacher('王五','003')
c.namePrint()
c.ghPrint()
c.eat()
