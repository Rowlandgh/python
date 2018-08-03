"""
open()的第二个实参:
 'r'只读 
 'w'写入 
 'a'附加
 'r+'读取和写入   
 省略时默认只读

"""

file_path = 'chapter_files\writer_msg.txt'       #假设写入的文件不存在，open()会创建它。           
with open (file_path,'w') as file_object:        #使用'w'时，如果文件已存在，python会在返回文件对象前清空文件。注意，会覆写内容。                 
    file_object.write('i love this code.\n')      #python只能将字符串写入文本文件，遇到数值数据时，先用str()转成字符串形式。
    file_object.write('i love that code.\n')
    file_object.write('i love all code.\n')        #写入多行

with open (file_path,'a') as file_object:        #以附加模式打开文件，写入到文件的行都将添加到末尾。如果文件不存在，python会创建。                
    file_object.write('u love this code too?\n')    
    file_object.write('maybe not?\n')

print('=========================================')

with open (file_path,'a') as f:
    f.write('lets begin:\n')
    while True:
        name = input('请输入你的名字,退出请按Q。')
        if name == 'q':
            break
        f.write(name + '\n')

