import csv
from matplotlib import pyplot as plt    #用matplotlib绘制折线图（ line chart）
from datetime import datetime

filename = 'death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #for index,column_header in enumerate(header_row):  #enumerate()函数将一个可遍历的数据对象(如列表、元组或字符串)同时列出数据和数据下标
                                                        #enumerate(sequence, [start=0])  seq:一个遍历对象 start:下标起始位置
        #print(index,column_header)                       #打印后可知日期在第0列，最高气温在第1列。
    dates,highs,lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],'%Y-%m-%d')    # strptime把读到的字符串转换成date对象（年-月-日的格式）
            high = int(row[1])                              #把字符串转为int，让matplotlib能够读取
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')              #捕获缺少数据的错误
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    
fig = plt.figure(dpi=128,figsize=(10,6))            #指定图表的宽，高，分辨率和背景色。每英寸128像素
plt.plot(dates,highs,c='red',alpha=0.5)             # alpha设置透明度，0完全透明，1完全不透明
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)   #fill_between填充在同一x值上，两个y值之间的空白

title = 'Daily high and low temperatures - 2014\nnDeath Valley, CA'
plt.title(title,fontsize=24)
plt.xlabel('',fontsize= 16)
fig.autofmt_xdate()                                 #绘制斜的标签，以免彼此重叠
plt.ylabel("Temperature (F)",fontsize=16) 
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()