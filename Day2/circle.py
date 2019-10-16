#coding:utf-8
__author__ = 'ljy'

#2019.10.13

# #练习：计算1+2+3+4……+100的和
# a = 1
# s = 0
# while a <= 100:
#     s = s + a
#     a = a + 1
#
# print('1+2+3+4……+100的和为：' + str(s))
#
#
# #例1：
# for i in range(1,5):
#     if i==3:
#         continue
#         print(i)
#     else:
#         print(i)
#

#100以内能被3整除的数
# ss = []
# i = 1
# while i <= 100:
#     if(i % 3 == 0):
#         ss.append(i)
#     i = i + 1
# print(ss)

s = [1,2,3,4]
s1 = [str(i) for i in s]
print(s1)
print('+'.join(s1))

