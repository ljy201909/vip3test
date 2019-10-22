# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.10.22

# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量

class soldier():

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return '士兵%s' % self.name

    def fire(self,guns):
        if guns.bullet > 0:
            print('士兵射击')
            guns.shoot()
        else:
            print('%s子弹不足，请装填子弹' % guns.name)
            guns.addBullet()



class gun():
    def __init__(self,name):
        self.name = name
        self.bullet = 0

    def __str__(self):
        return "一把枪：%s，有子弹%d颗" % (self.name,self.bullet)

    def addBullet(self):
        self.bullet = self.bullet + 30
        print('子弹已装满！')

    def shoot(self):
        self.bullet = self.bullet - 1
        print('此时枪中还剩',self.bullet,'颗子弹')

g = gun('AK47')
print(g)

a = soldier('瑞恩')
print(a)
a.fire(g)
a.fire(g)
a.fire(g)
