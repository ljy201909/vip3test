#coding:utf-8
__author__ = 'ljy'

#2019.10.13

#设计一个计算器，输入两个数，自动实现加减乘除（进阶：根据用户输入的计算符号计算结果）
def add(a,b):
    try:
        print('两数之和为:',a+b)
    except ValueError:
        print('请输入两个整数')

def sub(a,b):
    print('两数之差为:',a-b)

def mult(a,b):
    print('两数之积为:',a*b)

def div(a,b):
    if(b == 0):
        print('除数不能为0')
    else:
        print('两数之除为:',a/b)
try:
    a=int(input('请输入一个数：'))
except BaseException:
    print('请输入一个整数')
c=input('请输入一个运算符号：')
b=int(input('请输入另一个数：'))
if c == '+':
    add(a,b)
elif c == '-':
    sub(a,b)
elif c == '*':
    mult(a,b)
elif c == '/':
    div(a,b)
else:
    print('不支持此运算')

# #例:传参必须是必变
# def add_end(L=[]):
#     L.append('END')
#     return L
# print(add_end())
# print(add_end())


# #可变参数
# def calc(*numbers):
#     print(*numbers)
#     print(numbers)
#     sum = 0
#     for n in numbers:
#         sum += n
#     return sum
#
# num = [1,2,3]
# print(calc(*num))


# #关键字参数
# def person(name,age,**kwargs):
#     print('name:',name,'age:',age,kwargs)
#
# extra = {'city':'Beijing','job':'Engineer'}
# person('xiaoming',25,sex='male')