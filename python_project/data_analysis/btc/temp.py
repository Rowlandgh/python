import string

def  bracket(data):
    return data
 
if __name__ == '__main__':
    # 不带括号调用的结果：<function bracket at 0x0000000004DD0B38>,a是整个函数体，是一个函数对象，不须等该函数执行完成
    a = bracket
    print(a)
    # 带括号调用的结果：6 ,b是函数执行后返回的值6,须等该函数执行完成的结果
    b = bracket(6)
    print(b)


def test():
    test_list = [('a','3','C'),('c','2','B'),('b','1','A')]
    final_list = sorted(test_list,key=lambda i:i[1],reverse=False)
    print(final_list)

test()