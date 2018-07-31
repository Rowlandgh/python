import os

#path = os.getcwd()
#print(path)
def scan_folder():
    with open('C:\\Users\\kingsoft\\Desktop\\cn_test\\cn\\111.csv', "r", encoding="utf-8") as f:
        contents = f.readlines()        #把文件存成列表形式，每一行成为列表的一个元素。
        #print(contents)
        for file_be_list in contents:    
            file_eachline = file_be_list.split(',')  #把每个元素(行)存成一个列表
            #print(file_eachline)
            #num = file_eachline.index('cn')
            #print(num)
            if 'cn' in file_eachline:
                cn_column_num = file_eachline.index('cn')
                print(cn_column_num)
            
            #print('完成：把每个元素存成一个列表')

            #num = lines.index('cn')
'''                 for line in lines:
                print(line)
                num = lines.index('cn') '''


'''                     
                print(num) '''



'''                 for line in enumerate(lines):  #找到cn是列表的第几个元素
                if line == "cn":
                    num = str(line)
                    print(num) '''
scan_folder()
