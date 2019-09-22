#coding:utf-8
__author__ = 'ljy'

t = []

for i in range(2,10001):
    for j in range(2,i):
        if(i % j ==0):
            break
    else:
        t.append(i)

print(t)