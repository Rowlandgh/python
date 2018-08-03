from module_2 import Car                    #从模块module_2中导入类Car

from module_2 import Car,Car_type,E_car     #导入多个类

import module_2                             #导入整个模块

from module_2 import *                      #导入所有类，不推荐，类名不清晰。

car_1 = E_car('toyota','yellow',3)          #导入后，下面可以直接调用了。
print(car_1.name)                           
car_1.get_car_info()                       
car_1.type.car_type_des()                   
car_1.type.get_type()

#也可以在一个模块中导入另一个模块，就不举例了。
def docstring_rule():
    """
    类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线。
    实例名和模块名都采用小写格式，并在单词之间加上下划线。
    对于每个类，都应紧跟在类定义后面包含一个文档字符串。

    文档字符串的惯例是一个多行字符串，它的首行以大写字母开始，句号结尾。
    第二行是空行，从第三行开始是详细的描述。

    每个模块也都应包含一个文档字符串，对其中的类可用于做什么进行描述。
    可使用空行来组织代码，在类中，可使用一个空行来分隔方法；而在模块中，可使用两个空行来分隔类。
    需要同时导入标准库中的模块和你编写的模块时，先编写导入标准库模块的import语句，再添加一个空行，
    然后编写导入你自己编写的模块的import语句。
    """
    print('说明如上')
    