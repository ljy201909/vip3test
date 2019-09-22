#coding:utf-8
__author__ = 'ljy'

fac1 = 1

i = 1
while (i <= 10):
    fac1 = fac1 * i
    i = i + 1

print(fac1)


fac2 = 1
j = 1
a = int(input('please input a number >>'))
if (a <= 0):
    print('请输入正整数')
else:
    while (j <= a):
        fac2 = fac2 * j
        j = j + 1
if (fac2 > 1):
    print(fac2)
