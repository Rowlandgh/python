class Car():
    def __init__ (self, name, color,num=0):     
        self.name = name
        self.color = color
        self.num = num

    def get_car_info(self):
        all_info = self.name + ' ' + self.color + ' ' + str(self.num) + '号'
        print(all_info)


class Car_type():                              
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

class E_car(Car):                          
    def __init__ (self,name,color,num):        
        super().__init__(name,color,num)
        self.type = Car_type()  