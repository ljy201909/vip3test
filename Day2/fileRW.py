#coding:utf-8
__author__ = 'ljy'

#2019.10.13

#读A文件中的数字，在B文件中按顺序输出
with open('E:\code\\vip3test\data1.txt','r') as f:
    #读取文件内容
    s = f.readlines(0)
    #去除列表中\n
    L = []
    for i in s:
        L.append(i.replace("\n",''))
    #将列表中str转换成int
    L = [int(i) for i in L]
    #排序
    L.sort()

with open('E:\code\\vip3test\data2.txt','w+') as y:
    #将L转换成str
    L = [str(i) for i in L]
    #将L写入data2
    for i in L:
        y.write(i+"\n")

    y.seek(0)
    print(y.read())