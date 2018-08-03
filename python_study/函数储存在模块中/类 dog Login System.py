class Dog():                            #类名首字母大写   #self形参必不可少，且必须在所有形参的前面。
    def __init__ (self, name, age):        #__init__表示这是一个特殊方法，每当用Dog创建实例时，python都会自动运行它。
        self.name = name
        self.age = age

    def sit(self):                      #在类中定义的函数和普通函数相比只有一点不同，就是第一参数永远是类的自身实体变量self
                                        #并且调用时不用传递该参数。
        print(self.name.title() + ' is now sitting.')

    def roll(self):
        print(self.name.title() + ' is now rolling.')


my_dog = Dog ('xuxu',5)

print('My dogs name is ' + my_dog.name)
print('My dogs age is ' + str(my_dog.age))

my_dog.sit()
my_dog.roll()

your_dog = Dog('liujing',8)         #可以创建任意数量的实例。
your_dog.roll()

your_dog.name = 'xuxu'              #直接修改实例的属性name
print(your_dog.name)



class Car():
    def __init__ (self, name, color):     
        self.name = name
        self.color = 'red'
        self.num = 10000

    def updata_num(self,new_num): 
        if new_num >= self.num:
            self.num = new_num
        else:
            print('你不能输入比当前数字小的值。')           #num代表里程，这里防止把里程数调小。

    def num_increase(self,value):                          #模拟了一个可以手动增加里程的方法
        self.num += value

car_1 = Car('audi',8)
print(car_1.color)

car_1.updata_num(50000)                #通过方法修改实例的属性num
print(car_1.num)

car_1.num_increase(5000)                #通过方法间接增加num的值
print(car_1.num)

#################################################################################################

def hello():
    while error_count > 0 and error_count < limit_num:
        user_name = input('请输入用户名(注册新用户输入new)：')
        if user_name == 'new':
            user_regist()
            break
        user_password = input('请输入密码：')
        login(user_name,user_password)

userlist = {'xuxu':'xuxu2009','liujing':'feishi','luoweiran':'spt'}     #现有用户列表 
class Add_users():
    def __init__(self,name,password,count=0):                           #注册新用户，创建一个实例。
        self.name = name
        self.password = password
        if name not in userlist.keys():
            userlist[self.name] = self.password                             #把用户加入用户列表
            print(userlist)                                                 
            self.count = len(userlist)                                      #统计用户数
            print('用户总数：' + str(self.count))
        else:
            print('您输入的用户名已被占用，请重新输入')
            user_regist()

error_count = 1
limit_num = 4
def login(user_name,user_password):
    global error_count
    global limit_num
    while error_count < limit_num:
        if user_name not in userlist.keys():
            print('您输入的用户名不存在\n')
            error_count += 1
            chance = limit_num - error_count
            if chance == 0:
                print('你的重试次数已用完，程序退出')
            else:
                print('你还可以尝试' + str(chance) + '次\n')
            break

        elif user_password != userlist[user_name]:
            print('您的密码输入错误\n')
            error_count += 1
            chance = limit_num - error_count 
            if chance == 0:
                print('你的重试次数已用完，程序退出')
            else:
                print('你还可以尝试' + str(chance) + '次\n')
            break
            
        else:
            error_count = 0
            print('欢迎你，' + user_name)
            print('===登录成功===，程序退出。')
            break

def user_regist():
    name = input('请输入新的用户名：')
    password = input('请输入密码：')
    user_1 = Add_users(name,password)
    print('新用户' + user_1.name + '注册成功')
    print('密码是' + str(user_1.password ))
    yon = input('是否立即登录？yes/no: ')
    if yon == 'yes':
        login(user_1.name,user_1.password)
    elif yon == 'no':
        hello()
    else:
        print('输入错误!!!')

print('\n=====欢迎来到TEST账户登录系统=====')
hello()




