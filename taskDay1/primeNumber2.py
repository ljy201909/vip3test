#coding:utf-8
__author__ = 'ljy'

a = int(input('please input >>'))
t = []

for i in range(2,a+1):
    for j in range(i-1,1,-1):
        if(i % j ==0):
            break
    else:
        t.append(i)

print(t)