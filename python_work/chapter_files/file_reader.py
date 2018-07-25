with open('D:\python_work\chapter_files\pi_digits.txt') as file_object:         # with作用是让python选择关闭文件的合适时机。
                                                                                #也可以使用close()来手动关闭，但容易出错。
                                                                                #注意，使用with时，open()返回的文件对象只在with代码块内可用。
    contents = file_object.read()                                               #所以read()读取对象并存在contents中，这样在外部也可以使用。
    print(contents)


file_path = 'chapter_files\pi_digits.txt'                           # 也可以使用以python工作根目录为基准的相对路径
with open (file_path) as file_object:                               # 先把路径存到变量中再调用
    contents = file_object.read()
    print(contents)

print('\n===================================\n')

file_path = 'chapter_files\pi_digits.txt'                
with open (file_path) as file_object:                             
    for line in file_object:
        print(line.rstrip())                                        #使用rstrip消除了空格


file_path = 'chapter_files\pi_digits.txt'                
with open (file_path) as file_object:                             
    lines = file_object.readlines()                         #用readlines()读取文件的每一行并存成list形式，再把list存到lines变量中
for line in lines:                                          #在with代码块以外使用lines变量
    print(line.rstrip())                                       

print('\n===================================\n')

file_path = 'chapter_files\pi_digits.txt'                
with open (file_path) as file_object:                             
    lines = file_object.readlines() 
string_1 = ''
for line in lines:
    string_1 += line.rstrip()                               #这里使用了文件的内容，把lines中的每一行都加入字符串中。
print(string_1)
print(len(string_1))

print('\n' + string_1[:20] + '......')                      #显示字符串的前20个字符(切片)

print('\n===================================\n')

file_path = 'chapter_files\pi_digits_long.txt'
with open(file_path) as file_object:
    lines = file_object.readlines() 
string_1 = ''
for line in lines:
    string_1 += line.rstrip()
print(string_1)
num = input('请输入你的生日：(比如1980年1月1日可输入19800101)')
if num in string_1:
    print('你的数字竟然恰好在100个随机数内！')
else:
    print('你的数字没有在随机数中，很遗憾哦！')
