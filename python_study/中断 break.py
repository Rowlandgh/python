msg = '输入你去过的城市，我将为你记录下来！'
msg += '\n输入quit可以退出。'

citylist = []
while True:     # while true打头的循环会一直进行直到遇到break
    city = input(msg)
    if city == 'quit':
        break
    else:
        citylist.append(city)
        print('你可以继续增加城市，或者输入quit来退出。')
print('你去过下面的城市:\n' + str(citylist))

