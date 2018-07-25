cars = ['bmw','audi','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

cars = ['bmw','audi','subaru','toyota']
for car in cars:
    if car != 'subaru':
            print('这辆车不是斯巴鲁')
    else:
        print(car.title())
