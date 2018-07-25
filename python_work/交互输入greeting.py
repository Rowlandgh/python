msg1 = input('tell me sth and i will respond to you.\n')    #input将用户的输入存为字符串
if  msg1 == 'i love u':
    print('u enter this:' + msg1)
    print('fuck now')


tempstring1 = '\n\nthis sentence is too long,so i must set it into a varity.'
tempstring1 += '\nplease enter your name.\n'                #运算符+=用于在prompt字符串的末尾附加一个字符串。
name = input(tempstring1)
if  name.lower() == 'rowland':
    print('hello my lord.im waiting for u so long.')


age = input('please tell me your age:\n')
age = int(age)
if age >= 18:
    print ('time is ticking，hurry up！')
else:
    print ('you are too young to continue,jump out now.')

num = input('input a num for me,and i will tell you its even or odd!:')
num = int(num)

if num % 2 == 0:                        # % 求模运算
    print(str(num) + ' is a even.')     #print时连接字符串，先把int型转成string型。
else:
    print(str(num) + ' is a odd.')