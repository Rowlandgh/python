import matplotlib.pyplot as plt

x_values = list(range(1,1001))            # x_value = [1,2,3,4,5]
y_values = [x**2 for x in x_values]    # y_value = [1,4,9,16,25]


#plt.scatter(x_value,y_value,c='red',edgecolors='none',s=40)          #绘制一个点，向函数传递x,y坐标，
                                                                    #c指数据点颜色，edgecolors指数据点的轮廓，s指数据点的尺寸
#plt.scatter(x_value,y_value,c=(0,0,0.8),edgecolors='none',s=40)    #c也可以使用RGB分量的形式传递，注意是元组。
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=40)  #cmap：使用颜色映射，越大的值颜色越深
#plt.plot(x_values,y_values,linewidth=5)
plt.title('Square Numbers',fontsize=24)     #指定标题
plt.xlabel('value',fontsize=14)             #为x轴设置标题和字体大小
plt.ylabel('Square of Value',fontsize=14)   #为y轴设置标题和字体大小
plt.tick_params(axis='both',which='major',labelsize=14)   #tick_params设置刻度的样式，both会影响所有轴的刻度，刻度的字号也设置了
plt.axis([0,1100,0,1100000])            # axis函数需要4个值：x轴的最小、最大值，y轴的最小、最大值   
plt.show()
plt.savefig('squares_plot.png',bbox_inches='tight')         #保存文件。第一个实参是文件名，第二个是把图表多余的空白裁掉。