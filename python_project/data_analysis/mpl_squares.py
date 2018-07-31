import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
plt.plot(squares,linewidth=5)           #plot尝试根据提供的数字绘制出有意义的图形,linewidth决定线条的粗细
plt.title('Square Numbers',fontsize=24)     #   指定标题
plt.xlabel('value',fontsize=14)             #为x轴设置标题和字体大小
plt.ylabel('Square of Value',fontsize=14)   #为y轴设置标题和字体大小
plt.tick_params(axis='both',labelsize=14)   #tick_params设置刻度的样式，both会影响所有轴的刻度，刻度的字号也设置了
plt.show()                  #打开matplotlib查看器，并显示绘制的图形
