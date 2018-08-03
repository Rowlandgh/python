#9-6
class Icecream_shop():
    def __init__(self,favors,num,list):
        self.all_favors = favors
        self.num = num
        self.list = ['香草','巧克力','奶茶','五香','菠萝']

    def icecream_des(self):
        print(self.all_favors + self.num + '我最喜欢')
    
    def show_list(self):
        print(self.list)

ic1 = Icecream_shop('香草','五号',[])
ic1.icecream_des()
ic1.show_list()

class Users():
    def __init__(self,name,password):
        self.name = name
        self.password = password

class Admin(Users):
    def __init__(self,name,password):
        super().__init__(name,password)
        self.rights = ['可以添加用户','可以删除用户','可以禁言用户','可以通知用户']

    def show_rights(self):
        print(self.rights)

new_admin = Admin('luoweiran','1314')
new_admin.show_rights()

