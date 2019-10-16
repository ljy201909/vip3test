# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.10.15

# 3、摆放家具
# 需求：
# 1）.房子有户型，总面积和家具名称列表
#    新房子没有任何的家具
# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
# 3）.将以上三件家具添加到房子中
# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表

class House():
    def __init__(self,apartment,totalArea,furniture):
        self.apartment = apartment
        self.totalArea= totalArea
        self.furniture = furniture

    def initial(self):
        residualArea = self.residualAreaCount()
        print('房屋户型为',self.apartment,end='，')
        print('房屋面积为',self.totalArea,'平方米',end='，')
        print('家具有',self.furniture,end='，')
        print('房屋剩余面积为', residualArea, '平方米')

    def furnitureArea(self):
        f = {'床': 4.0, '衣柜': 2.0, '餐桌': 1.5}
        return f

    def residualAreaCount(self):
        f = self.furnitureArea()
        residualArea = self.totalArea
        for i in self.furniture:
            residualArea = residualArea - f[i]
        return residualArea

    def addFurniture(self,name):
        f = self.furnitureArea()
        self.furniture.append(name)
        print('搬入家具',name,end='，')
        self.initial()


a = House('一室一厅',40.0,[])
a.addFurniture('床')
a.addFurniture('衣柜')
a.addFurniture('餐桌')


