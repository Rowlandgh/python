def get_words_num(file_name):
    try:
        with open (file_name) as f_o:
            contents = f_o.read()              
    except FileNotFoundError:
        print(file_name + '不存在')
    else:
        words = contents.split()                      
        num_words = len(words)
        print(file_name + '共有' + str(num_words) + '单词')

file_name_1 = 'd:\\python_work\\english_sample_1.txt'
file_name_2 = 'd:\\python_work\\english_sample_2.txt'  
file_name_3 = 'd:\\python_work\\english_sample_3.txt'  
file_name_4 = 'd:\\python_work\\english_sample_4.txt' 
file_list = [file_name_1,file_name_2,file_name_3,file_name_4]
for files in file_list:                                             #处理多个文件                                     
    get_words_num(files)  




def get_words_num(file_name):
    try:
        with open (file_name) as f_o:
            contents = f_o.read()              
    except FileNotFoundError:
        pass                                                        #使用pass让python什么都不做
    else:
        words = contents.split()                      
        num_words = len(words)
        print(file_name + '共有' + str(num_words) + '单词')
 
file_name_1 = 'd:\\python_work\\english_sample_1.txt'  
file_name_3 = 'd:\\python_work\\english_sample_3.txt' 
file_list = [file_name_1,file_name_3]
for files in file_list:                                                               
    get_words_num(files)  