from survey import AnonymousSurvey
question = 'which language did you learn to speak first?'
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print('enter q to quit anytime.\n')
while True:
    response = input('language:')
    if response == 'q':
        break
    else:
        my_survey.store_responses(response)

print('Thank you for take part in my survey!')
my_survey.show_results()
