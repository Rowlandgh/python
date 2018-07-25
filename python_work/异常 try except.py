try:
    print(5/0)
except ZeroDivisionError:                           #捕获异常，可让程序继续执行。如果不去捕获，程序将中断。
    print('你不能除0')

print('输入两个数，我来帮你做除法。')

while True:
    num_1 = input('请输入被除数：(输入q可退出)')
    if num_1.lower() == 'q':
        break
    num_2 = input('再输入除数：(输入q可退出)')
    if num_2.lower() == 'q':
        break
    try:                                            #处理有可能抛出的异常
        result = float(num_1) / float(num_2)
    except ZeroDivisionError:                       #处理异常状况
        print('你不能除0')
    else:                                           #处理其它状况
        print(result)


file_name = 'd:\\fake_1.txt'           
try:
    with open (file_name) as f_o:
        contents = f_o.read()
except FileNotFoundError:
    print(file_name + '不存在')

print('===========================================')

file_name = 'd:\\python_work\\english_sample.txt'           
try:
    with open (file_name) as f_o:
        contents = f_o.read()                       #contents现在是一个长长的字符串
        print(contents)
except FileNotFoundError:
    print(file_name + '不存在')
else:
    words = contents.split()                        #split()以空格为分隔符将字符串拆成多个部分，并将这些部分都存到列表中。
    print(words)
    num_words = len(words)
    print('这个文件共有' + str(num_words) + '单词')