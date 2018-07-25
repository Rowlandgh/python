def write_num(filename,strings):
    with open(filename,'a') as f_o:
        f_o.write(strings + '\n')                   #不知道为为什么写不进去

def get_num(filename):
    try:    
        with open(filename) as f_o:
            contents = f_o.read()
            the_num = contents.count('the')                 # count()计算特定的短语在字符串中出现了多少次。
            print(the_num)
            namelist = contents.split()
            num = len(namelist)
            str_temp = filename + '中有' + str(num) + '个单词'
            print(str_temp)
            write_num('english_sample_4.txt',str(num))
    except FileNotFoundError:
            print(filename + '不存在')             #pass

filename_1 = 'english_sample_1.txt'
filename_2 = 'english_sample_2.txt'
filename_3 = 'english_sample_3.txt'
filename_list = [filename_1,filename_2,filename_3]

for filename in filename_list:
    get_num(filename)