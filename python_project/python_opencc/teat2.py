test_list = ['aaa','bbb','ccc','ddd','eee','fff',]
print(test_list)

num = test_list.index('ccc')
print(num)


test_str = '12,13,14,cn,13'
if ',cn' in test_str:
    print('yes')
new_str = test_str.replace('1','2')
print(new_str)

newlist = test_str.split(',')
print(newlist)
final = newlist.replace(newlist[3],'en')
print(final)
    