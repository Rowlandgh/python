bicycles = ['giant','美利达','凤凰','大航']
print(bicycles)

bicycles = ['giant ','美利达','凤凰','大航']
print(bicycles[1])
print(bicycles[0].title())
print(bicycles[-1])


bicycles = ['giant ','美利达','凤凰','大航']
msg="我有一辆"+bicycles[0].title()+"。"
print(msg)


bikes=['Honda','Suzuki','Yamaha','Kawasaki']
print(bikes)
print('使用-1时总是list的最后一个元素：'+ bikes[-1])

bikes[1]='BMW'
print(bikes)

bikes=['Honda','Suzuki','Yamaha','Kawasaki']
print(bikes)

bikes.append('Ducati')
print('新添加的元素会放到列表的末尾' + str(bikes))

bikes = []
bikes.append('本田')
bikes.append('铃木')
bikes.append('雅马哈')
bikes.append('川崎')
print(bikes)

bikes = ['no1','no2','no3']
bikes.insert(0,'no0')
print(bikes)

person=['nice1','nice2','bad3','nice4']
print(person)
del person[2]
print(person)

bikes=['Honda','Suzuki','Yamaha','Kawasaki']
print(bikes)
poped_bikes=bikes.pop()   #pop()删除list末尾的元素，并可接着使用它的值
print(poped_bikes)

bikes=['Honda','Suzuki','Yamaha','Kawasaki']
favorit_bike = bikes.pop(3)    #pop()只能是索引号
print ('我最喜欢'+ favorit_bike +'.')

bikes=['Honda','Suzuki','Yamaha','Kawasaki']
bikes.remove('Suzuki')
print(bikes)

bikes=['Honda','Suzuki','Yamaha','Kawasaki']
too_low=bikes[1]
bikes.remove(too_low)  #remove的参数只能是list成员名或变量，不能是索引号。
print(bikes)

