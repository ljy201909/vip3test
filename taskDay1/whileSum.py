#coding:utf-8
__author__ = 'ljy'

sum1 = 0
i = 1
while (i <= 100):
    sum1 = sum1 + i
    i+= 1

print(sum1)

a = int(input('please input a number >>'))
b = int(input('please input another number >>'))
sum2 = 0
if a >= b:
    j = b
    b = a
    a = j

while (a <= b):
    sum2 = sum2 + a
    a+= 1

print(sum2)
