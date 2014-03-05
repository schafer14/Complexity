import matplotlib.pyplot as pyplot
import random

xs = [x for x in range(0, 100)]
ys = [random.random()*100 for x in range(0, 100)]


pyplot.plot(xs, ys)
scale = 'linear'
pyplot.xscale(scale)
pyplot.yscale(scale)
pyplot.title('')
pyplot.xlabel('Numbers of camels in the world')
pyplot.ylabel('Murders per unit time')
pyplot.show()