def hello_world(name):                  # name 称为形参--函数完成工作所需要的一项信息
    """这里展示一个简单的函数结构"""        # 文档字符串用3引号括起，python用它们来生成有关函数的文档。
    print('hello_world     by '+ name)
hello_world('Rowland')            # Rowland 称为实参--调用函数时传递给它的信息。

def lovers(who,whoelse):
    print(who + ' love ' + whoelse )                           #基于实参顺序而关联到形参，这种关联方式称为位置实参。
lovers('Lily','tom')


def lovers(who,whoelse):
    print(who + ' love ' + whoelse )                            #关键字实参。
lovers(whoelse = 'tom',who = 'Lily')

def lovers(who,whoelse = 'tom'):
    print(who + ' love ' + whoelse )                             
lovers(who = 'Lily')                                         #和lovers('Lily')是等效调用，python这里会按照位置实参处理。

def fullname(first_name,last_name,middle_name=''):             #把middle_name作为可选参数，要先给出默认值。
    if middle_name:
        fullname = first_name + ' ' + middle_name + last_name
    else:
        fullname = first_name + ' ' + last_name
    return fullname
yourname = fullname('liu','jing')
print(yourname.title())
hisname = fullname('xu','wei','heng')
print(hisname.title())

def teammate(name,sex,age=''):
    templist = {'name':name,'sex':sex}
    if age:
        templist['age'] = age
    return templist                                     #函数返回字典
final = teammate('xuhengwei','male','30')
print(final)

def get_fullname(first_name,last_name):
    full_name = first_name + last_name
    return full_name
while True:                                             #函数中的while循环
    f_name = input('请输入您的姓：\n输入q可以退出\n')
    if f_name == 'q':
        print('退出成功')
        break
    l_name = input('请输入您的名：\n输入q可以退出\n')
    if l_name == 'q':
        print('退出成功')
        break
    final = get_fullname(f_name,l_name)
    print('\n您的名字是：' + final)