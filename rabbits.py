import matplotlib.pyplot as pyplot

def gen(steps, r, xt):
	list = []
	for x in range(0, steps):
		xt1 = r * xt * (1.0 - xt)
		xt = xt1
		list.append(xt1)
	return list

def graph(steps, r=2, xt=.2):
	pyplot.plot(range(0, steps), gen(steps, r, xt))
	scale = 'linear'
	pyplot.xscale(scale)
	pyplot.yscale(scale)
	pyplot.title('')
	pyplot.xlabel('t')
	pyplot.ylabel('x(t)')
	pyplot.show()


graph(100, 4, .201)
	