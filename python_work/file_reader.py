with open ('D:\python_work\chapter_files\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open ('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

''' 
r  只读（默认）

r+  读写

w  写入  先删除原文件，再重新创建，如果文件不存在则创建

w+  读写  先删除原文件，再重新创建，如果文件不存在则创建，可以写入输出

a 写入  在文件末尾追加新的内容，文件不存在，则创建

a+读写  在文件末尾追加新的内容，文件不存在，则创建

b  打开二进制的文件，可与r,w,a,结合使用
 
u  支持所有换行符号 \r\n
 '''