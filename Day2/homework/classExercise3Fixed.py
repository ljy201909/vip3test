# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.10.22

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
    def __init__(self,apartment,totalArea):
        self.apartment = apartment
        self.totalArea = totalArea
        self.residualArea = self.totalArea
        self.furniture = []

    def __str__(self):
        #return '房屋类型是：',self.apartment,'，总面积为：',self.totalArea,'平方米，剩余面积为：',self.residualArea,'平方米，家具有：',self.furniture
        return "房屋户型是：%s，总面积为：%0.01f平，剩余面积为：%0.01f平，家具有：%s" % (self.apartment,self.totalArea,self.residualArea,self.furniture)


    def addFurniture(self,furnitures):
        if(self.residualArea < furnitures.furnitureArea):
            print('放不下了!')
        else:
            self.residualArea = self.residualArea - furnitures.furnitureArea
            self.furniture.append(furnitures.name)
            print('给房子添加家具：%s' % furnitures.name)


class Furniture():
    def __init__(self,name,furnitureArea):
        self.name = name
        self.furnitureArea = furnitureArea

    def __str__(self):
        return '家具：%s，占地%0.01f平方米' % (self.name,self.furnitureArea)

a = House('三室一厅',120.0)
print(a)

f1 = Furniture('床',4)
f2 = Furniture('衣柜',2)
f3 = Furniture('餐桌',1.5)
print(f1)
print(f2)
print(f3)
a.addFurniture(f1)
a.addFurniture(f2)
a.addFurniture(f3)
print(a)