name="XuXu"
Sentence='"Liu Jing is a good person"'
print("这是2.3的练习：")
print(name+"\tonce said:"+Sentence) 

guest_list=['xuxu','liujing','hezhenjie','wangxinye','zhangxia','ganlin']
liujing=guest_list[1]
wangxinye=guest_list[3]
guest_list.remove(liujing)
guest_list.remove(wangxinye)
print("这是3.4的练习：")
print(guest_list) 

guest_list.append('zhaokun') 
guest_list.insert(2,'zhaoxu')
print(guest_list)

del_guest_list = guest_list.pop(4)
print(guest_list)

guest_list.remove('zhangxia')
print(guest_list)

del_guest_list = guest_list[3]
guest_list.remove(del_guest_list)
print(guest_list)

del_guest_list_array = [guest_list.pop(),guest_list.pop(),guest_list.pop()]
print('删除的人名单是 ' + str(del_guest_list_array))
print(guest_list)

#4-3   4-4
for i in range(1,11):
    print(i)

#4-5
number = [i for i in range(1,1000001)]
print(max(number))
print(min(number))
print(sum(number))

#4-6
squares = list(range(1,20,2))
print(squares)

#4-7
squares = list(range(3,31,3))
for a in squares:
    print(a)

#4-8   
for c in range(1,11):
    b = c**3
    print(b)

#4-9
squares = [b**3 for b in range(1,11)]
print(squares)


