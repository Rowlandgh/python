def users(names):
    for name in names:
        print('hello '+ name)
namelist = ['xuxu','liujing','hezhenjie','luoweiran']           #向函数传递列表
users(namelist)         


unprint_sth = ['xuxu','liujing','hezhenjie','luoweiran']
printed_sth = []

def print_names(unprint_sth,printed_sth):
    while unprint_sth:
        now_sth = unprint_sth.pop()                                #在函数中修改列表
        print(now_sth + ' is printing,please wait.\n')
        printed_sth.append(now_sth)

def show_printed_names(printed_sth):
    print('This name are printed:')
    for name in printed_sth:
        print(name)

print_names(unprint_sth,printed_sth)
#print_names(unprint_sth[:],printed_sth)                    #这么写python会使用unprint_sth的副本，所以原列表不会受到函数的影响。
show_printed_names(printed_sth)

def make_string_1(*group):                # *号会生成一个名为group的空元祖，并将收到的值封装进去。
    print('元祖内有以下元素：')
    count = 1
    for unit in group:
        print(str(count) + ' : ' + unit)
        count += 1
make_string_1('传递一个实参')
make_string_1('传','多','个','实','参')


def make_string_2(num,*group):                #python先匹配位置实参和关键字实参，再把余下的实参收入最后一个形参(元祖)中。
    print('元祖内共有' + str(num) + '个元素：')
    count = 1
    for unit in group:
        print(str(count) + ' : ' + unit)
        count += 1
make_string_2 (1,'传递一个实参')
make_string_2 (5,'传','多','个','实','参')


def user_profile(name,age,**user_info):     #两个**号会创建一个名为user_info的空字典，并将收到的所有键-值对都封装到这个字典中。
    profile = {}         
    profile['姓名'] = name                      #新建一个键'姓名'，再把传入的name作为'姓名'的值存储。
    profile['年龄'] = age
    for key,value in user_info.items():         #遍历user_info的所有键-值对，并将每个对都加入到字典profile中。
        profile[key] = value
    return profile

final_profile = user_profile('xuxu',30,位置 = 'beijing',职位 = 'programmer')
print(final_profile)
final_profile = user_profile(name='xuxu',age=30,位置 = 'beijing',职位 = 'programmer')
print(final_profile)
