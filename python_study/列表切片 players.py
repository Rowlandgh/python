#切片
players = ['p1','p2','p3','p4','p5','p6','p7','p8']
print(players[0:4])
print(players[:4])    #与上一个等价
print(players[3:])
print(players[-3:])

print('以下是前4个P：')
for player in players[:4]:
    print(player.title())

my_food = ['apple','pear','banana']
your_food = my_food[:]       #进行了复制
your_food.append('orange')
print(my_food)
print(your_food)

my_num = list(range(1,11))
your_num = my_num[:5]
for i in my_num:
    print(i)
for o in your_num:
    print(o)
your_num.append(list(range(11,21)))
my_num = your_num
print(my_num)

my_food = ['apple','pear','banana']
for i in my_food:
    print(i)
