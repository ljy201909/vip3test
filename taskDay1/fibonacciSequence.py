#coding:utf-8
__author__ = 'ljy'

#求斐波那契数列 1 2 3 5 8 13 ……

s = [1,2]
n = int(input('please input a number >>'))

i = 0
while (i < n-2):
    j = s[i+1] + s[i]
    s.append(j)
    i = i + 1

print(s)
