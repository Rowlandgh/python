un_user = ['liujing','xuhengwei','hezhenjie']
yet_user = []
msg = '输入1继续\n'
while un_user:
    temp_user = un_user.pop()                   #pop()删除list末尾的元素，并可接着使用它的值
    print('正在注册'+ temp_user + '...')
    yet_user.append(temp_user)
    print('注册完毕')
    print('下列用户已完成注册' + str(yet_user))
    test = input(msg)
    if test != '1':
        break
print('所有用户已注册完毕。退出。')


men = ['xuxu','liujing','hezhenjie','xuxu','liujing']
print(men)

while 'xuxu' in men:                # 删除列表中所有'xuxu'元素
    men.remove('xuxu')
print(men)

