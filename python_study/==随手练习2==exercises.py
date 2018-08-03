#7-8
name_order = ['1','2','3','3','3']
name_finish = []
print(name_order)
print(name_finish)

while name_order:
    name_finish.append(name_order.pop())
print(name_order)
print(name_finish)

#7-9
print('3已从列表中完全消除.')
while '3' in name_finish:
    name_finish.remove('3')
print(name_finish)

#8-9
print('\n\n以下是#8-9的练习')

def transfer_name(old_names):                           #把现有列表传递给新列表
    print('old_names：\n' + str(sorted(old_names)))
    new_names = []
    while old_names:
    #for name in old_names:                                     #这里不能用for跟pop()配合使用，不知道为什么。
        tempname = old_names.pop()
        new_names.append(tempname)
    print('new_names：\n' + str(sorted(new_names)))
    return new_names

def change_name(namelist):                              #把现有列表的每个名字前都加上字符串
    changed_name = []
    while namelist:
        tempname = namelist.pop()
        tempname = 'MR.' + tempname
        changed_name.append(tempname) 
    return changed_name

testlist1 = ['xuxu','liujing','hezhenjie','luoweiran']
new_namelist = transfer_name(testlist1)
final_list = change_name(new_namelist[:])                   #使用了列表的副本操作，而不影响原表。
print('changed_names：\n' + str(sorted(final_list)))
print('new_names：\n' + str(sorted(new_namelist)))

#for name in new_names:
    