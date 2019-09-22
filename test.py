#coding:utf-8
__author__ = 'ljy'

'''
#赋值abcd，并打印类型
a = 5
b = 2.5
c = 'hello'
d = "hello world"


print(type(a))
print(type(b))
print(type(c))
print(type(d))


#输入两个字符，并打印两个字符和其类型
x,y = input('Please input a value:').split(',')
print('The value of a is :',x,y,type(x),type(y))

#print + format
print('xxx={},yyy={}'.format(x,y))

print("%d,%f,%s" % (a,b,c))

'''
#元组
'''
s = list(range(1,10))
i = list(range (1,1000))
#输出整个元组
print (s)
#输出倒数第3个元素
print (s[-3])
#输出值 468
print (s[3:8:2])

print (s[8:3:-2])
'''

# s1 = [10,1,2,3,7,1,2,4,5,6,8,1,2,3,9]
# s2 = ['a','b','c']
# #逆序存放
# s1.reverse()
# print (s1)
# print(s1.reverse())
# #排序存放
# s1.sort()
# print (s1)
#排序
#print(sorted(s1))
#插入
# s1.insert(3.303)
# s1.insert(6,666)
# s1.insert(8,66)
# print (s1)
#追加
# s1.append(77)
# print (s1)
# #连接两个列表
# s1.extend(s2)
# print(s1)
#删除制定元素
#print(s1.pop(3))
#删除指定元素第一次出现的值
# # s1.remove(2)
# #返回该值在列表中出现的次数：m.count(n) –返回元素n在列表中出现的次数
# print(s1.count(2))
# #返回列表中元素最大值：max(s)
# print(max(s1))
# #返回列表中元素最小值：min(s)
# print(min(s1))
# #长度：len(s) ---返回列表元素的个数
# print(len(s1))
# #删除：del s[n] ----删除s[n]，n为下标
# del s1[2]
# #获得元素的下标：s.index(n) -------得到元素n在列表中的下标
# print(s1.index(2))
# #清空列表：s.clear() --------清空列表
# # s1.clear()
# # print(s1)
# #in 和 not in ---用来检查是否在列表中
# if 3 in s1:
#     print('true')
#
# sl = [11,13,5,7,0,56,23,34,72]
# si = [66,67,68]
# #求该列表中的最大值，最小值及列表中一共有几个元素
# print (max(sl),min(sl),len(sl))
#
# #获取56元素在列表的位置
# print (sl.index(56))
#
# #追加元素7
# sl.append(7)
# print(sl)
#
# #删除元素0
# sl.pop(4)
# print(sl)
#
# #排序列表（由大到小）
# sl.sort()
# sl.reverse()
# print (sl)
#
# #将列表[66,67,68]与原列表组合
# sl.extend(si)
# print(sl)

#集合

# s = {1,3,2}
# s.add(4)
# print(s)
# s.add(4)
# print(s)
#
# # s.remove(5)
# # print(s)
#
# s.remove(3)
# print(s)
# s.discard(5)
# print(s)
# # s.clear()
# # print(s)
# if 2 in s:
#     print('true')
# else:
#     print('false')

# #字典
# # s={'a':10,'b':20,'c':15}
# #
# # s['d'] = 11
# # print(s)
# # print(s.keys())
# # print(s.values())
# # print(type(s.keys()))
# # print(s.items())
# # del s['a']
# # print(s)
# # s.clear()
# # print(s)

a = int(input('please input >>'))
if 90<=a<=100 :
    print('等级为A')
elif 80<=a<90:
    print('等级为B')
elif 70<=a<80:
    print('等级为C')
elif 60<=a<70:
    print('等级为D')
elif 0<=a<60:
    print('等级为E')
else:
    print('请输入0-100的整数')




s = [1,2,3,4,5,6,7,8,9,10]
b = int(input('please input >>'))
if b in s:
    print('b在列表中')
else:
    print(b+'不在列表中')