def get_formatted_name(firstname,lastname):
    full_name = firstname + ' ' + lastname
    return full_name.title()

def get_formatted_name_2(firstname,middlename,lastname):
    full_name_2 = firstname + ' ' + middlename + ' ' + lastname
    return full_name_2.title()

    
def get_formatted_name_3(firstname,lastname,middlename=''):
    if middlename:
        full_name_3 = firstname + ' ' + middlename + ' ' + lastname
    else:
        full_name_3 = firstname + ' ' + lastname
    return full_name_3.title()
