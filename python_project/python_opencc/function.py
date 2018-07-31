from langconv import *

def translation(text):
    text = Converter('zh-hans').convert(text)
    return text

class File_contents():
    def __init__(self,file_name,file_path,new_file_path):
        self.path = file_path
        self.new_path = new_file_path
        self.name = file_name
        self.cn_column_num = 0

        old_file = open(self.path, "r", encoding="utf-8")
        new_file = open(self.new_path, "w", encoding="utf-8")

        self.file_in_list = old_file.readlines()            #把文件存成列表形式，每一行成为列表的一个元素。
        #print(self.file_in_list)
        self.firstline = self.file_in_list[0].strip('\n')        #把文件的第一行保存为一个列表，便于查表头。strip()是要去掉换行符。
        #print(self.firstline)
        self.firstline_in_list = self.firstline.split(',')       #把每个元素(行)存成一个列表，以，号为间隔。
        #print(self.firstline_in_list)
        if 'cn' in self.firstline_in_list:
            self.cn_column_num = self.firstline_in_list.index('cn')     #利用列表索引号定位cn列
            #print(self.cn_column_num)
        #print(self.file_in_list)
        for eachline in self.file_in_list:                          #每一行的内容eachline目前是字符串
            if 'cn' in eachline:
                new_file.write(eachline)                                    #跳过列头行
                continue
            else:
                eachline_in_list = eachline.split(',')                   #利用split函数先把每行转为列表形式
                cell_data = eachline_in_list[self.cn_column_num]          #找到cn列在当前行的内容
                #print('找到未翻译的内容： ' + cell_data)
                translated_cell_data = translation(cell_data)           #翻译繁体字符串
                #print('已翻译成： ' + translated_cell_data)
                new_file.write(eachline.replace(cell_data,translated_cell_data))    #用翻译好的替换原字符串，并写入新文件
        old_file.close()
        new_file.close()
