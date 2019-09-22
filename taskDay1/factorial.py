#coding:utf-8
__author__ = 'ljy'

#10的阶乘
fac1 = 1

i = 1
while (i <= 10):
    fac1 = fac1 * i
    i = i + 1

print(fac1)

#任意输入一个正整数，求阶乘
fac2 = 1
j = 1
n = int(input('please input a number >>'))
if (n <= 0):
    print('请输入正整数')
else:
    while (j <= n):
        fac2 = fac2 * j
        j = j + 1
if (fac2 > 1):
    print(fac2)
