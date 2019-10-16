# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.10.16

# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量

class soldier():

    def __init__(self,name,gun,bulletMax,bullet):
        self.name = name
        self.gun = gun
        self.bulletMax = bulletMax
        self.bullet = bullet

    def soldierPrint(self):
        print('士兵',self.name,end=',')

    def gunPrint(self):
        print('有一把',self.gun)

    def bulletPrint(self):
        print('枪中一共有',self.bulletMax,'颗子弹',end='，')
        print('现在还剩',self.bullet,'颗')

    def shoot(self):
        if self.bullet == 0:
            print('没子弹了！！！请装填子弹！！！')
        else:
            self.bullet = self.bullet - 1
            self.soldierPrint()
            self.gunPrint()
            self.bulletPrint()

    def addBullet(self):
        if self.bullet == self.bulletMax:
            print('枪中子弹已装满，可以去射击了')
        else:
            self.bullet = self.bullet + 1
            self.soldierPrint()
            self.gunPrint()
            self.bulletPrint()

def dataInput():
    name = input('请输入士兵姓名：')
    gun = input('请输入枪支型号：')
    bulletMax = int(input('请输入枪支子弹装填上限：'))
    bullet = int(input('请输入枪支当前子弹数：'))
    T = (name,gun,bulletMax,bullet)
    return T

A1 = dataInput()
a = soldier(A1[0],A1[1],A1[2],A1[3])
a.soldierPrint()
a.gunPrint()
a.shoot()
a.addBullet()



