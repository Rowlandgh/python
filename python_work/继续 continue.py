num = 0
while num < 10:
    num += 1
    if num % 2 == 0:           #遇到偶数就跳过print.结果只打印了奇数。
        continue
    print(num)

msg1 = '\n请输入你的年龄:\n'
msg1 += '输入quit可以立即退出测试\n'
price10 = '5元'
price50 = '10元'
price100 = '8元'
cont = 0
active = True
while active == True:
    if cont == 5:
        active == False
        print('\n5次测试机会已用尽。退出完毕。')
        break
    age = input(msg1)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age <= 10:
            print(str(age) + '岁的票价是' + str(price10))
            cont += 1
            continue
        elif age>10 and age<50:
            print(str(age) + '岁的票价是' + str(price50))
            cont += 1
            continue
        else:
            print(str(age) + '岁的票价是' + str(price100))
            cont += 1
            continue
