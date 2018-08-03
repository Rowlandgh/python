users = {
    'liujing':{
            'sex':'35',
            'age':'one',
            'location':'beijing',
    },

    'xuxu':{
            'sex':'male',
            'age':'30',
            'location':'nanjing',
    },

    'hezhenjie':{
            'sex':'female',
            'age':'40',
            'location':'shanghai',
    },
}

for user_name,user_info in users.items():       #user_name和user_info分别对应字典的键和值
    print('用户名：' + user_name)
    sex = user_info['sex']
    age = user_info['age']
    location = user_info['location']
    #print('性别：' + sex )
    #print('年纪：' + age )
    #print('地区：' + location )

    print('性别：' + user_info['sex'] )
    print('年级：' + user_info['age'] )
    print('地区：' + user_info['location'] )

    # {}为字典   []为列表  ()为元组
    dic1 = {'xuxu':'1','liujing':'2','hezhenjie':'3'}
    dic2 = {'man':'nanren','women':'nvren'}
    dic3 = {'程序员':'programmer','设计师':'designer','美术':'artist'}
    templist = []
    templist.append(dic1)       #把字典添加到列表中
    templist.append(dic2)
    templist.append(dic3)
    print(templist)
    del templist[0:2]
    print('\n\n以下是删除后的结果：')
    print(templist)

