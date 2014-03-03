import os
import matplotlib.pyplot as pyplot
from Generator import Generator

def etime():
	user, sys, chuser, chsys, real = os.times()
	return user + sys


def sum_plus(list):
	total = []
	for x in list:
		total += x
	return total

def sum_extend(list):
	total = []
	for x in list:
		total.extend(x)
	return total

def sum_sum(list):
	total = sum(list, [])
	return total 


g = Generator()
xs = []
ys = []
for it in [10, 100, 1000, 10000, 100000, 1000000]:
	list = []
	for thing in g.alpha_numeric_generator(it):
		list.append(thing)

	start = etime();
	sum_sum(list)
	end = etime();

	xs.append(it)
	ys.append(end - start)
	print 'Done' + `it`

pyplot.plot(xs, ys)
scale = 'log'
pyplot.xscale(scale)
pyplot.yscale(scale)
pyplot.title('')
pyplot.xlabel('n')
pyplot.ylabel('run time (s)')
pyplot.show()