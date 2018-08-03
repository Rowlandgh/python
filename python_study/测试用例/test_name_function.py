import unittest                                     #编写测试用例时，先导入模块unittest和要测试的函数
from name_function import get_formatted_name_3
""" from name_function import get_formatted_name
class Name_test_case(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('luo','weiran')
        self.assertEqual(formatted_name,'Luo Weiran')
unittest.main()

from name_function import get_formatted_name_2
class Name_test_case(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name_2('luo','weiran')
        self.assertEqual(formatted_name,'Luo Weiran')
unittest.main() """

class Name_test_case(unittest.TestCase):            #再创建一个继承unittest.TestCase的类
    def test_first_last_name(self):               
        formatted_name = get_formatted_name_3('liu','jing')
        self.assertEqual(formatted_name,'Liu Jing')         #assertEqual断言方法
    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name_3('luo','ran','wei')
        self.assertEqual(formatted_name,'Luo Wei Ran')
unittest.main()


#assertEqual( a, b) 核实 a == b 
#assertNotEqual( a, b) 核实 a != b 
#assertTrue( x) 核实 x 为 True 
#assertFalse( x) 核实 x 为 False 
#assertIn( item, list) 核实 item 在 list 中
#assertNotIn( item, list) 核实 item 不在 list 中
