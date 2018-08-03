class Car():
    def __init__ (self, name, color,num=0):     
        self.name = name
        self.color = color
        self.num = num

    def get_car_info(self):
        all_info = self.name + ' ' + self.color + ' ' + str(self.num) + '号'
        print(all_info)


class Car_type():                               #单独新建一个有关汽车‘类型’的实例Car_type()
    def __init__(self,car_type=500):
        self.car_type = car_type

    def car_type_des(self):
        print('this cars type is ' + str(self.car_type))
    
    def get_type(self):
        if self.car_type > 500:
            slogan = '好车'
        elif self.car_type <= 500:
            slogan = '差车'
        print('这是一辆' + slogan)

class E_car(Car):                           #父类Car()的子类
    def __init__ (self,name,color,num):        
        super().__init__(name,color,num)
        self.type = Car_type()              #把实例Car_type()作为子类E_car的一个属性，这行代码会创建一个新的Car_type实例，并存到属性self.type中
                                            #以后每当__init__方法被调用时，都会执行该操作。所以现在每个E-car实例都包含一个自动创建的Car_type实例。

car_1 = E_car('toyota','yellow',3)
print(car_1.name)                           #直接调用car_1的属性name
car_1.get_car_info()                        #直接调用car_1的方法get_car_info
car_1.type.car_type_des()                   #在实例car_1中查找type属性，并对其中的实例Car_type调用方法car_type_des
car_1.type.get_type()




