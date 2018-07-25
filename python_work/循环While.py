num = 1
while num <= 5 :
    print(num)
    num += 1        #num = num +1的简写


msg = "enter 'quit' to exit this program."
sth = ''                    #先设为空，使得首次执行while时有可供检查的东西
while sth != 'quit':
    sth = input(msg)
    if sth != 'quit':
        print('\n' + sth + ' is not correct order! please retry!\n')
print('Quit complete!')


msg = "enter 'quit' to exit this program."
msg2 = 'you input a wrong order! please retry!\n'
active = True
while active:               #使用active标志来控制while循环
    sth = input(msg)
    if sth == 'quit':
        active = False
    else:
        print(msg2)