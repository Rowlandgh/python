import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = 'which language did you learn to speak first?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_responses('english')
        self.assertIn('english',my_survey.responses)

    def test_store_three_responses(self):
        question = 'which language did you learn to speak first?'
        my_survey = AnonymousSurvey(question)
        responses = ['english','chinese','spainish']
        for response in responses:
            my_survey.store_responses(response)
        for response in responses:
            self.assertIn(response,my_survey.responses)
unittest.main()