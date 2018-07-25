anwser = {}     #建立一个空字典
flag = True     #定义一个循环结束标记
msg = '是否需要输入更多人的信息？yes/no\n'
while flag:
    name = input('\n请输入您的名字：')
    sth = input('\n请输入您想得到的礼物：')

    anwser[name] = sth      #把键-值对应存入字典中
    temp = ''
    while temp != 'no' and temp != 'yes':
        temp = input(msg)
        if temp == 'no':
            flag = False
        if temp == 'yes':
            continue
        print('您输入的错误的指令，请重新输入。')
        
print('\n-----礼物列表-----\n')
for name,sth in anwser.items():
    print(name + '想要' + sth + '.')