class Employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def give_raise(self,amount=1):
        self.salary += amount
        return self.salary

sbd = Employee('xuxu','40',30)
print('姓名：' + sbd.name + '\n' + '年龄：' + sbd.age + '\n' + '薪酬：' + str(sbd.salary) + '\n')

sbd.give_raise(10)
print('姓名：' + sbd.name + '\n' + '年龄：' + sbd.age + '\n' + '薪酬：' + str(sbd.salary) + '\n')