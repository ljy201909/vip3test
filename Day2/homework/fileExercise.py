# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.10.16

# 目录下有这些文件：
# A1.txt
# B2.txt
# C1.doc
# D1.excel
# 任务1-将该目录下的文件按照后缀进行分类，然后分别新建且放入不同的文件夹内，比如txt文件放入txt目录下等

import os

#取出文件名
p = 'E:\code\\vip3test\Day2\homework\\fileExercise'
s = os.listdir(p)
print(s)

#取出文件类型,并放入一个集合
t = set()
for i in s:
    t.add(i.split('.')[1])
s1 = list(t)

#创建文件类型对应的文件夹
for i in s1:
    os.mkdir(p+'\\'+i)

#校验文件名与文件夹匹配，则在文件夹下创建一个文件
for i in range(len(s)):
    if s[i].split('.')[1] in s1:
        f = open(p+'\\'+s[i].split('.')[1]+'\\'+s[i],'w+')
        f.close()

