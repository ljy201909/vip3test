#coding:utf-8
__author__ = 'ljy'

s = []
i = 1
while (i <= 100):
    if(i % 3 == 0):
        s.append(i)
    i = i + 1
print(s)


a = int(input('please input a number >>'))
b = int(input('please input another number >>'))
t = []
if a >= b:
    j = b
    b = a
    a = j

while (a <= b):
    if(a % 3 == 0):
        t.append(a)
    a = a + 1

print(t)