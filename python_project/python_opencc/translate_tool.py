import os
from function import*

def translate_in_folder():
    work_folder = '.\\fan-cn'
    work_folder_file_list = os.listdir(work_folder)                           #os.listdir用于把文件夹下的所有文件名存成列表元素
    #print(work_folder_file_list)
    translated_folder = '.\\cn'
    for file_name in work_folder_file_list:
        file_path = os.path.join(work_folder,file_name)
        new_file_path = os.path.join(translated_folder,file_name)
        File_contents(file_name,file_path,new_file_path)

if __name__=="__main__":         #若当前模块是主模块，则此模块名字就是__main__，若此模块是被import的，则此模块名字为文件名字（不加.py）
    print('翻译开始，请耐心等待。。。。。。')
    translate_in_folder()
    print('翻译完成')
