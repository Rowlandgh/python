import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.sbd = Employee('xuxu','40',30)
        self.info = self.sbd.name + self.sbd.age + str(self.sbd.salary)
    
    def test_give_default_raise(self):
        self.sbd.give_raise()
        self.assertEqual = (self.info,"xuxu4031")


    def test_give_custom_raise(self):
        self.sbd.give_raise(10)
        self.assertEqual = (self.info,"xuxu4040")

unittest.main()