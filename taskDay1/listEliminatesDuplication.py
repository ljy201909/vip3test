#coding:utf-8
__author__ = 'ljy'

#列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表

s = [1,2,3,4,3,4,2,5,5,8,9,7]
i = 0
j = 1
while (i < len(s)):
    while (j < len(s)):
        if (s[i] == s[j]):
            s.pop(j)
        j =j + 1
    i = i + 1
    j = i + 1

print(s)
