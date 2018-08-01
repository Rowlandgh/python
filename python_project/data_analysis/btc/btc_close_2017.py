import json
import pygal
import math
from itertools import groupby

filename = '.\\btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)
dates = []
months = []
weeks = []
weekdays = []
close = []

for btc_dict in btc_data:           #文件是一个pyone列表，其中每个元素都是一个字典dict
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))       #python不能直接把带有小数点的字符串直接转成整型
 
    line_chart = pygal.Line(x_label_rotation=20,show_minor_x_labels=False)  #x_label_rotation让x轴的日期标签顺时针旋转20度
                                                                            #show_minor_x_labels设置是否显示所有x轴标签
    line_chart.title = '收盘价对数变换'
    line_chart.x_labels = dates
    N = 20                                                                  #坐标轴每20天显示一次
    line_chart.x_labels_major = dates[::N]                                  # alist[a:b:s]   s为步进值，默认1

    close_math_log = [math.log10(i) for i in close]                         #用对数变换来消除非线性的趋势，可以更清晰的看出周期性

    line_chart.add('log收盘价',close_math_log)
    line_chart.render_to_file('收盘价对数折线图.svg')

""" alist[a:b:s] 从a到b-1，s表示步进，缺省为1.  所以[a:b:1]相当于[a:b]
当s<0时，a默认为-1. b默认为-len(a)-1 . 所以[::-1] == [-1:-len(a)-1:-1]，从最后一个元素到第一个元素。 """


def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)),key=lambda i:i[0]):     # lambda 匿名函数 语法：    lambda 参数:表达式
        y_list = [v for i, v in y]                                          #参数：可选，如果提供，通常是逗号分隔的变量（位置参数）
        xy_map.append([x, sum(y_list) / len(y_list)])                    #表达式：不能包含分支或循环（但允许条件表达式），也不能包含return（或yield）。若为元组，则要用圆括号将其包起来。
    x_unique, y_mean = [*zip(*xy_map)]

    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart

idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], close[:idx_month], '收盘价月日均值', '月日均值')
line_chart_month


idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week], close[1:idx_week], '收盘价周日均值', '周日均值')
line_chart_week

idx_week = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int, close[1:idx_week], '收盘价星期均值', '星期均值')
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line_chart_weekday.render_to_file('收盘价星期均值（¥）.svg')
line_chart_weekday

