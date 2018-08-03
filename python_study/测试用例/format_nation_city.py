#11-1
def nation_city(nation,city,num=''):
    if num:
        final_nation_city = city + ',' + nation + ',' + str(num)
    else:
        final_nation_city = city + ',' + nation
    return final_nation_city

nation_city('china','beijing',5)