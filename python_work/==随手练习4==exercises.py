from collections import OrderedDict                 #模块collections中的类OrderedDict的实例几乎与字典相同。
                                                    #区别在与记录了键-值对的添加顺序。

name_num = OrderedDict()                            #创建了OrderedDict类的一个实例（空的有序词典），并存到name_num中。
                                                    #所以没有使用{}，注意。
name_num['xuxu'] = '1'
name_num['liujing'] = '2'
name_num['hezhenjie'] = '3'
name_num['luoweiran'] = '4'

for name,num in name_num.items():
    print(name + "'s number is " + num)


from random import randint                          #模块random包含以各种方式生成随机数的函数                                  

class Die():
    def __init__(self,sides=6):
        self.sides = sides
    
    def roll_die(self):
        result = randint(1,self.sides)                       # randint 返回一个指定范围内的整数(包含1和6)
        print(result)

die_1 = Die(6)
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
print('==========')

die_1 = Die(10)
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()
die_1.roll_die()



#10-6
print('输入两个数，我来帮你做除法。')

while True:
    num_1 = input('请输入被除数：(输入q可退出)')
    if num_1.lower() == 'q':
        break
    num_2 = input('再输入除数：(输入q可退出)')
    if num_2.lower() == 'q':
        break
    try:                                            #处理有可能抛出的异常
        result = float(num_1) / float(num_2)
    except ZeroDivisionError:                       #处理异常状况
        print('你不能除0')
    except ValueError:
        print('你只能输入数字。')
    else:                                           #处理其它状况
        print(result)


