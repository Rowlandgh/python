from name_function import get_formatted_name
print('Enter q at any time to quit.')
while True:
    first = input('please enter the first name.')
    if first == 'q':
        break
    last = input('please enter the last name.')
    if last == 'q':
        break
    formatted_name = get_formatted_name(first,last)
    print(formatted_name)