import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]                   #输入值
squares = [1,4,9,16,25]                     #输出值
plt.plot(input_values,squares,linewidth=5)  #根据输入值x和输出值y画出图表，如果输入值不填，则该函数会智能推测
plt.title('Square Numbers',fontsize=24)     #指定标题
plt.xlabel('value',fontsize=14)             #为x轴设置标题和字体大小
plt.ylabel('Square of Value',fontsize=14)   #为y轴设置标题和字体大小
plt.tick_params(axis='both',labelsize=14)   #tick_params设置刻度的样式，both会影响所有轴的刻度，刻度的字号也设置了
plt.show()                  #打开matplotlib查看器，并显示绘制的图形