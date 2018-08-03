class Car():
    def __init__ (self, name, color,num=0):     
        self.name = name
        self.color = color
        self.num = num

    def get_car_info(self):
        all_info = self.name + ' ' + self.color + ' ' + str(self.num)
        return all_info

    def num_increase(self,value):
        self.num += value


class E_car(Car):                               #创建子类时，父类必须包含在当前文件中，且位于子类的前面。定义子类时，必须在括号里指定父类的名称。
    def __init__ (self,name,color,num):         #方法__init__接受创建Car实例所需的信息
        super().__init__(name,color,num)        #super()将父类和子类关联起来。父类也叫超类superclass，因此得名。
                                                #这行代码调用E-car父类的方法__init__(),让E-car的实例包含父类的所有属性。
                                                #注意，这里的参数没有self。

e_car_1 = E_car('tesla','black','26')
print(e_car_1.get_car_info())

#######################################################

class E_car(Car):                              
    def __init__ (self,name,color,num):        
        super().__init__(name,color,num)    
        self.size = 'big'                           #为子类实例增加新的属性

    def get_car_size(self):                         #为E_car增加新的方法
        print('this Ecar size is ' + self.size) 
    
    def num_increase(self,value):                   #重写父类的num_increase方法
        self.num = value + self.num
                                          
e_car_1 = E_car('honda','red',1)
e_car_1.size = 'medium'                             #修改子类实例的属性
e_car_1.num_increase(2)                     
print(e_car_1.name)
print(e_car_1.color)
print(e_car_1.num)
print(e_car_1.get_car_size())


