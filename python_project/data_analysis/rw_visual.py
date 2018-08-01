import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    plt.figure(dpi=128,figsize=(10,6))     #figure()用于指定图表的宽，高，分辨率和背景色。需要给figsize指定一个元组，指出窗口的尺寸，单位为英寸。
                                             # 也可以直接传dpi，每英寸多少像素
    point_numbers = list(range(rw.num_point))
    
    #这里给参数c赋值，作用是按照point_number表的顺序，由浅至深的着色
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=1)        #绘制主图
    #plt.plot(rw.x_values,rw.y_values,linewidth=5)

    plt.scatter(rw.x_values[0],rw.y_values[0],c='green',edgecolor='none',s=50)             #着重绘制起点
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',s=50)           #着重绘制终点
    
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk?(y/n):')
    if keep_running == 'n':
        break