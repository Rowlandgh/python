for value in range(1,5):
    print(value)

num = list(range(1,5))
print(num)

even_num = list(range(2,20,2))
print(even_num)

square = []
for value in range(1,11):
    result = value**2
    square.append(result)
print(square)

square = []
for value in range(1,11):
    square.append(value**2)     #简化版
print(square)

nums = [1,2,3,4,5,6,7,8,9,0]
print(min(nums))
print(max(nums))
print(sum(nums))

squares = [a**2 for a in range(1,11)]      #【列表解析】方法，注意，for语句后没有：号
print(squares)



