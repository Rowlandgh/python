#10-1 10-2

file_path = 'chapter_files\who love whoelse.txt'
with open(file_path) as file_object:
    file_1 = file_object.read()                   #读取整个文件           
    print(file_1)

with open(file_path) as file_object:                
    print(file_object.readlines())               #读取文件的每一行

with open(file_path) as file_object:                
    lines = file_object.readlines()               
    print(lines)
for line in lines:                              #存成列表，在with外打印
    print(line)

with open(file_path) as file_object:                
    string_1 = ''
    lines = file_object.readlines()              
for line in lines:                             
    string_1 += line
print('\n\n\n' + string_1)
string_1 = string_1.rstrip()
string_2 = string_1.replace('i','u')
print('\n\n\n' + string_2)