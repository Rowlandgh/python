dic = {'name':'xuxu','sex':'male','age':'twenty-eight','nation':'chinese'}
print(dic['name'])
print(dic['age'])
dic['race'] = 'han'
dic['politics'] = 'partymember'
print(dic)
del dic['politics']
print(dic)


liujing = {}
liujing['age'] = 35
liujing['number'] = 8
print(liujing)
liujing['age'] = 38
print(liujing)

print(dic['name'].title())

for key,value in dic.items():        #.items()返回键-值对照表
    print('key:' + key)
    print('value:' + value)

print(dic.keys())     #.keys()遍历所有的键（默认，不写也行）

boysnum = {'xuxu':'one','liujing':'two','luoweiran':'three','hezhenjie':'four'}
friend = ['xuxu','liujing']
for name in boysnum.keys():
    if name in friend: 
        print('i have a friend called ' + name.title())

if 'zhao kun' not in boysnum.keys():
    print('zhao kun is not a boy yet!')

boysnum = {'xuxu':'one','liujing':'two','luoweiran':'three','hezhenjie':'one'}
for name in sorted(boysnum.keys()):                      #使用sorted()可以按照首字母顺序排序
    print(name.title() + ', thx to join us.')

for num in boysnum.values():         #.values()遍历所有的值
    print('\n' + num)

for uniquenum in set(boysnum.values()):         # set可以去重
    print(uniquenum)
