#coding:utf-8
__author__ = 'ljy'

#2019.10.13

# #1-------------try -except  --已知异常类型
#
# def calc(a,b):
#     try:
#         print(a/b)
#     except ZeroDivisionError:
#         print('除数不能为0')
#
# a = int(input('-'))
# b = int(input('-'))
# calc(a,b)


#2-------------try -except  --未知异常 BaseException和Exception：

def calc(a,b):
    try:
        print(a/b)
    except BaseException:
        print('除数不能为0')

a = int(input('-'))
b = int(input('-'))
calc(a,b)

#3-------------多重异常：挨个匹配except后的异常类型

def calc(a,b):
    try:
        print(a/b)
    except BaseException:
        print('除数不能为0')

a = int(input('-'))
b = int(input('-'))
calc(a,b)

