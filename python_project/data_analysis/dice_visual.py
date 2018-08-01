from die import Die
import pygal    #用Pygal绘制条形图 bar chart


die1 = Die()
die2 = Die(10)

results = [die1.roll()+die2.roll() for roll_num in range(1000)]

frequencies = [results.count(value) for value in range(2,die1.num_sides+die2.num_sides)]

hist = pygal.Bar()

hist.title = 'Result of rolling one D6 and one D10 50000 times.'
hist.x_labels = [str(n) for n in range(2,17)]
hist.x_title = "Result"
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10',frequencies)

hist.render_to_file('dice_visual.svg')