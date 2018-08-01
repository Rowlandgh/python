import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    plt.figure(dpi=128,figsize=(10,6))

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