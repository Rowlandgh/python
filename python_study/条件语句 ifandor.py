car = 'honda'
bike = 'Honda'
if car == bike:
    print("ok")
else:
    print("not ok")

if car.lower() == bike.lower():
    print("ok")
else:
    print("not ok")

cars = ['honda','toyota','bmw']
if 'honda' not in cars:
    print("ok")
else:
    print("not ok")

eat = [1]
if eat:                  #如果list不为空，返回true，否则返回false
    print(eat)
else:
    print('nothing to say')

shop = ['honda','bmw']
i_want = ['honda','subaru','toyota','bmw','audi','VasWogen','masubishi']
for want in i_want:
    if want in shop:
        print('i want '+want+'.')
    else:
        print('shop dont have '+want+'.')

nums = list(range(1,6))
for a in nums:
    if a==1:
        print('1st')
    elif a==2:
        print('2nd')
    elif a==3:
        print('3rd')
    elif a==4:
        print('4th')
    else:
        print('5th')
