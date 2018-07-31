import temp2 as t2
from temp3 import Testclass

a = 68756454
b = format(a)
print(b)


def mainsome():
    name = 'rowland'
    num = 1
    people = Testclass(name,num)
    print(people.name)
    t2.testpeople(people)
    print(people.name)

if __name__ == '__main__':
    mainsome()