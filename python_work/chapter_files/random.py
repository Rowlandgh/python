from random import randint 

count = 0 
string_1 = ''
while count <= 100:
    ran_num = randint(1,100)
    string_1 += str(ran_num)
    count += 1
print(string_1)
