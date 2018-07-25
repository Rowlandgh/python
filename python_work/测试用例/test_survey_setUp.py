import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):                                                    #使用setUp()只需创建对象一次，并在每个测试方法中使用。
        question = 'which language did you learn to speak first?'
        self.my_survey = AnonymousSurvey(question)                      #创建一个调查对象，变量名前加self(即存在属性中)，即可在这个类的任何地方使用。
        self.responses = ['english','chinese','spainish']               #创建一个答案列表，变量名前加self(即存在属性中)，即可在这个类的任何地方使用。
    
    def test_store_single_response(self):
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_responses(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)
unittest.main()