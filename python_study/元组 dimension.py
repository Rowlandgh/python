dimension = (100,150,200,250,300)
print(dimension[0])
print(dimension[1])

for i in dimension:
    print(i)

dimension = (100,150)
print(dimension)      #只能整体修改元祖，不能单独修改其中的元素

dimension[0] = 50     #比如这样改元祖中的元素是不行的