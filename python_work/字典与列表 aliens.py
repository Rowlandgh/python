alien_0 = {'color': 'green', 'points': 5}              #在列表中嵌套字典
alien_1 = {'color': 'yellow', 'points': 10} 
alien_2 = {'color': 'red', 'points': 15} 
aliens = [alien_0, alien_1, alien_2] 
for alien in aliens: 
    print(alien)

aliens = []
for alien_num in range(30):
    new_alien = {'color': 'green', 'points': 5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('......')

print('共创建了' + str(len(aliens)) + '个外星人.')

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[0:5]:
    print(alien)
print('......')

aliens = {
        '分数':['five','ten','twenty'],
        '颜色':['red','green','blue','yellow'],     #当字典中的某个键需要关联多个值时，可以使用列表来嵌套。
        '速度':['low','medium','fast'],
        }

for point in aliens['分数']:
    print(point)
print(aliens)


favors = {
        'xuxu':['C','VB','java'],
        'liujing':['java','python'],          
        'hezhenjie':['ruby','erlang','php'],
        }
for name,value in favors.items():                     #.items()返回键-值对照表
    print(name + "'s best lang is:" )
    for a in value:
        print('\t' + a)


