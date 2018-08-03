import module_1

module_1.make_string_1('aaa','bbb','ccc')               #使用import导入模块时，需要在模块名和函数名之间用.号分隔。

from module_1 import make_string_1,make_string_2        #可以同时调用多个函数，用,号分隔。

make_string_2('ccc','bbb','aaa')               #这里也无需声明模块名称和.号



import module_1 as md1                              #使用as为导入的模块取外号。
md1.make_string_1('aaa','bbb','ccc')

from module_1 import make_string_1 as m1 , make_string_2 as m2          #使用as为导入的函数取外号。
m1('aaa','bbb','ccc') 
m2('ccc','bbb','aaa')

from module_1 import *                              # *号可以导入模块中的所有函数。
make_string_1('aaa','bbb','ccc')  
make_string_2('ccc','bbb','aaa')  
