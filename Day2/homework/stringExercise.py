# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.10.16

# 有这样一个文件，文件内容如下：
# Lucy|18601914231|男|19890218
# Jack|18101913132|女|19810311
# Tom|18201912533|女|19830713
# Lily|18301911734|男|19870210
# 任务1-找出所有L开头的人名
# 任务2-按照年龄进行排序
# 任务3-找出所有女性用户的信息


with open('E:\code\\vip3test\Day2\homework\data1.txt','r') as f:
    #将文件内容取出
    s = f.readlines(0)
#取出string末尾换行符
L = []
for i in s:
    L.append(i.replace("\n", ''))
#将L切片放入LL
LL = []
for i in range(len(L)):
    LL = LL + L[i].split('|')

# 任务1-找出所有L开头的人名
name = []
for i in range(0,len(LL),4):
    if LL[i][0] == 'L':     #LL[i]的首字母如果为L，就把名字放进name列表
        name.append(LL[i])
print('L开头的人名有：',name)

# 任务2-按照年龄进行排序
L1 = LL #因为会改变顺序，所以新定义一个列表，避免修改原有数据
age = []
for i in range(3,len(L1),4):
    for j in range(7,len(L1)-4,4):
        if(2019-int(L1[j][0:4]) > 2019-int(L1[j+4][0:4])): #如果前面的年龄大于后面的年龄，就互换这两个人的信息
            t = L1[j-3:j+1]
            L1[j-3:j+1] = L1[j+1:j+5]
            L1[j+1:j+5] = t
for i in range(0, len(L1), 4): #打印排序好的L1的数据
    age.append(L1[i])
print('四人按年龄排序为：',age)

# 任务3-找出所有女性用户的信息
sex = []
for i in range(2, len(LL), 4):
    if LL[i] == '女':
        sex.append(LL[i-2:i+2])
print('所有女性用户的信息为：',sex)
