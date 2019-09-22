#coding:utf-8
__author__ = 'ljy'

t = []

for i in range(2,101):
    for j in range(i-1,1,-1):
        if(i % j ==0):
            break
    else:
        t.append(i)

print(t)